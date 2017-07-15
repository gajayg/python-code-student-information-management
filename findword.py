import random
words=" phone  Cat Mango Dog  apple".split()
def find_word():
      wordindex=random.randint(0,len(words)-1);
     
      return words[wordindex];
def get_word(secret_word):
      findword='-'*len(secret_word);
      boo=0 
      while boo<6 :
            print(findword);
            print("Enter the string:");
            value=str(input())
            boo=boo+1;
            if len(value)!=1:
                  print("pls  .. Enter one character");
            else:
                  if value in secret_word:
                        for i in range(len(secret_word)):
                              if value==secret_word[i]:
                                    findword=findword[:i]+secret_word[i]+findword[i+1:];
                                                

                  else:
                        print("you were worng )-\n\tTry Again.......");
            if  secret_word==findword:
                   print("You won ")
                   print(findword+"  is the correct word");
                   break
            
      else:
            print(findword);
            print("Game Over You were faild");
while True:
      print("\t\t<<<<<guess the word>>>>>>")
      secretvalue=find_word();
      if secretvalue=='phone':
            print("Guess!!!!!\tIt's an  machine");
      elif secretvalue=='Cat' or secretvalue=='Dog':
            print("Guess!!! it's  the one of  the animal:");
      elif secretvalue=="Mango" or secretvalue=='apple':
            print("Guess!!! it's the one of the Fruit:")
      lsecretvalue=secretvalue.lower();
      get_word(lsecretvalue);
      print("You won thw Game")
      print("Play again Y/N:");
      value=input();
      if value=='n' or value=='N':
            break;
            


                        
                              
                        
            
      


                        
                              
                        
            
      
