import os
import random
import time
import sys

# Setup bright interface text colors
CYAN = "\x1b[36m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
WHITE = "\x1b[37;1m"
RESET = "\x1b[0m"

# Global statistics
affection = 40
hunger = 50

# Text-art frames for the cat
CAT_NORMAL = """
   /\\_/\\
  ( o.o )
   > ^ <
  /     \\
 (_______)┘
"""

CAT_HAPPY = """
   /\\_/\\   * ✨ *
  ( =^.^= )  * 
   > 🐾 <   🎵 Purr...
  /     \\
 (_______)┘
"""

def clear_frame():
    os.system("clear")
    print(f"{CYAN}==================================================")
    print("         PET EMULATOR V1.0 // THE CAT APP         ")
    print(f"=================================================={RESET}")

def main():
    global affection, hunger
    current_status = "The cat is sitting gracefully, blinking slowly at you."
    active_frame = CAT_NORMAL

    while True:
        clear_frame()
        
        # Keep stats between 0 and 100
        affection = max(0, min(100, affection))
        hunger = max(0, min(100, hunger))

        # Print layout graphics and statistics gauges
        print(active_frame)
        print(f"💖 Affection: [{GREEN}{'█' * (affection // 10)}{'░' * (10 - affection // 10)}{RESET}] {affection}%")
        print(f"🍖 Hunger Saturation: [{YELLOW}{'█' * (hunger // 10)}{'░' * (10 - hunger // 10)}{RESET}] {hunger}%\n")
        print(f"💬 STATUS: {WHITE}{current_status}{RESET}\n")
        
        # Menu Dashboard
        print("  1: Pet the cat")
        print("  2: Give Treat")
        print("  3: Feed cat")
        print(f"\n  [{CYAN}Q{RESET}] Safely put the cat to bed / Exit")
        
        choice = input(f"\n{CYAN}SELECT ACTION (1-3): {RESET}").strip()

        if choice == "1":
            # Cats are picky! 25% chance they don't want pets
            if random.random() < 0.25:
                affection -= 10
                current_status = " ⚡ Swipe! The cat swat your hand away. Too many pets!"
                active_frame = CAT_NORMAL
            else:
                affection += 15
                current_status = " Purrrrr... The cat leans into your hand and closes its eyes."
                active_frame = CAT_HAPPY
            time.sleep(0.5)
            
        elif choice == "2":
            if hunger >= 90:
                current_status = " The cat turns its nose up at the treat. Completely uninterested."
                active_frame = CAT_NORMAL
            else:
                affection += 10
                hunger += 15
                current_status = " Crunch crunch. It neatly eats the treat and licks its paws."
                active_frame = CAT_HAPPY
                time.sleep(0.5)
                
        elif choice == "3":
            if hunger >= 100:
                current_status = " The bowl is full, but the cat ignores it and stares out the window."
                active_frame = CAT_NORMAL
            else:
                hunger += 35
                affection += 5
                current_status = " Nom nom nom. The food bowl is completely cleared."
                active_frame = CAT_NORMAL
                
        elif choice.upper() == "Q":
            break
        else:
            current_status = "⚠️ Invalid action code. The cat twitches its ears in judgment."
            active_frame = CAT_NORMAL

        # Small background tick: cat gets hungrier over time
        if random.random() < 0.35:
            hunger -= 5
            
    clear_frame()
    print(f"\n{YELLOW}💤 The cat curled up into a perfect loaf and fell asleep.{RESET}")
    print(f"{CYAN}Thank you for playing the cat simulation engine! Goodbye!{RESET}\n")

if __name__ == "__main__":
    main()
