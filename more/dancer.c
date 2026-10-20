#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int ticks = 0;

    // Define the 4 text-art frames exactly like our C-- memory strings
    char* frame1 = "    (•◡•) /\n     /|/\n     / \\\n";
    char* frame2 = "   \\ (•◡•) /\n     \\|/\n      |\n     / \\\n";
    char* frame3 = "     \\ (•◡•)\n       \\|\\\n       / \\\n";
    char* frame4 = "   \\ (•◡•) /\n     \\|/\n      |\n     / \\\n";

    char* frames[] = {frame1, frame2, frame3, frame4};

    // Execute system call to clear the terminal window initially
    system("clear");

    // Infinite master while loop
    while (1) {
        for (int i = 0; i < 4; i++) {
            // \x1b[H snaps the cursor to the top-left (0,0) without clearing, preventing flicker
            printf("\x1b[H");
            printf("==================================================\n");
            printf("     RETRO DANCE CHASSIS // C ENGINE ACTIVE       \n");
            printf("==================================================\n\n");
            
            // Print the current frame matrix
            printf("%s\n", frames[i]);
            
            printf("--------------------------------------------------\n");
            printf("Loop Ticks: %d  || Press Ctrl+C to Halt\n", ticks);
            
            ticks++;
            
            // Wait 180,000 microseconds (0.18 seconds) using the native system sleep call
            usleep(180000);
        }
    }

    return 0;
}
