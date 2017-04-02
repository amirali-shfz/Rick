
import webbrowser
import time


class Character(object):
    def __init__(self, power, face):
        self.power = power
        self.face = face

print """=====================================
###ALL THE CHARACTERS ARE FICTIONAL###

Welcome to our journey! We will set out
to defeat Trumpi!
At the end, you will be asked for a password in order to
enter the final room. Through your journey, you
will be given a number in each stage. Put the numbers
together to find the password.
=====================================
Now you have to choose your character.

wizard or ninja?
====================================="""

pr = raw_input('>>>')

def ask(x, o, p, f):
    x = x.lower()
    while x != o and x != p:
        print""
        print f
        x = raw_input('>>>')
    return x

letter = """*********
WTF are you saying?!
Please either type wizard or ninja (^__^)
*********"""
pr = ask(pr, "wizard", "ninja", letter)

print """=====================================
****QUESTION NUMBER 1****
====================================="""
x = raw_input("In what month was Richard Paul Rick Astley born?")
x = x.lower()
if x == 'february':
    print """[X][X][X][X][X][X][X][X][X][X][X][X]
Your first number is ++++[ 4 ]++++
====================================="""
else:
    print """=====================================
WRONG ANSWER!
GAME OVER
====================================="""
    webbrowser.open('http://imgur.com/xbHSlNX')
    quit()

print """=====================================
Nice going Mr. %s!
What facial feature do you want?
A mustache or a beard?
=====================================""" %(pr.upper())

letter1 = """=====================================
Waaaahh???!
Please either type mustache or beard!
====================================="""
wp = raw_input('>>>')

wp = ask(wp, "mustache", "beard", letter1)

print """[X][X][X][X][X][X][X][X][X][X][X][X]
=====================================
****QUESTION NUMBER 2****
====================================="""
x = input("""In what year was Never Gonna Give You Up recorded?""")
if x == 1987:
    print """[X][X][X][X][X][X][X][X][X][X][X][X]
=====================================
Your second number is ++[ 2 ]++
====================================="""
else:
    print """=====================================
WRONG ANSWER!
GAME OVER
====================================="""
    webbrowser.open('http://imgur.com/xbHSlNX')
    quit()

you = Character(pr, wp)

print """[X][X][X][X][X][X][X][X][X][X][X][X]
=====================================
OKAAAY! Hey, BTW That %s looks nice on you!

Now you have to defeat Trumpi because he wants
to make a WA.. WALL.. WALL.. WALLET! You hate
wallets!
Do you want to drive your car or helicopter?
=====================================""" %(you.face)

letter2 = "You can't ride that! car or helicopter?"
vc = raw_input('>>>')

vc = ask(vc, "car", "helicopter", letter2)

if vc == "car":
    print 'VROOM VROOM!'
elif vc == "helicopter":
    print 'TOCOTOCOTOCOTOCO!!!'



print """ [X][X][X][X][X][X][X][X][X][X][X][X]
^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
You now see the WALLET making factory!

QUICK, the guards are looking at you, say something!!

( 1 ) 'NEVER GONNA GIVE YOU UP!'
( 2 ) 'I HATE WALLETS!'
^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~"""
x = input("""
1 or 2?""")

if x == 1:
    print """[X][X][X][X][X][X][X][X][X][X][X][X]
Nice choice! Your last number is ++++[ 0 ]++++"""
else:
    print """ GAME OVER MY FRIEND... """
    webbrowser.open('http://imgur.com/xbHSlNX')
    quit()

print """^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
Finally... You are here. Trumpi is here. WALLETS are here.
YOU HATE WALLETS!!!! """

if pr == "ninja":
    print """You need to cut his head ninja! But...
You need a password to open the last door"""
else:
    print """You need to explode him with your spell wizard!
But... You need a password to open the last door"""

pas = input("""^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
PASSWORD: """
)

if pas == 420:
    print "GOOD JOB!"

else:
    print "WRONG PASSWORD!"
    webbrowser.open('http://imgur.com/xbHSlNX')
    quit()

if you.face == "mustache":
    if you.power == "ninja":
        webbrowser.open('http://imgur.com/V2BzHxj')

    else:
        webbrowser.open('http://imgur.com/a/dqw9p')

elif you.face == "beard":
    if you.power == "ninja":
        webbrowser.open('http://imgur.com/SDqxRHM')
    else:
        webbrowser.open('http://imgur.com/gallery/KNCZ1')

time.sleep(10)

webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
