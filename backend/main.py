# main.py
import random

# Sample user profiles
profiles = [
    {"name": "Alice", "age": 24, "bio": "Loves hiking and coffee ☕"},
    {"name": "Brian", "age": 27, "bio": "Tech nerd & foodie 🍔"},
    {"name": "Cynthia", "age": 22, "bio": "Dancer 💃 and traveler 🌍"},
    {"name": "David", "age": 29, "bio": "Gamer 🎮 and music lover 🎵"},
    {"name": "Ella", "age": 25, "bio": "Photographer 📸, nature lover 🌿"},
]

# Simulate your account
current_user = {"name": "You", "age": 23, "bio": "Just testing this Tinder-like app 😎"}

# Store your likes and matches
your_likes = []
matches = []

def show_profile(profile):
    """Display a user profile"""
    print("\n--- Profile ---")
    print(f"Name: {profile['name']}, Age: {profile['age']}")
    print(f"Bio: {profile['bio']}")
    print("Press [l] to Like, [p] to Pass, [q] to Quit")

def simulate_other_like():
    """Random chance the other person likes you back"""
    return random.choice([True, False])

def tinder_app():
    print("🔥 Welcome to PyTinder 🔥")
    for profile in profiles:
        show_profile(profile)
        choice = input("Your choice: ").lower()

        if choice == "l":
            your_likes.append(profile["name"])
            if simulate_other_like():
                matches.append(profile["name"])
                print(f"💖 It's a match with {profile['name']}!")
            else:
                print(f"👉 You liked {profile['name']} but no match.")
        elif choice == "p":
            print(f"❌ You passed on {profile['name']}")
        elif choice == "q":
            break
        else:
            print("⚠️ Invalid choice, skipping...")

    print("\n=== Session Ended ===")
    print(f"Your likes: {your_likes}")
    print(f"Your matches: {matches}")

if __name__ == "__main__":
    tinder_app()

