from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days_to_add = int(input("Enter number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days = days_to_add)   
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()     