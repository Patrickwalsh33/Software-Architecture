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

total_hours = 0

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
            total_hours += duration_hours

            

print(f"Total EVA hours for selected country is: {total_hours}")
    
    

plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
