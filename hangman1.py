from images import IMAGES
import random
name=input("enter your name= ")
print("Welcome to Hangman Game ",name,"\U0001F917")
print("Try to guess the word   ")
print("_ _ _ _ _",name,"\U0001F618"," _ _ _ _ _ _ _")
def hangman():
  secret_word=choose_word()
  guessmade=""  
  turns=len(secret_word)
  print("len of the word",len(secret_word))
  while len(secret_word)>=0:
    main_word=""
    for letter in secret_word:
      if letter in guessmade:
        main_word+=letter
      else:
        main_word+="_ "
    if main_word==secret_word:
      print(main_word)
      print("YOU WON!","\U0001F929")
      break
    print("guess the word",main_word)
    guess=input("=")
    if guess in secret_word:
      guessmade+=guess
    else:
      print("enter valid letter")
      if guess not in secret_word:
        turns-=1
        if turns==len(secret_word)-1:
          print(len(secret_word)-1,"turns are left")
          print("--------------------")
          print(IMAGES[0])
        if turns==len(secret_word)-2:
          print(len(secret_word)-2,"turns are left")
          print("--------------------")
          print(IMAGES[1])
        if turns==len(secret_word)-3:
          print(len(secret_word)-3,"turns are left")
          print("--------------------")
          print(IMAGES[2])
        if turns==len(secret_word)-4:
          print(len(secret_word)-4,"turns are left")
          print("--------------------")
          print(IMAGES[3])
        if turns==len(secret_word)-5:
          print(len(secret_word)-5,"turns are left")
          print(IMAGES[4])
        if turns==len(secret_word)-6:
          print(len(secret_word)-6,"turns are left")
          print("--------------------")
          print(IMAGES[5])
        if turns==len(secret_word)-7:
          print(len(secret_word)-7,"turns are left  Hangman on his last breath")
          print("--------------------")
          print(IMAGES[6])
        if turns==len(secret_word)-8:
          print("you Are loose The Game")
          print("--------------------")
          print(IMAGES[7])
          print("The word was",secret_word,"Better Luck Next Time:(","\U0001F62A")
          break
# Time:('',"\U0001F62A")
        # break
            # [2:12 pm, 30/07/2021] Anusha Frd: import random
def load_words():
    f=open("words.txt","r")
    data=f.read().split() 
    empty=[]
    for word_list in data:
        empty.append(word_list)
    return empty
def choose_word():
    empty = load_words()
    secret_word = random.choice(empty)
    secret_word = secret_word.lower()
    return secret_word
print(choose_word())
