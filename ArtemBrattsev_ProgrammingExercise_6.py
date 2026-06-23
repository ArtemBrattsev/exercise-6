# Name: Artem Brattsev
# Course: COP 2373
# Programming Exercise 6 - Regular Expressions

import re


# Validates user input using regular expressions
class Validator:

    # validates phone number.
    def validate_phone(self, phone):

        pattern = r"^\d{3}-\d{3}-\d{4}$" 

        return re.match(pattern, phone)

    # validates a social security number
    def validate_ssn(self, ssn):

        pattern = r"^\d{3}-\d{2}-\d{4}$"

        return re.match(pattern, ssn)

    # Validates zip code
    def validate_zip(self, zip_code):

        pattern = r"^\d{5}$"

        return re.match(pattern, zip_code)


# Main function
def main():

    validator = Validator()

    phone = input("Enter a phone number (###-###-####): ")
    ssn = input("Enter a social security number (###-##-####): ")
    zip_code = input("Enter a zip code (#####): ")

    print() # prints out if user entered values right or wrong relatively to instructions

    if validator.validate_phone(phone):
        print("Phone Number: Valid")
    else:
        print("Phone Number: Invalid")

    if validator.validate_ssn(ssn):
        print("Social Security Number: Valid")
    else:
        print("Social Security Number: Invalid")

    if validator.validate_zip(zip_code):
        print("Zip Code: Valid")
    else:
        print("Zip Code: Invalid")


main()
