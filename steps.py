

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []

for i in range(len(days)):
    current_day = days[i]
    steps.append(input(f"How many steps did you take on {current_day}? "))

total_steps = int(steps[0]) + int(steps[1]) + int(steps[2]) + \
    int(steps[3]) + int(steps[4]) + int(steps[5]) + int(steps[6])
average_steps = round(total_steps / len(steps))

print(f"\nYou took {steps[0]} steps on {days[0]}")
print(f"You took {steps[1]} steps on {days[1]}")
print(f"You took {steps[2]} steps on {days[2]}")
print(f"You took {steps[3]} steps on {days[3]}")
print(f"You took {steps[4]} steps on {days[4]}")
print(f"You took {steps[5]} steps on {days[5]}")
print(f"You took {steps[6]} steps on {days[6]}")
print(f"\nTotal steps: {total_steps}")
print(f"Average steps: {average_steps}")
