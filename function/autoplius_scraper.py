from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
from random import randint


class autoplius_scraper:
    """
    This class scrapes car sale adverts from en.autopolius.lt website using BeautifulSoup package. It then
    extracts information about marque, manufacturing date, price (in €) as well as technical details:
    engine (in l), types of vehicle, fuel and gearbox, engine power (in kW) and mileage (in km).
    Data is returned in pandas DataFrame format and then is exported to autoplius.csv file in the repository.
    """

    def __init__(self):
        self.__page_no = 0
        self.__soup = None
        self.__cars = None
        (
            self.__marques,
            self.__engines,
            self.__carTypes,
            self.__years,
            self.__fuels,
            self.__gearboxes,
            self.__powers,
            self.__mileages,
            self.__prices,
        ) = ([] for i in range(9))
        self.__result = None

    def getPageNo(self, sample_size: int) -> int:
        """
        Returns the number of en.autoplius.lt pages that will be scraped to acquire the data of sample_size.

        Parameters:
            * sample_size(int): the number of samples that the user wants to receive after scraping the website.

        Returns:
            * page_no(int): the number of webpage scraping iterations. The reported value becomes an attribute of init method.
        """
        page_no = len(range(0, sample_size, 20))
        self.__page_no = page_no
        return page_no

    def scrape_page(self, URL: str) -> BeautifulSoup:
        """
        Scrapes the given URL address and returns a soup object.

        Parameters:
            * URL(str): website address which will be scraped.

        Returns:
            * soup(BeautifulSoup): BeautifulSoup object, which contains html code. The object becomes an attribute of init method.
        """
        print(f"Start scraping {URL}")
        page = requests.get(
            URL,
            headers=(
                {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                    "Accept-Language": "en-US, en;q=0.5",
                }
            ),
        )
        soup = BeautifulSoup(page.content, "html.parser")
        self.__soup = soup
        print(f"Website scraping finished!")
        return soup

    def find_announcements(self) -> BeautifulSoup:
        """
        Takes the soup object from init method and finds all ads with cars on sale.

        Parameters:
            * None

        Returns:
            * cars(BeautifulSoup): a BeautifulSoup object with all car sale ads. The object becomes an attribute of init method.
        """
        soup = self.__soup
        cars = soup.find_all("a", class_="announcement-item")
        self.__cars = cars
        return cars

    def scrape_marques(self) -> list:
        """
        Takes cars soup instance from init method, extracts car marques from every advertisement in it and merges the list with self.__marques init method.

        Parameters:
            * None

        Returns:
            * marques(list): a list of car marques. The object is appended to an instance of class.
        """
        cars = self.__cars
        marques = []
        for car in cars:
            try:
                marque = (
                    car.find("div", class_="announcement-title")
                    .text.strip()
                    .split(",")[0]
                )
            except:
                marque = None
            marques.append(marque)
        self.__marques = [*self.__marques, *marques]
        return marques

    def scrape_engines(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about engine size (in liters) from every advertisement in it and merges the list with self.__engines init method.

        Parameters:
            * None

        Returns:
            * engines(list): a list of engines from car adverts. The object is appended to an instance of class
        """
        cars = self.__cars
        engines = []
        for car in cars:
            try:
                engine = (
                    car.find("div", class_="announcement-title")
                    .text.strip()
                    .split(",")[1]
                    .split()[0]
                )
            except:
                engine = None
            engines.append(engine)
        self.__engines = [*self.__engines, *engines]
        return engines

    def scrape_carTypes(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about car type from every advertisement and merges the list with self.__carTypes init method.

        Parameters:
            * None

        Returns:
            * carTypes(list): a list of car types from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        carTypes = []
        for car in cars:
            try:
                carType = car.find("div", class_="announcement-title").text.split(",")[
                    -1
                ]
            except:
                carType = None
            carTypes.append(carType)
        self.__carTypes = [*self.__carTypes, *carTypes]
        return carTypes

    def scrape_years(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about car manufacturing date from every advertisement and merges the list with self.__years init method.

        Parameters:
            * None

        Returns:
            * years(list): a list of car manufacturing dates from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        years = []
        for car in cars:
            try:
                year = (
                    car.find("span", attrs={"title": "Date of manufacture"})
                    .text.strip()
                    .split("-")[0]
                )
            except:
                year = None
            years.append(year)
        self.__years = [*self.__years, *years]
        return years

    def scrape_fuels(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about the type of fuel used in car from every advertisement and merges the list with self.__fuels init method.

        Parameters:
            * None

        Returns:
            * fuels(list): a list of types of fuel used in each car from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        fuels = []
        for car in cars:
            try:
                fuel = car.find("span", attrs={"title": "Fuel type"}).text.strip()
            except:
                fuel = None
            fuels.append(fuel)
        self.__fuels = [*self.__fuels, *fuels]
        return fuels

    def scrape_gearboxes(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about car's gearbox type from every advertisement and merges the list with self.__gearboxes init method.

        Parameters:
            * None

        Returns:
            * gearboxes(list): a list of car gearboxes from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        gearboxes = []
        for car in cars:
            try:
                gearbox = car.find("span", attrs={"title": "Gearbox"}).text.strip()
            except:
                gearbox = None
            gearboxes.append(gearbox)
        self.__gearboxes = [*self.__gearboxes, *gearboxes]
        return gearboxes

    def scrape_powers(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about car's engine power (in kW) from every advertisement and merges the list with self.__powers init method.

        Parameters:
            * None

        Returns:
            * powers(list): a list with engine power from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        powers = []
        for car in cars:
            try:
                power = (
                    car.find("span", attrs={"title": "Power"}).text.strip().split()[0]
                )
            except:
                power = None
            powers.append(power)
        self.__powers = [*self.__powers, *powers]
        return powers

    def scrape_mileages(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about car's mileage (in km) from every advertisement and merges the list with self.__mileages init method.

        Parameters:
            * None

        Returns:
            * mileages(list): a list of mileages from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        mileages = []
        for car in cars:
            try:
                mileage = (
                    car.find("span", attrs={"title": "Mileage"})
                    .text.replace(" km", "")
                    .replace(" ", "")
                    .strip()
                )
            except:
                mileage = None
            mileages.append(mileage)
        self.__mileages = [*self.__mileages, *mileages]
        return mileages

    def scrape_prices(self) -> list:
        """
        Takes cars soup instance from init method, extracts information about car's price (in euros) from every advertisement and merges the list with self.__prices init method.

        Parameters:
            * None

        Returns:
            * mileages(list): a list of prices from car adverts. The object is appended to an instance of class.
        """
        cars = self.__cars
        prices = []
        for car in cars:
            try:
                price = (
                    car.find("div", attrs={"class": "announcement-pricing-info"})
                    .text.strip()
                    .replace(" €", "")
                    .replace(" ", "")
                    .split()[0]
                )
            except:
                price = None
            prices.append(price)
        self.__prices = [*self.__prices, *prices]
        return prices

    def into_pandas(self) -> pd.DataFrame:
        """
        Takes lists of car attributes (marque, car type, type of fuel and gearbox, manufacturing date, size of engines, engine power, mileage and price)
        from class init method and inserts them into a single pandas DataFrame.

        Parameters:
            * The following init methods:
                self.__marques,
                self.__engines,
                self.__carTypes,
                self.__years,
                self.__fuels,
                self.__gearboxes,
                self.__powers,
                self.__mileages,
                self.__prices

        Returns:
            * results(pd.DataFrame): a dataframe with car attributes scraped from ads in en.autoplius.lt.
        """
        result = pd.DataFrame(
            {
                "Marque": self.__marques,
                "CarType": self.__carTypes,
                "FuelType": self.__fuels,
                "Gearbox": self.__gearboxes,
                "ManufacturingDate": self.__years,
                "Engine_l": self.__engines,
                "Power_kW": self.__powers,
                "Mileage_km": self.__mileages,
                "Price_euro": self.__prices,
            }
        )
        self.__result = result
        return result

    def into_csv(self) -> str:
        """
        Takes pandas dataframe from results object in init method and exports it to .csv file format in repository.

        Parameters:
            * self.__result(pd.DataFrame) object

        Returns:
            * autoplius.csv: a .csv table with car attributes scraped from ads in en.autoplius.lt;
            * informational message about successfully exported dataframe to .csv table.
        """
        result = self.__result
        result.to_csv("autoplius.csv", index=False)

        return "Pandas dataframe has been successfully exported to the directory as autoplius.csv"

    def multiple_scrapes(self, sample_size: int):
        """
        Collects the required number of car attributes by scraping en.autoplius.lt website. Firstly, the requested sample size is converted
        into the number of website pages to be scraped. Then, for each iteration the website is scraped using scrape_page() and
        find_announcements() methods as well as information about car attributes is collected. Finally, the information is stored in init method objects.
        After each scraped webpage, the function sleeps for an interval of 2 to 10 seconds.

        Parameters:
            * sample_size(int): the required number of car attributes

        Returns:
            * The following init methods:
                self.__marques,
                self.__engines,
                self.__carTypes,
                self.__years,
                self.__fuels,
                self.__gearboxes,
                self.__powers,
                self.__mileages,
                self.__prices
        """

        self.getPageNo(sample_size)
        for i in range(1, self.__page_no + 1):
            URL = f"https://en.autoplius.lt/ads/used-cars?page_nr={i}"
            self.scrape_page(URL)
            self.find_announcements()
            self.scrape_marques()
            self.scrape_engines()
            self.scrape_carTypes()
            self.scrape_years()
            self.scrape_fuels()
            self.scrape_gearboxes()
            self.scrape_powers()
            self.scrape_mileages()
            self.scrape_prices()
            sleep(randint(2, 10))
            print(f"Iteration {i} completed")
        print("Scraping completed")
