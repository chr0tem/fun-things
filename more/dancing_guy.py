import os
import time
import sys

# Setup glowing text colors
CYAN = "\x1b[36;1m"
YELLOW = "\x1b[33m"
RESET = "\x1b[0m"

# The 4 frames of the classic 2000s text dancing guy
FRAME_1 = """
    (•◡•) /
     /|/
     / \\
"""

FRAME_2 = """
   \\ (•◡•) /
     \\|/
      |
     / \\
"""

FRAME_3 = """
     \\ (•◡•)
       \\|\\
       / \\
"""

FRAME_4 = """
   \\ (•◡•) /
     \\|/
      |
     / \\
"""

def main():
    frames = [FRAME_1, FRAME_2, FRAME_3, FRAME_4]
    loop_count = 0
    
    os.system("clear")
    print(f"{CYAN}Booting Text Graphic Engine...{RESET}")
    time.sleep(1)

    try:
        while True:
            for frame in frames:
                # Move cursor back to top-left instead of repeating lines
                sys.stdout.write("\x1b[H")
                
                print(f"{CYAN}=================================================={RESET}")
                print(f"     RETRO DANCE CHASSIS v1.0 // ENGINE ACTIVE     ")
                print(f"{CYAN}=================================================={RESET}\n")
                
                # Print the active text character frame
                print(f"{YELLOW}{frame}{RESET}")
                
                print(f"\n{CYAN}--------------------------------------------------{RESET}")
                print(f"Cycle Ticks: {loop_count}  ||  Press Ctrl+C to Halt")
                sys.stdout.flush()
                
                loop_count += 1
                time.sleep(0.18) # Animation delay frame rate speed

    except KeyboardInterrupt:
        os.system("clear")
        print(f"\n{CYAN}Animation paused safely. Engine halted.{RESET}\n")

if __name__ == "__main__":
    main()
