import sys
from random import randint
# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.


# 1 If the number the user said is less than 1 or greater than 100, it will tell them that  he/she has chosen a number that is out of play.



# 2 If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.


# 3 If the user chose a number greater than the secret number, it will let them know that it was greater.


# 4 And if the user got the secret number right, they will be informed that they have won,and how many tries that has taken them.



# 5 If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done.

name = input("What is your name? ")
rand_num = randint(1,100)
print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")
list1=[]
for i in range(8):
  ask_num=int(input('Pick a number: '))
  if ask_num==rand_num:
    print("You got it!!")
    sys.exit()
  else:
    if ask_num < 1 or ask_num > 100:
      print("Number is out of play")
    elif ask_num > rand_num:
      print("Answer is wrong lower than the number")
    elif ask_num < rand_num:
      print("Wrong,greater than the number")
  if ask_num in list1:
      print('You already tried that.')
  list1.append(ask_num)

print(f'You are a loser! You are a dissapointment! You are a failure! You are ugly! You are stupid! You should be ashamed! The number was {rand_num}')