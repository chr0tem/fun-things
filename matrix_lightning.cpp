#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <unistd.h>
#include <ncurses.h>

struct Strike {
    int start_x;
    int current_y;
    int current_x;
    int active_ticks;
};

const std::string BOLT_CHARS = "/\\_|-x+*";

int main() {
    initscr();
    cbreak();
    noecho();
    curs_set(0);       // Hide terminal cursor
    nodelay(stdscr, TRUE); // Keep loop spinning smoothly
    keypad(stdscr, TRUE);

    start_color();
    init_pair(1, COLOR_CYAN, COLOR_BLACK);   // Lightning Arc Glow
    init_pair(2, COLOR_WHITE, COLOR_BLACK);  // Core High Voltage Bolt
    init_pair(3, COLOR_WHITE, COLOR_BLUE);   // Power Grounding Flash

    int height, width;
    getmaxyx(stdscr, height, width);
    std::srand(std::time(0));

    std::vector<Strike> active_strikes;
    std::vector<int> ground_flash(width, 0);

    bool running = true;
    while (running) {
        int ch = getch();
        if (ch == 'q' || ch == 'Q') {
            running = false;
        }

        // Auto handling window resizes
        int new_height, new_width;
        getmaxyx(stdscr, new_height, new_width);
        if (new_height != height || new_width != width) {
            height = new_height;
            width = new_width;
            active_strikes.clear();
            ground_flash.assign(width, 0);
            clear();
        }

        // Randomly spark a new lightning bolt from the sky row
        if (rand() % 15 == 0 && active_strikes.size() < 4) {
            Strike s;
            s.start_x = rand() % width;
            s.current_x = s.start_x;
            s.current_y = 0;
            s.active_ticks = (rand() % 8) + 5; // Lifetime tracking
            active_strikes.push_back(s);
        }

        // Clear out old residual arcs from the grid canvas
        clear();

        // --- RENDER CURRENT SKY STRIKES ---
        for (auto it = active_strikes.begin(); it != active_strikes.end();) {
            it->active_ticks--;
            
            int temp_x = it->start_x;
            int temp_y = 0;

            // Generate an organic branched pathway down to the floor
            while (temp_y < height - 2) {
                temp_y++;
                // Let the bolt jag left (-1), stay straight (0), or jag right (+1)
                temp_x += (rand() % 3) - 1;
                if (temp_x < 0) temp_x = 0;
                if (temp_x >= width) temp_x = width - 1;

                // Pick high voltage colors
                int color_pair = (rand() % 2 == 0) ? 1 : 2;
                attron(COLOR_PAIR(color_pair) | A_BOLD);
                mvaddch(temp_y, temp_x, BOLT_CHARS[rand() % BOLT_CHARS.length()]);
                attroff(COLOR_PAIR(color_pair) | A_BOLD);
            }

            // Once the pathway touches down, lock the ground index for horizontal arcing
            if (it->active_ticks <= 0) {
                ground_flash[temp_x] = 6; // Set flash duration loops
                it = active_strikes.erase(it);
            } else {
                ++it;
            }
        }

        // --- RENDERING GROUND DISCHARGES ---
        for (int x = 0; x < width; ++x) {
            if (ground_flash[x] > 0) {
                ground_flash[x]--;

                int ground_y = (height - 2) + (rand() % 2);
                char spark_char = BOLT_CHARS[rand() % BOLT_CHARS.length()];

                // Use the ultimate blinding blue background flash blocks
                attron(COLOR_PAIR(3) | A_BOLD);
                mvaddch(ground_y, x, spark_char);
                if (x > 0 && rand() % 2 == 0) mvaddch(ground_y, x - 1, spark_char);
                if (x < width - 1 && rand() % 2 == 0) mvaddch(ground_y, x + 1, spark_char);
                attroff(COLOR_PAIR(3) | A_BOLD);
            }
        }

        refresh();
        usleep(45000); // 45ms animation tick speed
    }

    endwin();
    return 0;
}
