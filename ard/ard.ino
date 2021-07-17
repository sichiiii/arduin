#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
}



void read_command(String json)
{
  
  DynamicJsonDocument doc(1024);
  deserializeJson(doc, json);
  
  const char* sensor = doc["sensor"];
  long time          = doc["time"];
  double latitude    = doc["data"][0];
  double longitude   = doc["data"][1];
  String command     = doc["command"];
  if (doc["command"] == "ejection") 
  {
  digitalWrite(LED_BUILTIN, HIGH); // Включение светодиода
  delay(1000);                     // Задержка
  digitalWrite(LED_BUILTIN, LOW);  // Выключение светодиода
  delay(1000);
  digitalWrite(3, HIGH); // sets the digital pin 13 on
  delay(500);            // waits for a second
  digitalWrite(3, LOW);  // sets the digital pin 13 off
  delay(500);
  }
  if (doc["command"] == "enable_engine") 
  {
  digitalWrite(5, HIGH); // sets the digital pin 13 on
  delay(10000);            // waits for a second
  digitalWrite(5, LOW);  // sets the digital pin 13 off
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
