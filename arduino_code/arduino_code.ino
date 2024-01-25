//Déclaration des librairies
#include <BME280I2C.h>
#include <Wire.h>

//Déclaration de la fréquence de transmission des données
#define SERIAL_BAUD 115200

BME280I2C bme;    // Default : forced mode, standby time = 1000 ms
                  // Oversampling = pressure ×1, temperature ×1, humidity ×1, filter off,

//Connexion a la carte: détéction d'une potentielle carte et récupération du modèle précis
void setup()
{
  Serial.begin(SERIAL_BAUD);

  while(!Serial) {} // Wait

  Wire.begin();

  while(!bme.begin())
  {
    Serial.println("Could not find BME280 sensor!");
    delay(1000);
  }

  //détéction pour déterminer si c'est un module BME280(temp,hum,press) ou BMP280(temp,press)
  switch(bme.chipModel())
  {
     case BME280::ChipModel_BME280:
       Serial.println("Found BME280 sensor! Success.");
       break;
     case BME280::ChipModel_BMP280:
       Serial.println("Found BMP280 sensor! No Humidity available.");
       break;
     default:
       Serial.println("Found UNKNOWN sensor! Error!");
  }
}

void loop()
{
   //Appel de la fonction printBME280Data
   printBME280Data(&Serial);
   
   //Délais pour faire le relevé toutes les minutes
   delay(60000);
}

//Fonction printBME280Data
void printBME280Data
(
   Stream* client
)
{
   float temp(NAN), hum(NAN), pres(NAN);
   
   //Définition des Unitées de mesure
   BME280::TempUnit tempUnit(BME280::TempUnit_Celsius);
   BME280::PresUnit presUnit(BME280::PresUnit_Pa);
   
   //Lecture des données envoyées par le BME280
   bme.read(pres, temp, hum, tempUnit, presUnit);

   //Mise en forme pour l'envois vers l'API
   client->print(temp);
   client->print("/");
   client->print(hum);
   client->print("/");
   client->println(pres);

   delay(1000);
}
