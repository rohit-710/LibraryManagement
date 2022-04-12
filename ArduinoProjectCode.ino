#include  <SPI.h>
#include  <MFRC522.h>
#include  <Keypad.h>
#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

const int buzzer = 3;

char customKey;

const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns

// ---------------------------------------------------------------------------------
//define the symbols on the buttons of the keypads
// ---------------------------------------------------------------------------------
char hexaKeys[ROWS][COLS] = {
                               {'1','2','3','A'},
                               {'4','5','6','B'},
                               {'7','8','9','C'},
                               {'*','0','#','D'}
                            };

// Following two lines define how the Keypad rows and columns are connected
byte rowPins[ROWS] = {  5, 8, 7, 6};     //connect to the row pinouts of the keypad
byte colPins[COLS] = { 14,15,16,17};   //connect to the column pinouts of the keypa

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);





// ---------------------------------------------------------------------------------
void setup()
// ---------------------------------------------------------------------------------
{
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);
  
  Serial.begin(9600);                 // Initialize serial communications with the PC
  pinMode(buzzer, OUTPUT);            //
  while (!Serial);                    // Do nothing if no serial port is opened
  SPI.begin();                        // Init SPI bus
  mfrc522.PCD_Init();                 // Init MFRC522
  delay(200);                         // Optional delay.
  mfrc522.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader
  
  Serial.println("-----------------------------------------------------------");
  Serial.println("Press '0' on the keyboard for the Main Menu");
  Serial.println("Press '*' on the keyboard for the Arduino Project details");
  Serial.println("-----------------------------------------------------------");

}

// ---------------------------------------------------------------------------------
void loop()
// ---------------------------------------------------------------------------------
{
  delay(100);
  customKey = customKeypad.getKey();

  switch (customKey)
  {
     case '0':
         PadBeep();
         Serial.print("TXN00:-SKIP\r\n");
         break;
     case '1':
         PadBeep();
         Serial.print("TXN01:-SKIP\r\n");
         break;
     case '2':
         PadBeep();
         Serial.print("TXN02:-SKIP\r\n");
         break;
     case '3':
         PadBeep();
         Serial.print("TXN03:-SKIP\r\n");
         break;
     case '4':
         PadBeep();
         Serial.print("TXN04:-SKIP\r\n");
         break;
     case '5':
         PadBeep();
         Serial.print("TXN05:-SKIP\r\n");
         break;
     case '6':
         PadBeep();
         Serial.print("TXN06:-SKIP\r\n");
         break;
     case '7':
         PadBeep();
         Serial.print("TXN07:-SKIP\r\n");
         break;




     case '8':
         PadBeep();
         Serial.print("TXN08:-SKIP\r\n");
         break;
     case '9':
         PadBeep();
         Serial.print("TXN09:-SKIP\r\n");
         break;
     case 'A':
         PadBeep();
         Book_Checkout();
         break;
     case 'B':
         PadBeep();
         Book_Return();
         break;
     case 'C':
         PadBeep();
         Patron_details();
         break;
     case 'D':
         PadBeep();
         Book_details();
         break;
     case '*':
         PadBeep();
         Serial.print("TXN0*:-SKIP\r\n");
         break;
     case '#':
         PadBeep();
         Serial.print("TXN0#:-SKIP\r\n");
         break;
     default:
         break;
   }     // End of SWITCH - CASE statement
}        // End of LOOP function




// ---------------------------------------------------------------------------------
// Function to Borrow a Book:
// ---------------------------------------------------------------------------------

// ---------------------------------------------------------------------------------
void Book_Checkout()
// ---------------------------------------------------------------------------------
{
   int x = 0;
   String content1= "";
   String content2= "";
   while(true)
   {
       delay(300);
       if(x == 0)
       {
          Serial.print("Selected - Issue Book transaction ...\r\n");
          Serial.print("Please scan the ID card ...\r\n");
          x++;
       }
       if ( ! mfrc522.PICC_IsNewCardPresent())
       {
          continue;
       }

       if ( ! mfrc522.PICC_ReadCardSerial())
       {
          continue;
       }

       byte letter;
       for (byte i = 0; i < mfrc522.uid.size; i++)
       {
          content1.concat(String(mfrc522.uid.uidByte[i], HEX));
       }
       tone(buzzer, 250);
       delay(200);                       // wait for a second
       noTone(buzzer);
       delay(500);
       content1.toUpperCase();
       break;
    }     // End of WHILE-TRUE loop

   x = 0;
   while(true)
   {
       delay(300);
       if(x == 0)
       {
          Serial.print("Please scan the Book ...\r\n");
          x++;
       }
       if ( ! mfrc522.PICC_IsNewCardPresent())
       {
        continue;
       }

       if( ! mfrc522.PICC_ReadCardSerial())
       {
          continue;
       }



       byte letter;
       for (byte i = 0; i < mfrc522.uid.size; i++)
       {
          content2.concat(String(mfrc522.uid.uidByte[i], HEX));
       }
       tone(buzzer, 250);
       delay(200);                       // wait for a second
       noTone(buzzer);
       delay(500);
       content2.toUpperCase();
       String Sep01= "-";
       String Sep02= "\r\n";
       Serial.print("TXN0A:"+Sep01+content1+Sep01+content2+Sep02);
       break;
    }     // End of WHILE-TRUE loop


  return;
}         // End of the function Book_Checkout()

// ---------------------------------------------------------------------------------
// Function to Return a Book:
// ---------------------------------------------------------------------------------
// ---------------------------------------------------------------------------------
void Book_Return()
// ---------------------------------------------------------------------------------
{
  int x = 0;
while(true)
{

  delay(500);
  if(x == 0)
  {
     Serial.print("Selected Return Book ...\r\n");
     Serial.print("Please scan the book ...\r\n");
     x++;
  }
  if ( ! mfrc522.PICC_IsNewCardPresent())
  {
    continue;
  }

  if ( ! mfrc522.PICC_ReadCardSerial())
  {
    continue;
  }

  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     //content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));

  }
  tone(buzzer, 250);
  delay(200);                       // wait for a second
  noTone(buzzer);
  delay(500);
  content.toUpperCase();
  Serial.print("TXN0B:-"+content+"\r\n");
  break;
  }

return;
}


// ---------------------------------------------------------------------------------
// Function to Display Student Details:
// ---------------------------------------------------------------------------------

// ---------------------------------------------------------------------------------
void Patron_details()
// ---------------------------------------------------------------------------------
{
  int x = 0;
while(true)
{

  delay(500);
  if(x == 0)
  {
     Serial.print("Selected Student detail ...\r\n");
     Serial.print("Please scan the ID card ...\r\n");
     x++;
  }
  if ( ! mfrc522.PICC_IsNewCardPresent())
  {
    continue;
  }

  if ( ! mfrc522.PICC_ReadCardSerial())
  {
    continue;
  }

  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
     //content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));

  }
  tone(buzzer, 250);
  delay(200);                       // wait for a second
  noTone(buzzer);
  delay(500);
  content.toUpperCase();
  Serial.print("TXN0C:-"+content+"\r\n");
  break;
  }

return;
}


// ---------------------------------------------------------------------------------
// Function to Display Book Details:
// ---------------------------------------------------------------------------------

// ---------------------------------------------------------------------------------
void Book_details()
// ---------------------------------------------------------------------------------
{
  int x = 0;
while(true)
{

  delay(500);
  if(x == 0)
  {
     Serial.print("Selected Book detail ...\r\n");
     Serial.print("Please scan the Book ...\r\n");
     x++;
  }
  if ( ! mfrc522.PICC_IsNewCardPresent())
  {
    continue;
  }

  if ( ! mfrc522.PICC_ReadCardSerial())
  {
    continue;
  }
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  tone(buzzer, 250);
  delay(200);                       // wait for a second
  noTone(buzzer);
  delay(500);
  content.toUpperCase();
  Serial.print("TXN0D:-"+content+"\r\n");
  break;
  }

return;
}

// ---------------------------------------------------------------------------------
// Function to Manage the Beeper:
// ---------------------------------------------------------------------------------

// ---------------------------------------------------------------------------------
void PadBeep()
// ---------------------------------------------------------------------------------
{
    tone(buzzer, 2750);
    delay(50);
    noTone(buzzer);
    delay(50);
    return;
}
