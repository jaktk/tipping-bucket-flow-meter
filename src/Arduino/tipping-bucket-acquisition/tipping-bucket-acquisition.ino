int flowsensor = 2;
int hallsensor = 3;
unsigned long currentTime;
unsigned long lastTime;
unsigned long pulse_freq_tip;
unsigned long pulse_freq_flow;
double flow_lpm;
 
void flow_pulse() {
  pulse_freq_flow++;
}

void tip_pulse() {
  pulse_freq_tip++;
}

void setup() {
  pinMode(flowsensor, INPUT);
  pinMode(hallsensor, INPUT);
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(flowsensor), flow_pulse, RISING);
  attachInterrupt(digitalPinToInterrupt(hallsensor), tip_pulse, RISING);
  currentTime = millis();
  lastTime = currentTime;
}

void loop() {
  currentTime = millis();
  if(currentTime >= (lastTime + 1000)) {
    lastTime = currentTime;
    flow_lpm = (pulse_freq_flow / 7.5);
    if (flow_lpm < 1) flow_lpm = 0;
    Serial.print(flow_lpm, DEC);
    Serial.print(",");
    Serial.println(pulse_freq_tip, DEC);
    pulse_freq_flow = 0;
    pulse_freq_tip = 0;
   }
}
