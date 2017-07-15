import random
import time

def displayinfo():
      print("you are in a land, full of dragons.in frond of you,")
      print("You see two caves in one cave the dragon is friendly")
      print("and will share his treasure with you The other dragon ")
      print("is greedy znd hungry ,and will eat you on sight.")
      print()
def choose_caves():
      print("which cave will  you go into?(1 or 2)");
      cave=int(input())
      return cave

def check_caves(choosencave):
      print("You approach the cave ...")
      time.sleep(2);
      print("it's dark and spooky.........")
      time.sleep(2);
      print("A large dragon jump out in front of you! He opens his jaws and...")
      time.sleep(4);
      friendlydragon= random.randint(1,2);
      if  choosencave==friendlydragon:
            print('gives you his treasure!\n');
      else:
            print('Gobbles you down in one bite');

playagain='Yes';
while playagain=='Yes' or playagain=='Y':
      displayinfo()
      cavenumber=choose_caves()
      check_caves(cavenumber);
      time.sleep(2)
      print("\n\nDo you want to play again?(yes or no)")
      playagain=input()
      
      

      
      
          
        


    
