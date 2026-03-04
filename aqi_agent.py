import pandas as pd
# aqi breakpoints format = (low concentration, high concentration, low aqi index, high aqi index)
aqi_breakpoints = { 
    "PM2.5": [(0, 12, 0, 50), (12.1, 35.4, 51, 100), (35.5, 55.4, 101, 150), (55.5, 150.4, 151, 200)],
    "PM10":  [(0, 54, 0, 50), (55, 154, 51, 100), (155, 254, 101, 150), (255, 354, 151, 200)],
    "NO2":   [(0, 53, 0, 50), (54, 100, 51, 100), (101, 360, 101, 150)],
    "SO2":   [(0, 35, 0, 50), (36, 75, 51, 100), (76, 185, 101, 150)],
    "CO":    [(0.0, 4.4, 0, 50), (4.5, 9.4, 51, 100), (9.5, 12.4, 101, 150)],
    "O3":    [(0, 54, 0, 50), (55, 70, 51, 100), (71, 85, 101, 150)]
}

df = pd.read_csv("sensor_data.csv")
output = []

for idx, row in df.iterrows():
    individual_aqi = {}
    # Calculating
    for pollutant in aqi_breakpoints:
        concentration = row[pollutant]
        breakpoints = aqi_breakpoints[pollutant]
        aqi_value = None
        for C_low, C_high, AQI_low, AQI_high in breakpoints:
            if C_low <= concentration <= C_high:
                aqi_value = ((AQI_high - AQI_low) / (C_high - C_low)) * (concentration - C_low) + AQI_low
                break
        if aqi_value is not None:
            individual_aqi[pollutant] = aqi_value
    # Final AQI
    if individual_aqi:
        final_aqi = max(individual_aqi.values())
        if final_aqi <= 50:
            category = "Good"
        elif final_aqi <= 100:
            category = "Moderate"
        elif final_aqi <= 150:
            category = "Unhealthy for Sensitive Groups"
        elif final_aqi <= 200:
            category = "Unhealthy"
        elif final_aqi <= 300:
            category = "Very Unhealthy"
        else:
            category = "Hazardous"
    else:
        final_aqi = None
        category = "Insufficient Data"
    result_row = {
        "location": row["location"],
        "AQI": round(final_aqi, 1)
            if final_aqi 
            else None,
        "Category": category
    }

    output.append(result_row)
results = pd.DataFrame(output)
print(results)