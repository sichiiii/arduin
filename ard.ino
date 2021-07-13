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
