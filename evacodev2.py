import json
from datetime import datetime
import matplotlib.pyplot as plt

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")

    if not date_text or not duration_text:
        continue

    date = datetime.fromisoformat(date_text)
    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    records.append((date, duration_hours))

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

for date, duration_hours in records:
    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)

total_hours_per_country = 0

#loop that allows you to set a country value and the total cumulative EVA hours for that country will be printed to the terminal
#Pretty clunky to be hardcoding the country value, implementation should be improved
#hours + minutes -> hours conversion is also duplicated from lines 18-19, could probably be moved into its own function
for eva in eva_data:
        
        duration_text = eva.get("duration")
        if not duration_text:
            continue

        if eva.get("country") == "Russia":
            hours, minutes = map(int, duration_text.split(":"))
            duration_hours = hours + minutes / 60
            total_hours_per_country += duration_hours

            

print(f"Total EVA hours for selected country is: {total_hours_per_country}")
    
#adding functionality for user to input year and program to output the number of EVAs in that year and their total duration in hours

selected_year = input("Enter a year: ")

total_eva_in_year = 0
total_hours_per_year = 0

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")

    if not date_text or not duration_text:
        continue

    if date_text[:4] != selected_year:
        continue

    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    total_eva_in_year += 1
    total_hours_per_year += duration_hours

print(f"Total EVAs in {selected_year} was: {total_eva_in_year}")
print(f"Total duration of EVAs in {selected_year} was: {total_hours_per_year}")




#original graph of cumulative EVA hours over years
plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
