# Simple Reflex - AQI AGENT
This project implements a simple reflex agent that determines the AQI (Air Quality Index) for a different location using sensor data from the environment. 

The agent reads the pollutant concentration from the sensor_data CSV file, calculates the AQI, and outputs the AQI value and air quality category for each location

As this is a simple reflex agent, it only reacts when there is input from the current sensor, without storing the past information


# Input
Reads pollution data from a file called: sensor_data.csv

## Example format
location      ,PM2.5,PM10,NO2,SO2,CO,O3 

Gandi Maisamma,40   ,55  ,30 ,20 ,1.2,35

Each row represents pollution measurements for a specific location at a given time

# Output
The program calculates the AQI and prints:
Location    AQI value       AQI Category 
## Example output
<img width="651" height="89" alt="image" src="https://github.com/user-attachments/assets/fca50e14-2f42-4fc3-beb2-4f449f0a4757" />

# AQI Categories
<img width="225" height="278" alt="image" src="https://github.com/user-attachments/assets/ce900570-b46f-403a-b8c0-e4211ebf4df5" />

# Running the program
  python aqi_agent.py
  
Needs Python 3 and the pandas library

## Authors
Done as a team
1. Abhinav Santosh - SE24UCSE022
2. Ega Kesari Charan - SE24UCSE162
4. Muhammad Muzaffar Shaik - SE24UCSE252
5. Sai Jeevan - SE24UCSE236

