import random
Subject=[
    "Sahil",
    "Rohit",
    "Virat",
    "Cow",
    "Monkeys",
    "Modi",
    "Auto driver from delhi"
]

Actions =[
    "Launches",
    "Playing",
    "Speech",
    "Driving",
    "Dances with",
    "Cancels",
    "declars war on"
]

Places=[
    "at red Fort",
    "in odisha",
    "inside home",
    "in road",
    "temple"
]

while True:
    Subjects=random.choice(Subject)
    Action=random.choice(Actions)
    place=random.choice(Places)

    headline=f" Breaking news: {Subjects} {Action} {place} "
    print("\n" + headline)

    while True:  # ✅ Validate input
        ans = input("\nYou wanna try something new breaking news? (yes/no): ").strip().lower()
        if ans in ["yes", "no"]:
            break
        else:
            print("❌ Invalid input! Please type only 'yes' or 'no'.")

    if ans == "no":
        print("✅ Thank you for trying this, Have Fun!")
        break
    
   


