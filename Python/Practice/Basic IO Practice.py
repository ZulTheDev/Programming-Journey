#Module and Library
from colorama import Fore
from time import sleep
from os import system
#variable
user_input = input(Fore.RED + "What's your name?:" + Fore.LIGHTGREEN_EX)

#Function
def main():
    for i in range(0 , 20000):
        sleep(0.1)
        print(f"You're using: {i + int(1)} / 20,000 of packet loop transmiter")
        sleep(0.05)
        #If OS support this command
        try:
          system("clear")
        #If not use this instead.
        except:
          system("cls")
    print(user_input + ", Your power is full. Thanks for wasting your time! :P")
#output
main()