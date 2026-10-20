import curses
import random
import time

def matrix_effect(stdscr):
    curses.curs_set(0)  # Hide the mouse cursor
    stdscr.nodelay(True)  # Don't wait for input
    curses.start_color()
    
    # Colors: Green on Black, White on Black for the drop heads
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    height, width = stdscr.getmaxyx()
    columns = [0] * (width - 1)
    speeds = [random.randint(1, 3) for _ in range(width - 1)]
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#@$%&*"

    while True:
        key = stdscr.getch()
        if key == ord('q') or key == ord('Q'):
            break

        new_height, new_width = stdscr.getmaxyx()
        if new_height != height or new_width != width:
            height, width = new_height, new_width
            columns = [0] * (width - 1)
            speeds = [random.randint(1, 3) for _ in range(width - 1)]

        for x in range(len(columns)):
            char = random.choice(chars)
            y = columns[x]

            if y < height - 1:
                if y > 0:
                    try:
                        stdscr.addch(y - 1, x, random.choice(chars), curses.color_pair(1))
                    except curses.error:
                        pass
                try:
                    stdscr.addch(y, x, char, curses.color_pair(2))
                except curses.error:
                    pass

            columns[x] += speeds[x]

            if columns[x] >= height - 1 or random.random() > 0.95:
                for trail_y in range(height - 1):
                    try:
                        stdscr.addch(trail_y, x, ' ')
                    except curses.error:
                        pass
                columns[x] = 0
                speeds[x] = random.randint(1, 3)

        stdscr.refresh()
        time.sleep(0.05)

curses.wrapper(matrix_effect)
