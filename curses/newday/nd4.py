import curses
import time
from playsound import playsound
import random

from curses import wrapper

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)

stdscr.setscrreg(1, 24)
stdscr.scrollok(True)

stdscr.resize(24, 80)

stdscr.addstr(10, 10, "Loading...")

def main(stdscr):
	playsound('./click.wav', False)
	padpos = 0
	exitprg = False
	stdscr.clear()
	stdscr.box()
	stdscr.addstr(10, 10, "Ready! (Press a Key)")
	stdscr.getch()
	stdscr.clear()
	stdscr.refresh()
	time.sleep(1)

	file = open("newday4.txt", "r")

	while exitprg == False:
		col = 1

		line = file.readline()
		linelen = len(line)
		for i in line:
			playsound('click.wav', False)
			stdscr.addch(22, col, i)
			stdscr.refresh()
			col += 1
			time.sleep(random.uniform(0.02, 0.1))
		time.sleep(1)
		playsound('click.wav', False)
		stdscr.scroll()
		stdscr.refresh()
		time.sleep(1)
	#stdscr.box()
	stdscr.getch()
	end()

def end():
	curses.echo()
	curses.endwin()

wrapper(main)
