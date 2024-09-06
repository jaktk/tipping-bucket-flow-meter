int flowsensor = 2; 
unsigned long currentTime;
unsigned long lastTime;
unsigned long pulse_freq;
unsigned long flow_lpm;
 
void pulse() {
  pulse_freq++;
}

void setup() {
  pinMode(flowsensor, INPUT);
  Serial.begin(9600);
  attachInterrupt(0, pulse, RISING);
  currentTime = millis();
  lastTime = currentTime;
}

void loop() {
  currentTime = millis();
  if(currentTime >= (lastTime + 1000)) {
    lastTime = currentTime;
    flow_lpm = pulse_freq / 7.5;
    if (flow_lpm < 1) flow_lpm = 0;
    Serial.println(flow_lpm, DEC);
    pulse_freq = 0;
   }
}
