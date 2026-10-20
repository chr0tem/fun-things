import os
import time
import sys

# P Runtime Print Colors
GREEN = "\x1b[32m"
CYAN = "\x1b[36;1m"
YELLOW = "\x1b[33m"
PURPLE = "\x1b[35;1m"
RESET = "\x1b[0m"

# Internal Machine Memory Registers
happiness = 50
hunger = 50
current_state = "INITIALISE"

def clear_view():
    os.system("clear")
    print(f"{PURPLE}[ P-LANGUAGE STATE MACHINE INTERFACE ]{RESET}")
    print("==================================================")

def check_stats():
    global happiness, hunger, current_state
    # Lock memory variables inside safe state boundaries (0-100)
    happiness = max(0, min(100, happiness))
    hunger = max(0, min(100, hunger))
    
    print(f"\n📊 {CYAN}[EVENT: eCheckStats]{RESET}")
    print(f" -> Current Machine State: {YELLOW}{current_state}{RESET}")
    print(f" -> Memory variable 'happiness': {happiness}%")
    print(f" -> Memory variable 'hunger':    {hunger}%")
    
    # State transition checker logic
    if happiness >= 80 and current_state == "SITTING_PATIENTLY":
        current_state = "SUPER_HAPPY_BONUS_MODE"
        print(f"\n🔄 {GREEN}[STATE TRANSITION]: goto SuperHappyBonusMode;{RESET}")
    elif happiness < 80 and current_state == "SUPER_HAPPY_BONUS_MODE":
        current_state = "SITTING_PATIENTLY"
        print(f"\n🔄 {YELLOW}[STATE TRANSITION]: goto SittingPatiently;{RESET}")

def main():
    global happiness, hunger, current_state
    
    clear_view()
    print(f"🎬 {GREEN}[STATE: Initialise -> entry]{RESET}")
    print(" -> print \"Barkley is sitting patiently. System Idle.\"")
    current_state = "SITTING_PATIENTLY"
    time.sleep(2)

    while True:
        clear_view()
        print(f"📍 Active Machine State: {YELLOW}{current_state}{RESET}")
        print("--------------------------------------------------")
        
        if current_state == "SUPER_HAPPY_BONUS_MODE":
            print(f"✨ {GREEN}[STATE: SuperHappyBonusMode -> entry]{RESET}")
            print(" -> print \"SPECIAL STATUS: Barkley is doing zoomies around the room!\"")
        else:
            print(" -> Status: Machine active. Awaiting formal asynchronous event triggers...")

        print("\nTrigger Event Dispatcher Queue:")
        print(f"  1: Send Event -> {CYAN}ePetDog{RESET}")
        print(f"  2: Send Event -> {CYAN}eGiveTreat{RESET}")
        print(f"  3: Send Event -> {CYAN}eFeedDog{RESET}")
        print(f"\n  [{RED_TAG if 'RED_TAG' in locals() else 'x1b[31m'}Q{RESET}] Terminate Machine Runtime")
        
        choice = input("\nDispatch Event Choice (1-3): ").strip()

        if choice == "1":
            print(f"\n📥 {CYAN}[EVENT DISPATCHED: ePetDog]{RESET}")
            happiness += 15
            hunger -= 5
            print(" -> execution: happiness = happiness + 15; hunger = hunger - 5;")
            check_stats()
            time.sleep(2.5)

        elif choice == "2":
            print(f"\n📥 {CYAN}[EVENT DISPATCHED: eGiveTreat]{RESET}")
            if hunger >= 90:
                print(" -> execution: conditional refusual. print \"Refused! Barkley is too full.\"")
            else:
                happiness += 10
                hunger += 15
                print(" -> execution: happiness = happiness + 10; hunger = hunger + 15;")
            check_stats()
            time.sleep(2.5)

        elif choice == "3":
            print(f"\n📥 {CYAN}[EVENT DISPATCHED: eFeedDog]{RESET}")
            if hunger >= 100:
                print(" -> execution: conditional refusal. print \"Refused. Barkley falls asleep next to the bowl.\"")
            else:
                hunger += 35
                happiness += 5
                print(" -> execution: hunger = hunger + 35; happiness = happiness + 5;")
            check_stats()
            time.sleep(2.5)

        elif choice.upper() == 'Q':
            break

    clear_view()
    print(f"\n\x1b[33m[ P-Machine Runtime Safely Halted. Engine Disconnected. ]\n{RESET}")

if __name__ == "__main__":
    main()
