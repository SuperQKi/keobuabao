print("What do you choose?")
from random import randint
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Bua"
if computer == 1:
	computer = "Bao"
if computer == 2:
	computer = "Keo"
print("-------")
print("You choose:" + str(player))
print("computer chooses:" + str(computer))
print("--------")
if player == computer:
	print("Draw")
else:
	if player == "Keo":
		if computer == "Bua":
			print("Lose")
		else:
			print("Win")

	elif player == "Bua":
		if computer == "Keo":
			print("Win")
		else:
			print("Lose")

	elif player == "Bao":
		if computer == "Keo":
			print("Lose")
		else:
			print("Win")
	else:
		print(" Nhap lai")

