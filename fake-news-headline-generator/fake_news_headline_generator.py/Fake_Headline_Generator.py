# import random module
import random

# ---------------- FUNNY DATA ----------------
funny_subjects = [
    "Mr. Modi",
    "The sun",
    "The dog",
    "My house",
    "My shirt",
    "A. P. J. Abdul Kalam",
    "Children",
    "Every leader",
    "The group of Monkey "
    "My Teacher"
]

funny_actions = [
    "is dancing",
    "is cooking",
    "is crying",
    "is swimming",
    "is laughing",
    "is running",
    "is weeping",
    "is reading"
]

funny_places = [
    "on the buffalo",
    "near India Gate",
    "inside parliament",
    "with many plates of momos",
    "without clothes",
    "on the Tree",
    "at river"
]

# ---------------- SERIOUS DATA ----------------
serious_subjects = [
    "The Prime Minister",
    "The government",
    "The market",
    "Students",
    "The police",
    "The company",
    "The school",
    "The country",
    "The America"
]

serious_actions = [
    "announced a new policy",
    "is working on development",
    "remained closed",
    "are preparing for exams",
    "started an investigation",
    "reported growth",
    "attacked",
    "never go"
]

serious_places = [
    "in the parliament",
    "across the country",
    "in the capital",
    "during the meeting",
    "today",
    "on the japan",
    "without india"
]

# ---------------- MODE SELECTION ----------------
mode = input("Choose mode (funny/serious): ").lower()

print("\n--- Fake News Headline Generator ---")

while True:

    if mode == "funny":
        subject = random.choice(funny_subjects)
        action = random.choice(funny_actions)
        place = random.choice(funny_places)

    elif mode == "serious":
        subject = random.choice(serious_subjects)
        action = random.choice(serious_actions)
        place = random.choice(serious_places)

    else:
        print("Invalid mode selected!")
        break

    headline = f"Breaking News: {subject} {action} {place}"
    print("\n " + headline)

    user_input = input("Do you want another headline? (yes/no): ").lower()
    if user_input == "no":
        break

print("\nThanks for using fake news headline generator")
