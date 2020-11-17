# The Fires of Norbak

version: 0.3.2

Changelog:
v0.3.2:
 - Removed input queuing. Now when you press a key or perform any other type of input, those inputs will be "flushed" from the queue.

v0.3.1:
 - Added typetext skipping; for text that appears one character at a time, you can press space to display the full text instantly.

v0.3:
 - Added shop & currency

v0.2:
 - Added weapons & armor.
 - Fixed the runaway feature, so now when you unsuccessfully run away, you take the turn's damage as normal.
 
imports: curses (windows-curses on Windows), random, time, playsound

Space is the select key, rather than enter. Curses doesn't work well with the enter key, for some reason. The only exception to this is when you are inputing your name, here enter will work.
