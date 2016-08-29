# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        #print "### Cannot convert", number
        return ""
    
def name_to_number(name):
    if(name == "rock"):
        return 0
    elif(name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        #print "### Cannot convert", name
        return 5

def is_valid_number(number):
    return number >= 0 and number <= 4

    
def rpsls(name):    
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    if (is_valid_number(player_number) and is_valid_number(comp_number)):
        # compute difference of player_number and comp_number modulo five
        diff = (player_number - comp_number) % 5
        # use if/elif/else to determine winner
        winner = ""
        if(diff == 1 or diff == 2):
            winner = "Prayer wins!"
        elif(diff == 3 or diff == 4):
            winner = "Computer wins!"
        else:
            winner = "Player and computer tie!"
            
        # convert comp_number to name using number_to_name
        comp_name = number_to_name(comp_number)
        # print results
        print ("")
        print ("Player chooses", name)
        print ("Computer chooses", comp_name)
        print (winner)
    elif(not (is_valid_number(player_number))):
        print ("")   
        print ("### Cannot convert player string", name)
    else:
        print ("")   
        print ("### Cannot convert computer number", comp_number)
        
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
