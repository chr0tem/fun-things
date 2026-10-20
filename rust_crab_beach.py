import os
import random
import time
import sys

# Retro Color Codes
RED = "\x1b[31m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"
RESET = "\x1b[0m"

BOLT_CHARS = ["/", "\\", "_", "|", "-", "x", "+", "*"]

def run_beach_storm():
    print("\x1b[2J") # Clear the screen once at the start
    
    crab_x = 10
    crab_dir = 1 # 1 means moving right, -1 means moving left

    try:
        while True:
            # 1. Get the terminal size automatically without external folders
            try:
                columns, rows = os.get_terminal_size()
            except OSError:
                columns, rows = 80, 24

            # Create a blank grid array matching your screen dimensions
            grid = [[" " for _ in range(columns)] for _ in range(rows)]
            
            # 2. DESIGN THE BEACH AND WATER AT THE BOTTOM
            sand_row = rows - 2
            water_row = rows - 1
            for x in range(columns):
                if x % 4 == 0:
                    grid[sand_row][x] = f"{YELLOW}.{RESET}" # Yellow sand particles
                grid[water_row][x] = f"{BLUE}~{RESET}"     # Blue ocean water line

            # 3. ANIMATE FERRIS THE CRAB WALK
            crab_x += crab_dir
            if crab_x >= columns - 10:
                crab_x = columns - 10
                crab_dir = -1 # Hit the right wall, turn left
            elif crab_x <= 2:
                crab_x = 2
                crab_dir = 1  # Hit the left wall, turn right

            # Choose his shell direction art piece
            crab_sprite = "(v.v)🦀>" if crab_dir == 1 else "<🦀(v.v)"
            
            # Print Ferris onto the sand row margin
            for i, char in enumerate(crab_sprite):
                if crab_x + i < columns:
                    grid[sand_row - 1][crab_x + i] = f"{RED}{char}{RESET}"

            # 4. RANDOM LIGHTNING BURSTS
            # 15% chance to drop a lightning branch frame from the clouds
            if random.random() < 0.15:
                start_x = random.randint(5, columns - 6)
                curr_x = start_x
                
                # Trace the lightning down until it hits the beach line
                for y in range(sand_row - 1):
                    color = random.choice([CYAN, WHITE])
                    grid[y][curr_x] = f"{color}{random.choice(BOLT_CHARS)}{RESET}"
                    
                    # Jag the bolt pathway organically sideways
                    curr_x += random.choice([-1, 0, 1])
                    if curr_x < 0: curr_x = 0
                    if curr_x >= columns: curr_x = columns - 1

                # Add a high-voltage impact splash block near Ferris's walk line
                for spark_x in range(max(0, curr_x - 2), min(columns, curr_x + 3)):
                    grid[sand_row - 1][spark_x] = f"{YELLOW}*{RESET}"

            # 5. RENDER THE COMBINED DISPLAY FRAME
            output = "\n".join("".join(row) for row in grid)
            sys.stdout.write("\x1b[H" + output) # Move cursor to top-left instantly
            sys.stdout.flush()

            # Keep a stable frame rate animation speed (Approx 12 updates per second)
            time.sleep(0.08)

    except KeyboardInterrupt:
        print("\n\x1b[0mBeach storm cleared. Ferris crawled back into his shell safely.")

if __name__ == "__main__":
    run_beach_storm()
