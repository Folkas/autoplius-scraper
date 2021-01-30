from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import pandas as pd
from time import sleep
from random import randint

def autoplius_scraper(sample_size: int) -> pd.DataFrame:
  """
  The function scrapes car sale adverts from en.autoplius.lt and using BeautifulSoup package extracts information about car marque, manufacturing date, price (in €) as well as technical details:
  engine (in l), types of vehicle, fuel and gearbox, engine power (in kW) and mileage (in km). Data is returned in pandas DataFrame format and then is exported to autoplius.csv file in the repository.

  Parameters:
    * sample_size(int): number of car adverts to be extracted after the scraping
  
  Returns:
    * pd.DataFrame with details about cars on sale (marque, manufacturing date, price, engine, vehicle, fuel, gearbox, power and mileage)
    * pd.DataFrame is exported to autoplius.csv file in the repository
  """
  
  #calculating the number of website scraping iterations
  page_no = len(range(0, sample_size, 20))

  for i in range(1, page_no + 1):

    URL =f"https://en.autoplius.lt/ads/used-cars?page_nr={i}"
    page = requests.get(URL, headers=(
                    {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                        "Accept-Language": "en-US, en;q=0.5"
                    }
                ))
    soup = BeautifulSoup(page.content, "html.parser")

    marques, engines, carTypes, years, fuels, gearboxes, powers, mileages, prices = ([] for i in range(9))

    cars = soup.find_all("a", class_="announcement-item")

    for car in cars:

      #extracting info about car marque
      marque = car.find("div", class_="announcement-title").text.strip().split(",")[0]
      marques.append(marque)

      #car engine
      engine = car.find("div", class_="announcement-title").text.strip().split(",")[1].split()[0]
      engines.append(engine)

      #vehicle type
      carType= car.find("div", class_="announcement-title").text.strip().split(",")[2].replace(" ", "")  
      carTypes.append(carType)

      #date of manufacturing
      year= car.find("span", attrs={'title' : 'Date of manufacture'}).text.strip().split("-")[0]
      years.append(year)

      #fuel type
      fuel= car.find("span", attrs={'title' : 'Fuel type'}).text.strip()
      fuels.append(fuel)

      #gearbox
      gearbox = car.find("span", attrs={'title' : 'Gearbox'}).text.strip()
      gearboxes.append(gearbox)

      #engine power
      power = car.find("span", attrs={'title' : 'Power'}).text.strip().split()[0]
      powers.append(int(power))

      #mileage
      mileage = car.find("span", attrs={'title' : 'Mileage'}).text.replace(" km", "").replace(" ", "").strip()
      mileages.append(int(mileage))

      #price
      price = car.find("div", attrs={'class' : 'announcement-pricing-info'}).text.strip().replace(" €","").replace(" ","").split()[0]
      prices.append(int(price))

      #controlling the execution of scraping by pausing the looping rate
      sleep(randint(2,10))
    
  #inserting lists into pandas DataFrame
  result=pd.DataFrame({
      "Marque": marques,
      "CarType": carTypes,
      "FuelType": fuels,
      "Gearbox": gearboxes,
      "ManufacturingDate": years,
      "Engine_l": engines,
      "Power_kW": powers,
      "Mileage_km": mileages,
      "Price_€": prices
  })
  
  #exporting the dataframe to .csv file
  result.to_csv('autoplius.csv', index=False)

  return result

