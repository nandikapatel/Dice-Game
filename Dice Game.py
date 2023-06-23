import random   # random number generator 
import time  # to create a pause for when getting an answer

####################################################
#colours 
red = "\033[0;31m"
blue = "\033[0;34m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_blue = "\033[0;94m"
bright_cyan = "\033[0;96m"
####################################################

####################################################
#verifing the players
def verification():
  verify1 = str("123abc")
  verify2 = str("456efg")
  
  v1 = input(white+"\nPlayer 1 enter your password: ")
  while v1 != verify1: 
    #to re-enter password if incorrect
    print (red+ "Incorrect!")
    v1 = input("Player 1 re-enter your password: ")
  
  v2 = input(white+"\nPlayer 2 enter your password: ")
  while v2 != verify2:
    #to re-enter password if incorrect 
    print (red+ "Incorrect!")
    v2 = input("Player 2 re-enter your password: ")
  print(white+"----------------------------")
  time.sleep(0.2)
  print("Welcome in!") 
####################################################

####################################################
#totaling the scores 
def calculatePoints(score, dice1, dice2):
  total = dice1 + dice2 
  EVENTOTAL = 10
  ODDTOTAL = -5
  if total % 2 == 0:
#if total is even add 10 to score 
    score += total + EVENTOTAL
  else:
#if total is odd subtract 5 to score 
    score += total + ODDTOTAL
    #if the score is to be less then 0, the score should be saved as 0 
    if score < 0:
      score = 0
      print (white+"Your total after the point deductions is less than 0, thus your score will remain 0.")

#for when a double is rolled
  if dice1 == dice2:
    dice3 = random.randint(1,6)
    print (white+"Your new total score is:",score,".")
    print("\nSince you rolled doubles, you get to roll an extra die!")
    input ("Press ENTER to roll an extra die...")
    time.sleep(0.5)
    print ("You rolled a", dice3,"!")
    score += dice3
    time.sleep(0.5)
  return score
####################################################

####################################################
#the scoring process
def scoringProcess (dice1,dice2):
  if (dice1 + dice2) % 2 == 0:
      print ("\nSince", dice1, "plus", dice2, "is an even number (", dice1 + dice2, "), 10 points will be added to your score.")
  else:
      print("\nSince", dice1, "plus",dice2, "is an odd number (", dice1 + dice2, "), 5 points will be deducted from your score.")
####################################################

####################################################
#login 
print ("Player 1 please enter your name: ")
p1 = input ("")
print ("Player 2 please enter your name: ")
p2 = input ("")
while p1 == p2:
  print (red+ "Player 2, please enter a diffent name: ")
  p2 = input (white+"")
verification()
####################################################

####################################################

#rules of the game
print ("\n#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")

print (cyan+ "TWO PLAYER DICE GAME")
time.sleep(1)
print(blue+ "\nThis is a 2 player dice game, where 2 players roll two 6-sided dice each and get points depending on what they roll. The game consists of 5 rounds. In each round, each player rolls the two dice.")
time.sleep(0.5)
print ("\nThe rules are:")
print (bright_blue+ "The points rolled on each player’s dice are added to their score. If the added total is an even number, an additional 10 points are added to their total score. Whereas if the added total is an odd number, 5 points are subtracted from their total score. However, at no point in the game shall a player's score go below 0.")
print ("If a player rolls a double, they get to roll one extra die and the number rolled gets added to their score. The score of a player cannot go below 0 at any point.")
print ("The person with the highest score at the end of all 5 rounds wins. If both players happen to have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).")
print (white+"\nHave Fun!")

print ("\n#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
####################################################

####################################################
#variables
NUMPLAYERS = 2
player = 0
score1 = 0
score2 = 0
####################################################

####################################################
print (red+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print (white+"First Round...")
ROUNDS = 10
for g in range(ROUNDS):
  total = 0
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  ###############################################
  # if player (a number starting 0 and increasing by 1) mod NUMPLAYERS (2 players) equals 0, the player playing will by player 1. If it equals 1, the player playing will be player 2. 
  if player % NUMPLAYERS == 0:
    print(red+"----------------------------")
    input (bright_cyan+ p1 + ", press ENTER to roll both dice...")
    print("\nYou rolled a" , dice1,"and a",dice2, "!")
    scoringProcess(dice1,dice2)
    print(red+"----------------------------")
    score1 = calculatePoints(score1, dice1, dice2)
    print (white+"Your total score after this round is:",score1,".")
    time.sleep(0.5)

  else:
    print(red+"----------------------------")
    input (bright_blue+ p2 + ", press ENTER to roll both dice...")
    print("\nYou rolled a", dice1, "and a",dice2,"!")
    scoringProcess(dice1,dice2)
    print(red+"----------------------------")
    score2 = calculatePoints(score2, dice1, dice2)
    print (white+"Your total score after this round is:",score2, ".")
    time.sleep(0.5)
    print(red+"----------------------------")

  ###############################################

  ###############################################
  #g = the variable representing the count from 0-9, meaning every 2 counts = 1 round --> e.x. (if g = 1) 1 % 2 = 1 ==> round 1 
  if g % 2 == 1:   
    ###########################################
    #if not in the last round: 
    if g != 9:
      print (red+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      input (white+"Press ENTER to continue to the next round...")
      time.sleep(0.5)
####################################################
  player += 1
####################################################

print (red+"\n~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~")
print ("\n"+red+ p1,"'s final score is",score1, "and", p2, "'s final score is", score2, "!")

###########################################
if score1 > score2:
  time.sleep(0.5)
  print ("\n",p1,"has won with",score1-score2, "more points than",p2,"!")
elif score1 < score2:
 time.sleep(0.5)
 print ("\n",p2,"has won with",score2-score1, "points more than",p1,"!")
else:
  print (white+ "You both get to roll an extra dice since you are tied!")
  extra1 = random.randint(1,6)
  score1 += extra1
  time.sleep(0.5)
  input (p1 + ", press ENTER to roll the extra die...")
  print ("You rolled a...",extra1, "!")
  extra2 = random.randint(1,6)
  score2 += extra2
  time.sleep(0.5)
  input (p2 +", press ENTER to roll the extra die...")
  print ("You rolled a...",extra2, "!")
#########################################
while extra1 == extra2: 
    print ("You both must keep rolling an extra dice each util a winner is determined!")
    extra1 = random.randint(1,6)
    score1 += extra1
    time.sleep(0.5)
    input (p1 + ", press ENTER to roll the extra die...")
    print ("You rolled a...",extra1, "!")
    extra2 = random.randint(1,6)
    score2 += extra2
    time.sleep(0.5)
    input (p2 + ", press ENTER to roll the extra die...")
    print ("You rolled a...", extra2, "!")
#########################################
  time.sleep(0.5)
#########################################
  if extra1 > extra2:
    print (red+"----------------------------")
    print (white+ p1,"has won since",extra1,"is greater than", extra2, "!")
  elif extra1 < extra2:
    print (red+"----------------------------")
    print (white+p2,"has won since", extra2, "is greater than", extra1,"!")
