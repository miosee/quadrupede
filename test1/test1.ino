#include <Servo.h>

Servo servo[4][3];
const int servo_pin[4][3] = { {2, 3, 4}, {5, 6, 7}, {8, 9, 10}, {11, 12, 13} };
const int aInit[4][3] = { {90, 90, 135}, {90, 90, 45}, {90, 90, 45}, {90, 90, 135} };

int a[4][3];;
int i, j;

void setup() {
  delay(1000);
  Serial.begin(115200);
  
  for (i = 0; i < 4; i++) {
    for (j = 0; j < 3; j++) {
      servo[i][j].attach(servo_pin[i][j]);
      a[i][j] = aInit[i][j];
      servo[i][j].write(a[i][j]);
    }
  }
  i = 0;
  j = 0;
}


void loop() {
  if (Serial.available()) {
    switch (Serial.read()) {
      case 'u':
        a[i][j] += 5;
        servo[i][j].write(a[i][j]);
        break;
      case 'd':
        a[i][j] -= 5;
        servo[i][j].write(a[i][j]);
        break;
      case 'i':
        i++;
        if (i > 3) {
          i = 0;
        }
        break;
      case 'j':
        j++;
        if (j > 2) {
          j = 0;
        }
        break;
    }
    Serial.print("a : ");
    Serial.print(a[i][j]);
    Serial.print(", i : ");
    Serial.print(i);
    Serial.print(", j : ");
    Serial.println(j);
  }
}
