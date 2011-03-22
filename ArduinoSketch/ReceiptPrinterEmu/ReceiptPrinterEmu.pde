#include <LCD4Bit_mod.h>
LCD4Bit_mod lcd = LCD4Bit_mod(2); 
//#define BAUD 9600

boolean pagemode = false;
char line0[41];
char line1[41];
char line2[41];
char linecounter = 0;

void setup() {
  lcd.init();
  Serial.begin(9600);
  Serial.println("Hello.");
  lcd.clear();
  sprintf(line0,"");
  sprintf(line1,"");
  sprintf(line2,"");
  lcd.printIn("ESC/POS Emulator");
  lcd.cursorTo(2, 0);
  lcd.printIn("2011-03-14");
  delay(1500);
}

void ProcessGS() {
  
}

void ProcessESC() {
  
}

void newline() {
 lcd.printIn("NewLine");
 strcpy(line0,line1);
 strcpy(line1,line2);
 linecounter = 0;
 strcpy(line2,""); 
}

void cut() {
 sprintf(line2,"******CUT*******");
 newline(); 
}

void loop() {
  boolean changed = false;
  if(Serial.available() > 0) {
   char incoming = Serial.read();
   switch(incoming) {
     case '\r':
    case '\n':
     newline();
     changed = true;
     break;
    
      /*linecounter = 0;
      break;*/
    case '\t':
      changed = true;
      for(int i=0;i<4;i++) {
       if(linecounter == 40)
         line2[linecounter] = '\0';
       else
         line2[linecounter++] = ' ';
      }
    break;
    case 12: //FF
      newline();
      cut();
      changed = true;
    break;
    case 29:
      ProcessGS();
      changed = true; //maybe
    break;
    case 27:
      ProcessESC();
      changed = true;//maybe
    default:
      if(linecounter > 39)
        newline();
       line2[linecounter++] = incoming;
       line2[linecounter] = '\0';
       changed = true;
      break;
   }
   if(!changed)
     return;
   //print lines to screen
   lcd.clear();
   lcd.cursorTo(1, 0);
   lcd.printIn(line0);
   lcd.cursorTo(2, 0);
   lcd.printIn(line1);
  }
}

