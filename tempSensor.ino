#define REFRESH_RATE 1

void setup() {
  Serial.begin(9600);
  Serial.print("Time (s),Temperature Reading (C)\n"); // using newlines because println sends carriage returns and newlines
}

void loop() {
  static int timeVal;
  static float temperatureValue;
  
  // Read temperature sensor
  temperatureValue = .48828125 * analogRead(0) - 50; // Convert analog voltage to temperature as specified by manufacturer

  // Log temperature, power setting for csv
  Serial.print(String(timeVal) + "," + String(temperatureValue) + "\n");

  // Pause until next evaluation time
  delay(1000 / REFRESH_RATE);
  timeVal += REFRESH_RATE;
}
