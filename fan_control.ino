String person;
int fanRelay = 8;

void setup() {
  // put your setup code here, to run once:
    pinMode(fanRelay, OUTPUT);

    Serial.begin(115200);
}

void loop() {
    while (Serial.available() == 0){
        
    }
    
    person = Serial.readStringUntil('\r');
    
    if (person == "present"){
        digitalWrite(fanRelay, HIGH);
    }

    if (person == "absent"){
        digitalWrite(fanRelay, LOW);
    }
}
