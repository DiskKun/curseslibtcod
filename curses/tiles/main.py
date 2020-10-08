## MODULES
import curses
import random
from curses import wrapper
from curses import textpad
from curses.textpad import Textbox

## CURSES INITIALIZATION
stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)
stdscr.resize(24, 80)

## PLAYER INITIALIZATION
class Player:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		
		self.inventory = []
		self.armor = {
			"head": ["Cloth Hat", 1],
			"torso": ["Cloth Shirt", 1],
			"legs": ["Cloth Pants", 1],
			"feet": ["Shoes", 1],
			"hand1": [],
			"hand2": []
		}
		self.weapons = {
			"Stick": 1
		}
		self.playerx = 40
		self.playery = 12

## MAKE PLAYER (TEMP)
p = Player(name="Player", type="Rogue")

## MAIN FUNCTION
def main(stdscr):
	draw()
	while True:
		action()
	stdscr.getkey()
	end()

## PLAYER INPUT ACTIONS
def action():
	inp = stdscr.getkey()
	if inp == "KEY_UP":
		move("up")
	elif inp == "KEY_DOWN":
		move("down")
	elif inp == "KEY_LEFT":
		move("left")
	elif inp == "KEY_RIGHT":
		move("right")
		
## MOVEMENT
def move(direction):
	if direction == "up" and p.playery > 1:
		if stdscr.inch(p.playery-1, p.playerx) != 35:
			p.playery -= 1
	elif direction == "down" and p.playery < 22:
		if stdscr.inch(p.playery+1, p.playerx) != 35:
			p.playery += 1
	elif direction == "left" and p.playerx > 1:
		if stdscr.inch(p.playery, p.playerx-1) != 35:
			p.playerx -= 1
	elif direction == "right" and p.playerx < 78:
		if stdscr.inch(p.playery, p.playerx+1) != 35:
			p.playerx += 1
	draw()
	
## DRAW SCREEN
def draw():
	## clear
	stdscr.erase()
	with open("map0.txt", "r+") as file:
		for i in file:
			stdscr.addstr(file.readline())
	## border
	stdscr.border()
	## player
	stdscr.addch(p.playery, p.playerx, "&")

## END
def end():
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	quit()

wrapper(main)
