import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1 : ("┌─────────┐", 
         "│         │", 
         "│   ●     │", 
         "│         │", 
         "└─────────┘"),
    2 : ("┌─────────┐", 
         "│         │", 
         "│  ●   ●  │", 
         "│         │", 
         "└─────────┘"),
    3 : ("┌─────────┐", 
         "│         │", 
         "│ ●  ●  ● │", 
         "│         │", 
         "└─────────┘"),
    4 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│         │", 
         "│  ●   ●  │", 
         "└─────────┘"),
    5 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│    ●    │", 
         "│  ●   ●  │", 
         "└─────────┘"),
    6 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│  ●   ●  │", 
         "│  ●   ●  │", 
         "└─────────┘"),
        
}

dice = []
total = 0

num_of_dice = int(input("How many Dices do you want to roll:"))

for d in range(num_of_dice):
    dice.append(random.randint(1, 6))


for d in range(num_of_dice):
    for line in dice_art.get(dice[d]):
        print(line)

for d in dice:
    total += d
print(f"total:{total}")