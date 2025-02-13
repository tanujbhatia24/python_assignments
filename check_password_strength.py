import re

# Giving a heads up to the user about the Password criteria
print("## Password must meet the following criteria: ##")
print(" - At least 8 characters long")
print(" - Contains at least one uppercase letter")
print(" - Contains at least one lowercase letter")
print(" - Contains at least one digit (0-9)")
print(" - Contains at least one special character from the list [!, @, #, $, %]")


# Creating the function
def check_password_strength(password):
    try:
        
        # Creating an empty list to store the missing criteria in the entered Password
        missing_criteria = []

        # Checking for minimum length criteria in the entered Password
        if len(password) < 8:
            missing_criteria.append("Password must be at least 8 characters long.")
        
        # Checking for Uppercase letters criteria in the entered Password
        if not re.search(r"[A-Z]", password):
            missing_criteria.append("Password must contain at least one uppercase letter.")

        # Checking for Lowercase letter criteria in the entered Password       
        if not re.search(r"[a-z]", password):
            missing_criteria.append("Password must contain at least one lowercase letter.")
        
        # Checking for a Digit criteria in the entered Password
        if not re.search(r"[0-9]", password):
            missing_criteria.append("Password must contain at least one digit (0-9).")
        
        # Checking for a Special Character criteria in the entered Password
        if not re.search(r"[!@#$%]", password):
            missing_criteria.append("Password must contain at least one special character from the list [!, @, #, $, %].")

        # Providing feedback to the user if any criteria is missing from the entered Password    
        if missing_criteria:
            print("Weak: Password is missing the following criteria:")
            for criteria in missing_criteria:
                print(f" - {criteria}")
            return False
        
        print("Strong: Password meets all criteria.")
        return True
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Creating main logic, so that function/code should be available for import and reuse in other programs.
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    try:
        print(check_password_strength(str(password)))
    except Exception as e:
        print(f"An error occurred in the main program: {e}")
