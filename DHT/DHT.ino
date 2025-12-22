#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperatureC = dht.readTemperature();   // Celsius
  float temperatureF = dht.readTemperature(true); // Fahrenheit

  if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
    Serial.println("Sensor error");
    delay(2000);
    return;
  }

  // 🔹 CONSISTENT FORMAT (important for Flask parsing)
  Serial.print("TemperatureC:");
  Serial.print(temperatureC);
  Serial.print(" | TemperatureF:");
  Serial.print(temperatureF);
  Serial.print(" | Humidity:");
  Serial.print(humidity);
  Serial.println("%");

  delay(2000);
}
