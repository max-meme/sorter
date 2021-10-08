#include <Wire.h>

//---Globals---

const int DRV_count = 6;
const int adress = 0x8;
char temp[32];
volatile boolean receiveFlag = false;

//All pins used
const int pins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, LED_BUILTIN};

//All DRVs in with their respective pins
const int DRVs[DRV_count][2] = {{2, 3}, {4, 5}, {6, 7}, {8, 9}, {10, 11}, {14, 15}};

void setup() {
  //set all pins as out
  for(int i = 0; i < 19; i++)
  {
    pinMode(pins[i], OUTPUT);
  }
  //setup I2C between Pi and Nano
  Wire.begin(adress);
  Wire.onReceive(recieveEvent);
}

void recieveEvent(int howMany) {
  int m = 0;
  while(Wire.available()) {
    m = Wire.read();
  }
  
  for (int i = 0; i < howMany; i++) {
      temp[i] = Wire.read();
      temp[i + 1] = '\0'; //add null after ea. char
    }

  //RPi first byte is cmd byte so shift everything to the left 1 pos so temp contains our string
  for (int i = 0; i < howMany; ++i)
    temp[i] = temp[i + 1];
  blinkLED();
  receiveFlag = true;
}

void loop() {
  //testDRVs();
  delay(100);
  if (receiveFlag == true) {
    Serial.println(temp);
    receiveFlag = false;
  }
}

void testDRVs() {
  for(int i = 0; i < DRV_count; i++) {
    int step_pin = DRVs[i][1];
    int dir_pin = DRVs[i][2];

    digitalWrite(dir_pin, LOW);
    for(int j = 0; j < 100; j++) {
      digitalWrite(step_pin, HIGH);
      delay(0.01);
      digitalWrite(step_pin, LOW);
      delay(0.01);
    }

    digitalWrite(dir_pin, HIGH);
    for(int j = 0; j < 100; j++) {
      digitalWrite(step_pin, HIGH);
      delay(0.01);
      digitalWrite(step_pin, LOW);
      delay(0.01);
    }
  }
}

void blinkLED() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);
}