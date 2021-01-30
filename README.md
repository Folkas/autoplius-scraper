# autoplius-scraper


[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]https://github.com/Folkas/autoplius-scraper/blob/main/LICENSE)

## Table of contents:
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Recommendations](#recommendations)
* [Other](#other)


## General info:
This repository contains two scraping functions for en.autoplius.lt website for Turing College module 2 spring 4 final assignment. Both functions scrape the webpage and return information about cars on sale in a .csv file.

## Setup
To run this project, install it using `pip` command:
```
!pip install git+https://github.com/Folkas/autoplius-scraper.git
```
The scraping functions are located in ```functions``` folder ```scraper.py``` file

## Features
The package provides two functions: ```autoplius_scraper(sample_size: int)``` and ```autoplius_scraper2(sample_size: int)```, where sample_size refers to the number of samples to be scraped. Both functions scrape en.autoplius.lt webpage and extract details about each advert: manufacturing date, price (in €), engine (in l), types of vehicle, fuel and gearbox, engine power (in kW) and mileage (in km). The only difference is that ```autoplius_scraper``` also extracts a column "Marque" with car brand and model (e.g. "Volkswagen Passat"), whereas ```autoplius_scraper2``` returns the "Marque" in two columns: "Brand" (e.g. "Volkswagen") and "Model" (e.g. "Passat"). 

## Recommendations
While in theory both functions return the same information, ```autoplius_scraper2``` should be used only when the user is sure that no None values will be scraped from the website.
