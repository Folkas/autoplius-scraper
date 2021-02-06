# autoplius-scraper


[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]https://github.com/Folkas/autoplius-scraper/blob/main/LICENSE)

## Table of contents:
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Other](#other)


## General info:
This repository contains a scraping class for en.autoplius.lt website for Turing College module 2 spring 4 final assignment. The class contains methods, which scrape the webpage, extract information about car attributes from ads and return information in pandas DataFrame table or .csv file.

## Setup
To run this project, install it using `pip` command:
```
!pip install git+https://github.com/Folkas/autoplius-scraper.git
```
The scraping functions are located in ```function``` folder ```scraper.py``` file, while the tests are found in ```test``` folder.

## Features
```getPageNo(sample_size:int)```

Returns the number of en.autoplius.lt pages that will be scraped to acquire the data of sample_size.

```scrape_page(URL:str)```

Scrapes the given URL address and returns a soup object.

```find_announcements()```

Takes the soup object from init method and finds all ads with cars on sale.

```scrape_marques()```

Takes cars soup instance from init method, extracts car marques from every advertisement in it and merges the list with self.__marques init method.

```scrape_engines()```

Takes cars soup instance from init method, extracts information about engine size (in liters) from every advertisement in it and merges the list with self.__engines init method.

```scrape_carTypes()```

Takes cars soup instance from init method, extracts information about car type from every advertisement and merges the list with self.__carTypes init method.

```scrape_years()```

Takes cars soup instance from init method, extracts information about car manufacturing date from every advertisement and merges the list with self.__years init method.

```scrape_fuels()```

Takes cars soup instance from init method, extracts information about the type of fuel used in car from every advertisement and merges the list with self.__fuels init method.

```scrape_gearboxes()```

Takes cars soup instance from init method, extracts information about car's gearbox type from every advertisement and merges the list with self.__gearboxes init method.

```scrape_powers()```

Takes cars soup instance from init method, extracts information about car's engine power (in kW) from every advertisement and merges the list with self.__powers init method.

```scrape_mileages()```

Takes cars soup instance from init method, extracts information about car's mileage (in km) from every advertisement and merges the list with self.__mileages init method.

```scrape_prices()```

Takes cars soup instance from init method, extracts information about car's price (in euros) from every advertisement and merges the list with self.__prices init method.

```into_pandas()```

Takes lists of car attributes (marque, car type, type of fuel and gearbox, manufacturing date, size of engines, engine power, mileage and price) from class init method and inserts them into a single pandas DataFrame.

```into_csv()```

Takes pandas dataframe from results object in init method and exports it to .csv file format in repository.

```multiple_scrapes(sample_size:int)```

```sample_size``` refers to the number of samples to be scraped. The method scrapes en.autoplius.lt webpage and extract details about each advert: manufacturing date, price (in €), engine (in l), types of vehicle, fuel and gearbox, engine power (in kW) and mileage (in km). 
Firstly, the requested sample size is converted into the number of website pages to be scraped with ```getPageNo()``` method. Then, for each iteration the website is scraped using ```scrape_page()``` and ```find_announcements()``` methods as well as information about car attributes is collected. Finally, the information is stored in init method objects. After each scraped webpage, the function sleeps for an interval of 2 to 10 seconds.

## Other
The ```old_scraper.py``` in ```function``` folder has an old function, which alone performs all operations as the ```autoplius_scraper``` class.
