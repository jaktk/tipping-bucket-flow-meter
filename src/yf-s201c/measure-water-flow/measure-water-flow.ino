int flowsensor = 2; 
unsigned long currentTime;
unsigned long lastTime;
unsigned long pulse_freq;
 
void pulse ()
{
  pulse_freq++;
}

void setup()
{
  pinMode(flowsensor, INPUT);
  Serial.begin(9600);
  attachInterrupt(0, pulse, RISING);
  currentTime = millis();
  lastTime = currentTime;
}

void loop()
{
  currentTime = millis();
  if(currentTime >= (lastTime + 1000))
  {
    lastTime = currentTime;
    Serial.println(pulse_freq, DEC);
    pulse_freq = 0;
   }
}
