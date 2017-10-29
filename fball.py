# Because NFL games can be really boring and you need practice

from random import *

print "Let's play some football!"

def start_game():
	cyline = 20
	print "You are on offense and are starting from your own 20 yard line."
	while (cyline < 100):
		print "The defense is ready, choose your play - run or pass."
		play = raw_input()
		if play == "pass":
			gained = randint(7,15)
			cyline = cyline + gained
			print "You gained " + str(gained) + " yards, nice play!  You are now on the " + str(cyline) + " yard line."
		elif play == "run":
			gained = randint(1,6)
			cyline = cyline + gained
			print "You gained " + str(gained) + " yards.  You are now on the " + str(cyline) + " yard line."
		elif play == "punt":
			print "Are you kidding bro?  Punts don't win games, try again."
		else:
			print "Come on now, pick a real play (or we'll be here all day)"
	print "Congradulations, you finally scored a "
	print "  _____ ___  _   _  ___ _  _ ___   _____      ___  _ _ _ _ "
	print " |_   _/ _ \| | | |/ __| || |   \ / _ \ \    / / \| | | | |"
	print "   | || (_) | |_| | (__| __ | |) | (_) \ \/\/ /| .` |_|_|_|"
	print "   |_| \___/ \___/ \___|_||_|___/ \___/ \_/\_/ |_|\_(_|_|_)"
	print "                                                           "

start_game()


	
