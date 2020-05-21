# import curses
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == 27:
                break
                ''' char == curses.KEY_UP:
                print "up"
            elif char == curses.KEY_DOWN:
                print "down"
            elif char == curses.KEY_RIGHT:
                print "right"
            elif char == curses.KEY_LEFT:
                print "left"
            elif char == 10:
                for x in range (9):
                    print("%d.Hello Puto,I Love You SOOO Much"%x)
                    # time.sleep(1)'''
            #all The small letters
            elif char == ord('y'):
                print "y"
            elif char == ord('q'):
                print "q"
            elif char == ord('w'):
                print "w"
            elif char == ord('e'):
                print "e"
            elif char == ord('r'):
                print "r"
            elif char == ord('t'):
                print "t"
            elif char == ord('u'):
                print "u"
            elif char == ord('i'):
                print "i"
            elif char == ord('o'):
                print "o"
            elif char == ord('p'):
                print "p"
            elif char == ord('a'):
                print "a"
            elif char == ord('s'):
                print "s"
            elif char == ord('d'):
                print "d"
            elif char == ord('f'):
                print "f"
            elif char == ord('g'):
                print "g"
            elif char == ord('h'):
                print "h"
            elif char == ord('j'):
                print "j"
            elif char == ord('k'):
                print "k"
            elif char == ord('l'):
                print "l"
            elif char == ord('z'):
                print "z"
            elif char == ord('x'):
                print "x"
            elif char == ord('c'):
                print "c"
            elif char == ord('v'):
                print "v"
            elif char == ord('b'):
                print "b"
            elif char == ord('n'):
                print "n"
            elif char == ord('m'):
                print "m"

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()