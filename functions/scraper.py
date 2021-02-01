from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
from random import randint

def autoplius_scraper(sample_size: int) -> pd.DataFrame:
  """
  The function scrapes car sale adverts from en.autoplius.lt and using BeautifulSoup 
  package extracts information about car marque, manufacturing date, price (in €) 
  as well as technical details: engine (in l), types of vehicle, fuel and gearbox, 
  engine power (in kW) and mileage (in km). Data is returned in pandas DataFrame 
  format and then is exported to autoplius.csv file in the repository.

  Parameters:
    * sample_size(int): number of car adverts to be extracted after the scraping
  
  Returns:
    * pd.DataFrame with details about cars on sale (marque, manufacturing date, 
    price, engine, vehicle, fuel, gearbox, power and mileage)
    * data is exported to autoplius.csv file in the repository
  """
  
  #calculating the number of website scraping iterations
  page_no = len(range(0, sample_size, 20))
  marques, engines, carTypes, years, fuels, gearboxes, powers, mileages, prices = ([] for i in range(9))

  print("Starting iterating over the webpage..")

  for i in range(1, page_no + 1):
    
    URL =f"https://en.autoplius.lt/ads/used-cars?page_nr={i}"
    page = requests.get(URL, headers=(
                    {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                        "Accept-Language": "en-US, en;q=0.5"
                    }
                ))
    soup = BeautifulSoup(page.content, "html.parser")

    cars = soup.find_all("a", class_="announcement-item")

    #controlling the execution of scraping by pausing the looping rate
    sleep(randint(2,10))

    for car in cars:

      #extracting info about car marque
      try:
        marque = car.find("div", class_="announcement-title").text.strip().split(",")[0]
      except:
        marque = None
      marques.append(marque)

      #car engine
      try:
        engine = car.find("div", class_="announcement-title").text.strip().split(",")[1].split()[0]
      except:
        engine = None
      engines.append(engine)

      #vehicle type
      try:
        carType= car.find("div", class_="announcement-title").text.split(",")[-1]  
      except:
        carType = None
      carTypes.append(carType)

      #date of manufacturing
      try:
        year= car.find("span", attrs={'title' : 'Date of manufacture'}).text.strip().split("-")[0]
      except:
        year = None
      years.append(year)

      #fuel type
      try:
        fuel= car.find("span", attrs={'title' : 'Fuel type'}).text.strip()
      except:
        fuel= None
      fuels.append(fuel)

      #gearbox
      try:
        gearbox = car.find("span", attrs={'title' : 'Gearbox'}).text.strip()
      except:
        gearbox = None
      gearboxes.append(gearbox)

      #engine power
      try:
        power = car.find("span", attrs={'title' : 'Power'}).text.strip().split()[0]
      except:
        power = None
      powers.append(power)

      #mileage
      try:
        mileage = car.find("span", attrs={'title' : 'Mileage'}).text.replace(" km", "").replace(" ", "").strip()
      except:
        mileage = None
      mileages.append(mileage)

      #price
      try:
        price = car.find("div", attrs={'class' : 'announcement-pricing-info'}).text.strip().replace(" €","").replace(" ","").split()[0]
      except:
        price=None
      prices.append(price)

    print(f"Iteration {i} completed")
  
    
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
      "Price_euro": prices
  })
  
  #exporting the dataframe to .csv file
  result.to_csv('autoplius.csv', index=False)

  return result

def autoplius_scraper2(sample_size: int) -> pd.DataFrame:
  """
  This function works the same way as autoplius_scraper. The only difference is that 
  it extracts the Marque variable and splits it into 2 parts: Brand (e.g. BMW, 
  Volkswagen, etc.) and Model (535, Passat, etc.). The final table contains the 
  following columns: Brand, Model, CarType, FuelType, Gearbox, ManufacturingDate, 
  Engine_l, Power_kW, Mileage_km, Price_€. Because this function separates the Marque 
  variable into two, it should be used only when the Marque has no None values.
  
  Parameters:
    * sample_size(int): number of car adverts to be extracted after the scraping
  
  Returns:
    * pd.DataFrame with details about cars on sale (marque, manufacturing date, price, 
    engine, vehicle, fuel, gearbox, power and mileage)
    * data is exported to autoplius.csv file in the repository
  """
  
  #calculating the number of website scraping iterations
  page_no = len(range(0, sample_size, 20))
  marques, engines, carTypes, years, fuels, gearboxes, powers, mileages, prices = ([] for i in range(9))

  print("Starting iterating over the webpage..")

  for i in range(1, page_no + 1):
    
    URL =f"https://en.autoplius.lt/ads/used-cars?page_nr={i}"
    page = requests.get(URL, headers=(
                    {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                        "Accept-Language": "en-US, en;q=0.5"
                    }
                ))
    soup = BeautifulSoup(page.content, "html.parser")

    cars = soup.find_all("a", class_="announcement-item")

    #controlling the execution of scraping by pausing the looping rate
    sleep(randint(2,10))

    for car in cars:

      #extracting info about car marque
      try:
        marque = car.find("div", class_="announcement-title").text.strip().split(",")[0]
      except:
        marque = None
      marques.append(marque)

      #car engine
      try:
        engine = car.find("div", class_="announcement-title").text.strip().split(",")[1].split()[0]
      except:
        engine = None
      engines.append(engine)

      #vehicle type
      try:
        carType= car.find("div", class_="announcement-title").text.split(",")[-1]  
      except:
        carType = None
      carTypes.append(carType)

      #date of manufacturing
      try:
        year= car.find("span", attrs={'title' : 'Date of manufacture'}).text.strip().split("-")[0]
      except:
        year = None
      years.append(year)

      #fuel type
      try:
        fuel= car.find("span", attrs={'title' : 'Fuel type'}).text.strip()
      except:
        fuel= None
      fuels.append(fuel)

      #gearbox
      try:
        gearbox = car.find("span", attrs={'title' : 'Gearbox'}).text.strip()
      except:
        gearbox = None
      gearboxes.append(gearbox)

      #engine power
      try:
        power = car.find("span", attrs={'title' : 'Power'}).text.strip().split()[0]
      except:
        power = None
      powers.append(power)

      #mileage
      try:
        mileage = car.find("span", attrs={'title' : 'Mileage'}).text.replace(" km", "").replace(" ", "").strip()
      except:
        mileage = None
      mileages.append(mileage)

      #price
      try:
        price = car.find("div", attrs={'class' : 'announcement-pricing-info'}).text.strip().replace(" €","").replace(" ","").split()[0]
      except:
        price=None
      prices.append(price)

    print(f"Iteration {i} completed")
  
    
  #inserting lists into pandas DataFrame. Brand and model are extracted from marques variable.
  result=pd.DataFrame({
      "Brand": [val.split()[0] for val in marques],
      "Model": [" ".join(val.split()[1:]) for val in marques],
      "CarType": carTypes,
      "FuelType": fuels,
      "Gearbox": gearboxes,
      "ManufacturingDate": years,
      "Engine_l": engines,
      "Power_kW": powers,
      "Mileage_km": mileages,
      "Price_euro": prices
  })
  #exporting the dataframe to .csv file
  result.to_csv('autoplius_edited.csv', index=False)

  return result
