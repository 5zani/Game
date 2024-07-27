print('''
***************************
          |                   |                  |                     |
 ___|_____.="";=._____|_______|__
|                   |  ,-"_,=""     `"=.|                  |
|______|"=._o`"-.        `"=._____|______
          |                "=._o"=._      `"=.                     |
 ___|_______:=.o "=..".-="'"=.______|__
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
|______|."  ,. .` ` `` ,  `"-."-._   ". '_|______
          |           |o`"=.` , "` `; .". ,  "-."-._; ;              |
 ___|____| ;-.o"=.; ." ` '."\ . "-._ /_____|___
|                   | |o;    "-.o"=.``  '` " ,_.--o;   |
|______|| ;     (#) -.o `"=..--"_o.-; ;_|______
_/__/__/_|o;.    "      `".o|o_.--"    ;o;_/__/__/_
/__/__/__/"=._o--.        ; | ;        ; ;/__/__/__/_
_/__/__/__/"=._o--.   ;o|o;     .;o;_/__/__/_
/__/__/__/__/_"=._o.; | ;.--"o.--"/__/__/__/_
_/__/__/__/__/_"=.o|o.--""_/__/__/__/__
/__/__/__/__/__/__/__/__/__/__/___ /
***************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you  want to go? Type "left" or "right".').lower()

if choice1 == "left":
 choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
 if choice2 == "wait":
   choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, One yellow, One blue. Which colour do you choose?\n").lower()
   if choice3 == "red":
     print("It's a room full of fire. Game Over.")
   elif choice3 == "yellow":
     print("You found the treasure! you win!")
   elif choice3 == "blue":
     print("You entred a room full of beasts, Game Over.")
   else:
     print("You chose a door that doesn't exist. Game Over.")
 else:
   print("You got attacked by an angry trout. Game over.")
else:
          print("You fell into the hole. Game Over.")