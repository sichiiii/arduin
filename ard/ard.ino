#include <ArduinoJson.h>

String inData;

int digitalD5 = 5;
int digitalD7 = 7;
int digitalD6 = 6;
int analogA5 = A5;
int digitalD3 = 3;

float val1 = 0.0;
bool val2 = 0;

StaticJsonDocument<200> flask;
StaticJsonDocument<200> sensors;

void setup() {
  Serial.begin(9600);
  pinMode(digitalD5, OUTPUT);
  pinMode(digitalD7, OUTPUT);
  pinMode(digitalD6, OUTPUT);
  pinMode(analogA5, INPUT);
  pinMode(digitalD3, INPUT);
}

void loop() {
       deserializeJson(sensors, Serial);
       deserializeJson(flask, Serial);
       
       if (flask["command"] == "conveer"){
            digitalWrite(digitalD5, LOW);
            delay(5);
            digitalWrite(digitalD7, LOW);
            delay(5);
            digitalWrite(digitalD5, HIGH);   
       }
       if (flask["command"] == "blade"){
            digitalWrite(digitalD5, LOW);
            delay(5);
            digitalWrite(digitalD7, LOW);
            delay(5);
            digitalWrite(digitalD7, HIGH);       
       }
       if (flask["command"] == "escape"){
            digitalWrite(digitalD5, LOW);
            delay(5);
            digitalWrite(digitalD7, LOW);
            delay(5);
            digitalWrite(digitalD6, HIGH);  
       }            
       val1 = analogRead(analogA5);     
       val2 = digitalRead(digitalD3);
       sensors["weight"] = val1;
       sensors["check"] = val2; 
       serializeJson(sensors, Serial);
}

  
