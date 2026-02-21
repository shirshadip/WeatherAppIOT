#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("DHT11 sensor initialized");
}

void loop() {
  float humidity = dht.readHumidity();
  float temperatureC = dht.readTemperature();
  float temperatureF = dht.readTemperature(true);

  if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
    Serial.println("Sensor error");
    delay(2000);
    return;
  }

  Serial.print("TemperatureC:");
  Serial.print(temperatureC, 1);
  Serial.print(" | TemperatureF:");
  Serial.print(temperatureF, 1);
  Serial.print(" | Humidity:");
  Serial.print(humidity, 1);
  Serial.println("%");

  delay(2000);
}
