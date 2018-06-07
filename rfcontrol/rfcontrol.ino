#include <StringSplitter.h> //https://github.com/aharshac/StringSplitter
#include <LiquidCrystal.h>  //https://github.com/miguelbalboa/rfid
#include <MFRC522.h>

#define LED_VERDE A4
#define LED_VERMELHO A5
#define BUZZER 8
#define SS_PIN 10
#define RST_PIN 9

//lcd display
const int DISPLAY_HORIZONTAL_SIZE = 16, DISPLAY_VERTICAL_SIZE = 2;
const int rs = 7, en = 6, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

//rfid reader
MFRC522 leitorRFID(SS_PIN, RST_PIN);

//messages to be displayed
const String MESSAGE_ASK_FOR_CARD = "APROXIME SEU CARTAO DO LEITOR",
             MESSAGE_WELCOMING = "BEM-VINDO, DANIEL",
             MESSAGE_DENYING_CARD = "CARTAO RECUSADO!",
             MESSAGE_BLOCKED_SYSTEM = "SISTEMA BLOQUEADO!";

//control variables
const int FIRST_ROW = 1, SECOND_ROW = 2;
String currentExhibitedMessage = "";

enum rowValue {
  first,
  second
};

String TagsCadastradas[] = {"b5da2b77"};
int timesDenied = 0;

void setup()
{
  //pinning leds and buzzer
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  //initializing modules
  Serial.begin(9600);
  SPI.begin();
  lcd.begin(DISPLAY_HORIZONTAL_SIZE, DISPLAY_VERTICAL_SIZE);
  leitorRFID.PCD_Init();
}

//================================================================================================================

void loop()
{
  if (!isBlocked())
  {
    showMessage(MESSAGE_ASK_FOR_CARD);

    // check if there is a tag present
    if (!leitorRFID.PICC_IsNewCardPresent() || !leitorRFID.PICC_ReadCardSerial()) {
      delay(50);
      return;
    }

    String idTag = "";

    //getting idTag from the RFID reader
    for (byte i = 0; i < leitorRFID.uid.size; i++) {
      idTag.concat(String(leitorRFID.uid.uidByte[i], HEX));
    }

    if (isAccessGranted(idTag))
      allowAccess();
    else
      denyAccess();
    delay(2000); //wait 2 seconds before waiting for a new reading
  }
}

bool isBlocked()
{
  return timesDenied >= 3;
}

bool isAccessGranted (String tag)
{
  //checking if idTag is registered
  for (int i = 0; i < (sizeof(TagsCadastradas) / sizeof(String)); i++) {
    if (tag.equalsIgnoreCase(TagsCadastradas[i]))
      return true;
  }

  return false;
}

void allowAccess() {

  showMessage(MESSAGE_WELCOMING);
  
  digitalWrite(LED_VERDE, HIGH);
  delay(3000);

  digitalWrite(LED_VERDE, LOW);
  delay(100);
}

void denyAccess()
{
  emitDenyingAlert();

  //checking if system is blocked
  timesDenied++;
  if (timesDenied >= 3)
    blockSystem();
}

void emitDenyingAlert ()
{
  //displaying message and lighting up red led
  showMessage(MESSAGE_DENYING_CARD);
  digitalWrite(LED_VERMELHO, HIGH);

  delay(3000);

  digitalWrite(LED_VERMELHO, LOW);
}

void blockSystem ()
{
  showMessage(MESSAGE_BLOCKED_SYSTEM);

  digitalWrite(LED_VERMELHO, HIGH);

  //emiting sound for three seconds
  tone(BUZZER, 500);
  delay(3000);
  noTone(BUZZER);
}

void showMessage (String message)
{
  //in order to avoid calculating, spliting, clearing and displaying the same message on display
  if (message.equalsIgnoreCase(currentExhibitedMessage))
    return;

  currentExhibitedMessage = message;

  lcd.clear();

  //[0] - string to be displayed on first row
  //[1] - string to be displayed on second row
  String parts [2];

  if (fitsInOneLine(message))
  {
    printCentralizedMessage(message, first);
  }
  else
  {
    splitMessage(parts, message);
    printCentralizedMessage(parts[0], first);
    printCentralizedMessage(parts[1], second);
  }
}

bool fitsInOneLine(String message) {
  return message.length() <= DISPLAY_HORIZONTAL_SIZE;
}

void printCentralizedMessage(String message, rowValue row)
{
  //get number of spaces to the left
  int numberOfSpacesInGeneral = DISPLAY_HORIZONTAL_SIZE - message.length();
  float numberOfSpacesNotRounded = numberOfSpacesInGeneral / 2;
  int numberOfSpacesToTheLeftRounded = (int) numberOfSpacesNotRounded;

  //adding that number of spaces
  String resultingMessage = "";
  for (int i = 0; i < numberOfSpacesToTheLeftRounded; i++)
    resultingMessage += " ";

  //adding message
  resultingMessage += message;

  //change row to which the message will be printed to rowValue
  if (row == first)
    firstLine();
  else
    secondLine();

  //printing format value
  lcd.print(resultingMessage);
}

void splitMessage(String * parts, String message)
{

  const int MAX_NUMBER_WORDS = 20;
  const int FIRST_ROW = 0, SECOND_ROW = 1;

  StringSplitter *splitter = new StringSplitter(message, ' ', MAX_NUMBER_WORDS);
  int qntWords = splitter -> getItemCount();

  String currentRow = "";       // the line to be added to the parts array
  int currentRowIndex = 0;      // to which part of the array the word will be added to
  int currentRowCharacters = 0; // current amount of characters in a row, to check if it fits

  for (int i = 0; i < qntWords && currentRowIndex < 2; i++)
  {
    String word = splitter -> getItemAtIndex(i);

    //what is happening:
    //if it is the first line, we are going to add to the list, and increment our
    //variables so that we can continue this process on the next line
    //if it is the second, we are going to the second row anyway, as it wont be displayed

    //skipping to the next row
    //if if the first line and it wont fit
    if (currentRow.length() + word.length() > DISPLAY_HORIZONTAL_SIZE && currentRowIndex == FIRST_ROW)
    {
      //attributing to array to be returned
      //cleaning string variable for current row, in case it's the first one
      //incrementing number of rows added
      parts[currentRowIndex] = currentRow;
      currentRow = "";
      currentRowIndex++;
    }

    //adding word
    //if first line and fits or if is just the second line
    if ((currentRowIndex == FIRST_ROW && currentRow.length() + word.length() < DISPLAY_HORIZONTAL_SIZE) || currentRowIndex == SECOND_ROW)
      currentRow += word + " ";

  }

  //second row, left over from when we got out of the loop
  parts[SECOND_ROW] = currentRow;

  //removing space at the end, since we always add it
  parts[0].remove(parts[0].length() - 1);
  parts[1].remove(parts[1].length() - 1);
}

//cursor moving cursor functions
void firstLine()
{
  lcd.setCursor(0, 0);
}
void secondLine()
{
  lcd.setCursor(0, 1);
}
