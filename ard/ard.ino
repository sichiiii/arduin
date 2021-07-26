#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
}

int analogPinA5 = 5;
int digitalPinD3 = 3;
int digitalPinD5 = 5;
int digitalPinD6 = 6;
int digitalPinD7 = 7;

void read_command(String json)
{
  
  DynamicJsonDocument doc(1024);
  deserializeJson(doc, json);

  pinMode(digitalPinD5, OUTPUT);
  pinMode(digitalPinD6, OUTPUT);
  pinMode(digitalPinD7, OUTPUT);

  pinMode(analogPinA5, OUTPUT);

  
  const char* sensor = doc["sensor"];
  long time          = doc["time"];
  double latitude    = doc["data"][0];
  double longitude   = doc["data"][1];
  String command     = doc["command"];

  if (doc["command"] == "volume_sensor") 
  {
  digitalWrite(digitalPinD3, HIGH); // sets the pin on
  delay(500);     
  digitalWrite(digitalPinD3, LOW);  // sets the pin off
  delay(500);
  }
  
  if (doc["command"] == "enable_engine") 
  {
  digitalWrite(digitalPinD5, HIGH); // sets the pin on
  delay(10000);     
  digitalWrite(digitalPinD5, LOW);  // sets the pin off
  delay(500);
  }

  if (doc["command"] == "ejection") 
  {
  digitalWrite(digitalPinD6, HIGH); // sets the digital pin 13 on
  delay(500);            
  digitalWrite(digitalPinD6, LOW);  // sets the digital pin 13 off
  delay(500);
  }
    
  if (doc["command"] == "crusher") 
  {
  digitalWrite(digitalPinD7, HIGH); // sets the pin on
  delay(500);     
  digitalWrite(digitalPinD7, LOW);  // sets the pin off
  delay(500);
  }  

  if (doc["command"] == "tensa") 
  {
  analogWrite(analogPinA5, HIGH); // sets the pin on
  delay(500);     
  analogWrite(analogPinA5, LOW);  // sets the pin off
  delay(500);
  }  
}



void loop() {
  int stateButton = random(0, 10);
  if(Serial.available() > 0){
    read_command(Serial.readString());
  }

  
  StaticJsonDocument<200> doc;

  
  doc["status"] = 0;
  doc["test"] = "test";
  doc["data"]["test_input"] = stateButton;

  serializeJson(doc, Serial);
 

  // Start a new line
  Serial.println();
  delay(100);
  
}
