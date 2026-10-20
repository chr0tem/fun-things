using Random

function clear_canvas()
    # Wipe the terminal viewport
    print("\x1b[2J")
end

function run_game()
    affection = 40
    hunger = 50
    running = true

    clear_canvas()

    while running
        # \x1b[H snaps cursor to top-left (0,0) to prevent screen stuttering
        print("\x1b[H")
        println("==================================================")
        println("         PET EMULATOR V1.0 // JULIA CAT ENGINE    ")
        println("==================================================")

        # Render the text-art cat based on its data states
        if affection >= 75
            println("   /\\_/\\    * Purr... *")
            println("  ( =^.^= )   * ✨ *")
            println("   >  o  <")
        else
            println("   /\\_/\\ ")
            println("  ( o.o )")
            xl  = "   > ^ < "
            println(xl)
        end
        println("  /     \\")
        println(" (_______)x\n")

        # Format dynamic metrics output rows
        @printf("💖 Affection Level: %d%%\n", affection)
        @printf("🍖 Hunger Saturation: %d%%\n\n", hunger)

        println("  1: Pet the cat")
        println("  2: Give Treat")
        println("  3: Feed cat")
        println("\n  Press [Q] then Enter to Halt Machine\n")
        print("Select Action (1-3) > ")

        # Read line parameter input streams safely
        user_input = strip(uppercase(readline()))

        if user_input == "1"
            # Roll a 20% random strike chance
            if rand(1:5) == 1
                affection -= 10
                println("\n⚡ Swipe! The cat swatted your hand away.     ")
            else
                affection += 15
                println("\nPurrrrr... The cat leans into your hand.     ")
            end
            flush(stdout)
            sleep(1.2) # Pause frame to read trace logging
        elseif user_input == "2"
            if hunger >= 90
                println("\nThe cat turns its nose up. Uninterested.     ")
            else
                affection += 10
                hunger += 15
                println("\nCrunch crunch. It neatly eats the treat.     ")
            end
            flush(stdout)
            sleep(1.2)
        elseif user_input == "3"
            if hunger >= 100
                println("\nThe bowl is full. The cat ignores it.        ")
            else
                hunger += 35
                affection += 5
                println("\nNom nom nom. The food bowl is cleared.       ")
            end
            flush(stdout)
            sleep(1.2)
        elseif user_input == "Q"
            running = false
        end

        # Ambient background stats degradation tick
        if rand(1:3) == 1
            hunger -= 5
        end

        # Cap data boundaries safely between 0 and 100
        affection = max(0, min(100, affection))
        hunger = max(0, min(100, hunger))

        # Clear remaining dangling output lines underneath active fields
        print("\x1b[J")
    end

    clear_canvas()
    print("\x1b[H")
    println("Julia Cat Engine successfully disconnected.\n")
end

# Fire up the engine wrapper!
run_game()
