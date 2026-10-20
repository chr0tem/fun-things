import std.stdio;
import std.string;
import std.random;
import std.conv;
import core.thread;

void main() {
    int affection = 40;
    int hunger = 50;
    bool running = true;

    // Clear the standard terminal canvas at boot
    write("\x1b[2J");

    while (running) {
        // \x1b[H snaps cursor to top-left (0,0) to prevent loop screen stuttering
        write("\x1b[H");
        writeln("==================================================");
        writeln("         PET EMULATOR V1.0 // DLANG CAT CORE       ");
        writeln("==================================================");

        // Render the text-art cat based on its data states
        if (affection >= 75) {
            writeln("   /\\_/\\    * Purr... *");
            writeln("  ( =^.^= )   * ✨ *");
            writeln("   >  o  <");
        } else {
            writeln("   /\\_/\\ ");
            writeln("  ( o.o )");
            writeln("   > ^ < ");
        }
        writeln("  /     \\");
        writeln(" (_______)x\n");

        // Format dynamic metrics output rows
        writefln("💖 Affection Level: %d%%", affection);
        writefln("🍖 Hunger Saturation: %d%%\n", hunger);

        writeln("  1: Pet the cat");
        writeln("  2: Give Treat");
        writeln("  3: Feed cat");
        writeln("\n  Press [Q] then Enter to Halt Machine\n");
        write("Select Action (1-3) > ");

        // Collect string line input parameters cleanly via standard input streams
        string input = readln().strip().toUpper();

        if (input == "1") {
            // Roll a quick pseudo-random 20% scratch chance metric
            if (uniform(0, 5) == 0) {
                affection -= 10;
                writeln("\n⚡ Swipe! The cat swatted your hand away.     ");
            } else {
                affection += 15;
                writeln("\nPurrrrr... The cat leans into your hand.     ");
            }
            stdout.flush();
            Thread.sleep(dur!"msecs"(1200)); // Freeze layout frame to read trace logging
        }
        else if (input == "2") {
            if (hunger >= 90) {
                writeln("\nThe cat turns its nose up. Uninterested.     ");
            } else {
                affection += 10;
                hunger += 15;
                writeln("\nCrunch crunch. It neatly eats the treat.     ");
            }
            stdout.flush();
            Thread.sleep(dur!"msecs"(1200));
        }
        else if (input == "3") {
            if (hunger >= 100) {
                writeln("\nThe bowl is full. The cat ignores it.        ");
            } else {
                hunger += 35;
                affection += 5;
                writeln("\nNom nom nom. The food bowl is cleared.       ");
            }
            stdout.flush();
            Thread.sleep(dur!"msecs"(1200));
        }
        else if (input == "Q") {
            running = false;
        }

        // Ambient stats degradation tick
        if (uniform(0, 3) == 0) {
            hunger -= 5;
        }

        // Cap data boundaries safely between 0 and 100
        if (affection > 100) affection = 100;
        if (affection < 0)   affection = 0;
        if (hunger > 100)    hunger = 100;
        if (hunger < 0)      hunger = 0;

        // Clear remaining dangling output lines underneath active fields
        write("\x1b[J");
    }

    write("\x1b[2J\x1b[H");
    writeln("Dlang Cat Engine successfully disconnected.\n");
}
