package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"os/exec"
	"strings"
	"time"
)

func clearCanvas() {
	cmd := exec.Command("clear")
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func main() {
	// Initialize random seed generation utilities
	rand.Seed(time.Now().UnixNano())

	affection := 40
	hunger := 50
	running := true
	reader := bufio.NewReader(os.Stdin)

	// Initial screen clear
	clearCanvas()

	for running {
		// \x1b[H snaps the cursor to top-left (0,0) preventing layout stutter
		fmt.Print("\x1b[H")
		fmt.Println("==================================================")
		fmt.Println("         PET EMULATOR V1.0 // GOLANG CAT CORE     ")
		fmt.Println("==================================================")

		// Render responsive text-art depending on affection scores
		if affection >= 75 {
			fmt.Println("   /\\_/\\    * Purr... *")
			fmt.Println("  ( =^.^= )   * ✨ *")
			fmt.Println("   >  o  <")
		} else {
			fmt.Println("   /\\_/\\ ")
			fmt.Println("  ( o.o )")
			fmt.Println("   > ^ < ")
		}
		fmt.Println("  /     \\")
		fmt.Println(" (_______)x\n")

		// Print layout status gauges
		fmt.Printf("💖 Affection Level: %d%%\n", affection)
		fmt.Printf("🍖 Hunger Saturation: %d%%\n\n", hunger)

		fmt.Println("  1: Pet the cat")
		fmt.Println("  2: Give Treat")
		fmt.Println("  3: Feed cat")
		fmt.Println("\n  Press [Q] then Enter to Halt Machine\n")
		fmt.Print("Select Action (1-3) > ")

		// Intercept keyboard stream line string parameters
		input, _ := reader.ReadString('\n')
		char := strings.ToUpper(strings.TrimSpace(input))

		if char == "1" {
			// Roll a 20% random strike chance
			if rand.Intn(5) == 0 {
				affection -= 10
				fmt.Println("\n⚡ Swipe! The cat swatted your hand away.     ")
			} else {
				affection += 15
				fmt.Println("\nPurrrrr... The cat leans into your hand.     ")
			}
			os.Stdout.Sync()
			time.Sleep(1200 * time.Millisecond)
		} else if char == "2" {
			if hunger >= 90 {
				fmt.Println("\nThe cat turns its nose up. Uninterested.     ")
            } else {
				affection += 10
				hunger += 15
				fmt.Println("\nCrunch crunch. It neatly eats the treat.     ")
			}
			os.Stdout.Sync()
			time.Sleep(1200 * time.Millisecond)
		} else if char == "3" {
			if hunger >= 100 {
				fmt.Println("\nThe bowl is full. The cat ignores it.        ")
			} else {
				hunger += 35
				affection += 5
				fmt.Println("\nNom nom nom. The food bowl is cleared.       ")
			}
			os.Stdout.Sync()
			time.Sleep(1200 * time.Millisecond)
		} else if char == "Q" {
			running = false
		}

		// Background degradation math ticks
		if rand.Intn(3) == 0 {
			hunger -= 5
		}

		// Enforce state boundary limits
		if affection > 100 { affection = 100 }
		if affection < 0   { affection = 0 }
		if hunger > 100    { hunger = 100 }
		if hunger < 0      { hunger = 0 }

		// Clear hanging layout artifacts from viewport
		fmt.Print("\x1b[J")
	}

	clearCanvas()
	fmt.Println("Go Cat Engine successfully disconnected.\n")
}
