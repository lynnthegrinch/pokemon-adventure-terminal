# pkmn adv
# codedex checkpoint

# importing random module
import random
# printing intro

print("█▀█ █▀█ █▄▀ █▀▀ █▀▄▀█ █▀█ █▄░█   ▄▀█ █▀▄ █░█ █▀▀ █▄░█ ▀█▀ █░█ █▀█ █▀▀")
print("█▀▀ █▄█ █░█ ██▄ █░▀░█ █▄█ █░▀█   █▀█ █▄▀ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ██▄")
pkmn_trn = input("whats your name?  ")
pkm = 0

answ = input("hi " + pkmn_trn + " are you ready to pick your starter? Yes or no")

if answ == 'yes'or answ == 'y':
  print("pick your starter")
  pkm = pkm +1
  starter = input("a. turtwig b. piplup c. chimchar")
  if starter == 'a' or starter == 'turtwig': #turtwig
    print("nice choice!")
    print("do you wanna give turtwig a nickname?")
    turtwig1 = input("yes or no")
    if turtwig1 == 'yes'or turtwig1 == 'y':
        turtwignick = input("what name do you want to give it?")
        print("your turtwig is now called" + turtwignick + " congrats!")
    elif turtwig1 == 'no' or turtwig1 == 'n':
        print("congrats for picking turtwig")
    else:
        print("try again later")
  elif starter == 'b' or starter == 'piplup': #piplup
    print("nice choice!")
    print("do you wanna give piplup a nickname?")
    pip1 = input("yes or no")
    if pip1 == 'yes'or pip1 == 'y':
        pipni = input("what name do you want to give it?")
        print("your piplup is now called" + pipni + " congrats!")
    elif pip1 == 'no' or pip1 == 'n':
        print("congrats for picking piplup")
    else:
        print("bye")
  elif starter == 'c' or starter == 'chimchar': #chimchar
    print("nice choice!")
    print("do you wanna give chimchar a nickname?")
    chim1 = input("yes or no")
    if chim1 == 'yes'or chim1 == 'y':
        chimn = input("what name do you want to give it?")
        print("your chimchar is now called" + chimn + " congrats!")
    elif chim1 == 'no' or chim1 == 'n':
        print("congrats for picking chimchar")
    else:
        print("goodbye")
  else:
      print("you are unfunny")
else:
    print("bye")



print("starter or not starter, we should go on an adventure") #adv
adv = input("let's go? yes or no")
while adv == 'yes'or adv == 'y':
    num =  random.randint(1, 4)
    if num == 1: #rattata
        print("you found a rattata, what do you want to do")
        rat = input("catch? yes or no")
        if rat == 'yes' or rat == 'y':
            mum = random.randint(1, 2)
            if mum == 1:
                print("you caught a rattata!")
                pkm = pkm +1
            else:
                print("noo, rattata ran away")
        else:
            print("want to go again?")
            ans_2 = input('yes or no')
            if ans_2 == 'no':
                break
                print("you have" + pkm)
    elif num == 2: #spheal
         print("you found a spheal, what do you want to do")
         sp = input("catch? yes or no")
         if sp == 'yes' or sp == 'y':
            rum = random.randint(1, 2)
            if rum == 1:
                print("you caught a spheal!")
                pkm = pkm +1
            else:
                print("noo, spheal ran away")
         else:
            print("want to go again?")
            ans_3 = input('yes or no')
            if ans_3 == 'no':
                break
                print("you have" + pkm)
    elif num == 3: #snorlax
         print("you found a snorlax, what do you want to do")
         sn = input("catch? yes or no")
         if sn == 'yes' or sn == 'y':
            rur = random.randint(1, 2)
            if rur == 1:
                print("you caught a snorlax!")
                pkm = pkm +1
            else:
                print("noo, snorlax ran away")
         else:
            print("want to go again?")
            ans_3 = input('yes or no')
            if ans_3 == 'no' or ans_3 == 'n':
                break
                print("you have" + pkm)
    else: #ditto
         print("you found a ditto, what do you want to do")
         di = input("catch? yes or no")
         if di == 'yes' or di == 'y':
            nun = random.randint(1, 2)
            if nun == 1:
                print("you caught a ditto!")
                pkm = pkm +1
            else:
                print("noo, ditto ran away")
         else:
            print("want to go again?")
            ans_4 = input('yes or no')
            if ans_4 == 'no'or ans_4 == 'n':
                break
                print("you have" + pkm)
else:
    print("bye")

