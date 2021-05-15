#!/usr/bin/env python

import os, sys, select
import time
import datetime
import random
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

os.system("clear") #clear panel
GPIO.setwarnings(False)
reader = SimpleMFRC522()

CRED = '\033[91m'
CGREEN = '\33[92m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
YELLOW  = '\033[33m'
MAGENTA = '\u001b[35;1m'

def read():
	try:
		now = datetime.datetime.now()
		id, text = reader.read()
		id = str(id) #First value
		text = str(text) #Second value
		if "Error" in id:
			return("ERROR, RETRY")
		else:
			if "Error" in text:
				return("ERROR, RETRY")
			else:
				if text == "": #Checking if there is a second value
					check_true = "false"
				else:
					check_true = "true"
				if check_true == "true":
					return(text)
				else:
					return(id)
	finally:
		GPIO.cleanup()

def write(str):
	try:
		now = datetime.datetime.now()
		reader.write(str)
		return "success"
	finally:
		GPIO.cleanup()
	
def unlock(str):
	now = datetime.datetime.now()
	print (WHITE+"[+]"+CGREEN+ " " + str + " signed in - " +now.strftime("%Y-%m-%d %H:%M:%S"))

def menu():
	os.system("clear")
	print(MAGENTA+''' _____  ______ _____ _____  _              _ 
|  __ \|  ____|_   _|  __ \| |            | |
| |__) | |__    | | | |  | | |_ ___   ___ | |
|  _  /|  __|   | | | |  | | __/ _ \ / _ \| |
| | \ \| |     _| |_| |__| | || (_) | (_) | |
|_|  \_\_|    |_____|_____/ \__\___/ \___/|_|''')
	print(WHITE+"-------------------------------------------------------")
	print(WHITE+"[+]"+CGREEN+" rFID Lookup (RFID-RC522 via Pi4)")
	print(WHITE+"[-]"+CGREEN+" Written by " + CRED + "Underscores" + CGREEN + " 5/14/2021")
	print(WHITE+"-------------------------------------------------------")
	print(WHITE+"[+]"+CGREEN+" What would you like to do?")
	print(WHITE+"[-]"+CGREEN+" 1 = Startup 24/7 Reading")
	print(WHITE+"[-]"+CGREEN+" 2 = Write New Card")
	print(WHITE+"[-]"+CGREEN+" 3 = Read Card")
	print(WHITE+"[-]"+CGREEN+" 4 = Add New User")
	print(WHITE+"-------------------------------------------------------")

	input1 = input(CGREEN + "What would you like to do? " + WHITE)
	color_list = ["\33[92m", "\033[36m", "\033[37m", "\033[33m", "\u001b[35;1m"]

	if input1 == "1":
		print(WHITE+"-------------------------------------------------------")
		print(WHITE+"[+]" + CGREEN + " Sniffer is on, waiting for card to be read")
		print(WHITE+"[-]" + CGREEN + " Press ENTER at anytime to stop")
		while True:
			if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
				menu()
			card = read()
			if card != "":
				print(random.choice(color_list) + card)
	else:
		if input1 == "2":
			print(WHITE+"-------------------------------------------------------")
			input2 = input(WHITE+"[+]" + CGREEN + " Data you want to write to card: " + WHITE)
			reader.write(input2)
			print(WHITE+"[-]" + CGREEN + " Your card has been successfully written with data: " + WHITE +  input2)
			wait = input(WHITE+"[-]"+CGREEN+ " Press ENTER to return to menu")
			menu()
		else:
			if input1 == "3":
				print(WHITE+"-------------------------------------------------------")
				print(WHITE+"[+]" + CGREEN + " Awaiting read...")
				card = read()
				print(WHITE+"[-]" + CGREEN + " Card was successfully read: " + WHITE + card)
				#print(card)
				wait = input(WHITE+"[-]"+CGREEN+ " Press ENTER to return to menu")
				menu()
			else:
				if input1 == "4":
					print("soon")
					menu()
				else:
					menu()

menu()
