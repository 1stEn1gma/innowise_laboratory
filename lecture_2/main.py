import re
from datetime import datetime


def generate_profile(age: int) -> str:
    """ Gets the user's age and returns their life stage """

    if age < 12:
        return "Child"
    elif age < 19:
        return "Teenager"
    else:
        return "Adult"


# get current year
current_year = datetime.now().year

# get user full name
user_name = input("Enter your full name: ")

# get user birth year
correct_user_birth_year = False

while not correct_user_birth_year:
    birth_year_str = input("Enter your birth year: ")

    try:
        # Try to convert birth_year_str to an intiger
        birth_year = int(birth_year_str)

        # Validity check
        if birth_year <= current_year:
            correct_user_birth_year = True
        else:
            print("Incorrect value")
    except ValueError:
        print("Incorrect value")

current_age = current_year - birth_year

# get user birth hobbies
hobbies = []

add_hobby = True

while add_hobby:
    user_answer = input("Enter a favorite hobby or type \'stop\' to finish: ")

    # Validity check
    clean_user_answer = re.sub(r'[^a-zA-Z0-9]', '', user_answer)

    if clean_user_answer != "":
        if user_answer.lower() == "stop":
            add_hobby = False
        else:
            hobbies.append(user_answer)
    else:
        print("Incorrect value")

# get user life stage
life_stage = generate_profile(current_age)

# store user data
user_profile = {
    "name": user_name,
    "age": current_age,
    "life stage": life_stage,
    "hobbies": hobbies
}

# generate user hobbies string
amount_of_user_hobbies = len(user_profile["hobbies"])

hobbies_str = "You didn't mention any hobbies\n"

if amount_of_user_hobbies > 0:
    hobbies_str = f"Favorite Hobbies ({amount_of_user_hobbies}):\n"
    for hobby in user_profile["hobbies"]:
        hobbies_str = hobbies_str + " - " + hobby + "\n"

# display user profile
print(f"\n"
      f"~~~~~~~~~~~~~~~\n"
      f"Profile Summary: \n"
      f"Name: {user_profile["name"]}\n"
      f"Age: {user_profile["age"]}\n"
      f"Life Stage: {user_profile["life stage"]}\n"
      f"{hobbies_str}"
      f"~~~~~~~~~~~~~~~")
