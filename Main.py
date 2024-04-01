from dateutil import parser
import re

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

def validate_date(input_date):
    # Regex to check if the date is in the format: Month DD, YYYY
    if re.match(r"^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}$", input_date):
        return True
    # Regex to check if the date is in the format: MM/DD/YYYY
    elif re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", input_date):
        return True
    return False

def convert_date(input_date):
    try:
        parsed_date = parser.parse(input_date)
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError:
        return None

def main():
    while True:
        user_input = input("Please enter a date (MM/DD/YYYY or Month DD, YYYY): ")
        if validate_date(user_input):
            iso_date = convert_date(user_input)
            if iso_date:
                print(f"ISO 8601 Format: {iso_date}")
                break
            else:
                print("Invalid date, please try again.")
        else:
            print("Incorrect format, please try again.")

# Uncomment the following line to run the function in an interactive environment
main()
