#include <Wire.h>

//---Globals---

const int DRV_count = 6;

//All pins used
const int pins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, LED_BUILTIN};

//All DRVs in with their respective pins
const int DRVs[DRV_count][2] = {{2, 3}, {4, 5}, {6, 7}, {8, 9}, {10, 11}, {14, 15}};

void setup() {
  //set all pins as out
  for(int i = 0; i < 18; i++)
  {
    pinMode(pins[i], OUTPUT);
  }
  //setup I2C between Pi and Nano
  Wire.begin(0x8);
  Wire.onReceive(recieveEvent);
}

void recieveEvent(int howMany) {
  while(Wire.available()) {
    char m = Wire.read();
  }
  blinkLED();
}

void loop() {
  //testDRVs();
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
  delay(1);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1);
}