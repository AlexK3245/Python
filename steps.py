""" This program will ask the user how many steps they took each day, then it will calculate the total
    amount of steps and the average amount and print it"""

# Assignment

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
total = 0

for i in range(len(days)):
    current_day = days[i]
    steps.append(input(f"How many steps did you take on {current_day}? "))
    total += int(steps[i])

average_steps = round(total / len(steps))

print(f"\nYou took {steps[0]} steps on {days[0]}")
print(f"You took {steps[1]} steps on {days[1]}")
print(f"You took {steps[2]} steps on {days[2]}")
print(f"You took {steps[3]} steps on {days[3]}")
print(f"You took {steps[4]} steps on {days[4]}")
print(f"You took {steps[5]} steps on {days[5]}")
print(f"You took {steps[6]} steps on {days[6]}")
print(f"\nTotal steps: {total}")
print(f"Average steps: {average_steps}")
