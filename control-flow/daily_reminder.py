task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

reminder = ""

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low": 
        reminder = f"'{task}' is a low priority task."
    case _:
        print("Invalid priority level. Please choose from high, medium, or low.") 

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    print("Invalid input for time-bound. Please enter 'yes' or 'no'.")    

print(f"Reminder: {reminder}")