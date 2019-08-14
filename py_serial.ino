int red = 5;
int green = 3;
int blue = 4;


void setup()
{
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    if (Serial.read() == 'l')
    {
      digitalWrite(blue, HIGH);
      delay(1000);
      digitalWrite(blue,LOW);
    }
  }
  else if (Serial.read() == 't') {
    for (int i = 0; i < 100; i++) {
      analogWrite(blue, random(0, 500));
      analogWrite(red, random(0, 100));
      analogWrite(green, random(0, 100));
      delay(10);
    }
  }
  else if (Serial.read() == 'n') {
    digitalWrite(red, HIGH);
    delay(1000);
  }
  else
  {
    digitalWrite(blue, LOW);
    digitalWrite(green, LOW);
    digitalWrite(red, LOW);
  }
}
