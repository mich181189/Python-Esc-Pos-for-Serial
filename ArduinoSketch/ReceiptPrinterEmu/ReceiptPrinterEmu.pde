#include <LCD4Bit_mod.h>
LCD4Bit_mod lcd = LCD4Bit_mod(2); 
#define BAUD 9600

boolean pagemode = false;
char line1[41];
char line2[41];
char linecounter = 0;

void setup() {
  Serial.begin(BAUD);
  lcd.clear();
  sprintf(line1,"");
  sprintf(line2,"");
  lcd.printIn("ESC/POS Emulator");
  lcd.cursorTo(2, 0);
  lcd.printIn("2011-03-14");
  delay(1500);
}

void ProcessGS() {
  
}

void processESC() {
  
}

void newline() {
 strcpy(line1,line2);
 linecounter = 0;
 strcpy(line2,""); 
}

void loop() {
  boolean changed = false;
  if(Serial.available() > 0) {
   char incoming = Serial.read();
   switch(incoming) {
    case '\n':
     newline();
     changed = true;
     break;
    case '\r':
      linecounter = 0;
      break;
    default:
      ++linecounter;
      if(linecounter > 40)
        newline();
       line2[linecounter] = incoming;
       line2[linecounter+1] = '\0';
       changed = true;
      break;
   }
   if(!changed)
     return;
   //print lines to screen
   lcd.clear();
   lcd.cursorTo(1, 0);
   lcd.printIn(line1);
   lcd.cursorTo(2, 0);
   lcd.printIn(line2);
  }
}

