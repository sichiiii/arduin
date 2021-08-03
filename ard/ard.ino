#include <ArduinoJson.h>

String inData;

int digitalD5 = 5;
int digitalD7 = 7;
int digitalD6 = 6;
int analogA5 = A5;
int digitalD3 = 3;

void setup() {
  Serial.begin(9600);
  pinMode(digitalD5, OUTPUT);
  pinMode(digitalD7, OUTPUT);
  pinMode(digitalD6, OUTPUT);
  pinMode(analogA5, OUTPUT);
  pinMode(digitalD3, OUTPUT);
  while(!Serial){
  }
}

void loop() {
      int     size_ = 0;
      String  payload;
      while ( !Serial.available()  ){}
      if ( Serial.available() )
        payload = Serial.readStringUntil( '\n' );
      StaticJsonDocument<512> doc;
    
      DeserializationError   error = deserializeJson(doc, payload);
      if (error) {
        Serial.println(error.c_str()); 
        return;
      }
      String command = doc["command"];
      
      if(doc["command"] == "conveer") {
        Serial.println("{\"value\":\"conveer has been received\"}");
      }
      if(doc["command"] == "blade") {
        Serial.println("blade has been received");
      }
      if(doc["command"] == "escape") {
        Serial.println("escaoe has been received");
      }
      if(doc["command"] == "weight") {
        Serial.println(123);
      }
      if(doc["command"] == "check") {
        Serial.println("check has been received");
      }
      //serializeJson(doc, Serial);
      //Serial.println("not");
      delay(100);
    }
  
