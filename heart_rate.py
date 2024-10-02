# Tracking heart rate throughout the day

total = 0
average = 0

time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
for time in time_slots:
    bpm = input(f"Enter your heart rate (in BPM) in the {time}: ")
    heart_rates.append([time, bpm])

# print(heart_rates)
for i in range(4):
    bpm = heart_rates[i][1]
    total += int(bpm)

average = total/4
print(f"Your average heart rate today was: {average:.2f}")
