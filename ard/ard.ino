#include <ArduinoJson.h>

String inData;

int conveer_D5 = 5;
int blade_D7 = 7;
int escape_D6 = 6;
int tensa_A5 = A5;
int check_D3 = 3;

float val1 = 0.0;
bool val2 = 0;

StaticJsonDocument<200> flask;
StaticJsonDocument<200> sensors;

void setup() {
  Serial.begin(9600);
  pinMode(conveer_D5, OUTPUT);
  pinMode(blade_D7, OUTPUT);
  pinMode(escape_D6, OUTPUT);
  pinMode(tensa_A5, INPUT);
  pinMode(check_D3, INPUT);
}

void loop() {
       deserializeJson(sensors, Serial);
       deserializeJson(flask, Serial);
       
       if (flask["command"] == "conveer"){
            digitalWrite(escape_D6, LOW);
            digitalWrite(blade_D7, LOW);
            digitalWrite(conveer_D5, HIGH);   
       }
       if (flask["command"] == "blade"){
            digitalWrite(conveer_D5, LOW);
            digitalWrite(blade_D7, LOW);
            digitalWrite(blade_D7, HIGH);       
       }
       if (flask["command"] == "escape"){
            digitalWrite(conveer_D5, LOW);
            digitalWrite(blade_D7, LOW);
            digitalWrite(escape_D6, HIGH);  
       }
       if (flask["command"] == "stop"){
            digitalWrite(conveer_D5, LOW);
            digitalWrite(blade_D7, LOW);
            digitalWrite(escape_D6, LOW);
       }
       val1 = analogRead(tensa_A5);     
       val2 = digitalRead(check_D3);
       sensors["weight"] = val1;
       sensors["check"] = val2;
       delay(100); 
       serializeJson(sensors, Serial);
}

  
