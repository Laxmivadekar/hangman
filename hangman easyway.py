import random
def hangman():
    list_of_words=['python','java','hangman','laptop','wire','network','mobile phone','waterbottle']
    word=random.choice(list_of_words)
    turns=10      #we have 10 turns and it will be decrease for every time we choose wrong assumptions
    guessmade=''  #it is user made user will be guessing the word
    while len(word)>0:
        main_word=''  #which word we have,creating the user or which word we want to show the user
        missed=0 #for missing the variable
        valid_entry=set('abcdefghijklmnopqrstuvwxyz') #it will creates all the letters in the set disecular formate(means it will create the clumsly not intthe order all letter are)
        for letter in word: 
            if letter in guessmade:
                main_word+=letter
            else:
                main_word+='_ '
        if main_word==word:
            print(main_word)
            print('you won!!!!!!!!!!')
            break
        print('guess the words ',main_word)
        guess=input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print('enter the valid charachters')
            guess=input()
        if guess not in word:
            turns-=1
            if turns==9:
                print('9 turns left!!!')
                print('_ _ _ _ _ _ _ _ _')
            if turns==8:
                print('8 turns left!!!')
                print('        0       ') #it will create the head of the hangman
            if turns==7:
                print('7 turns left!!!')
                print('        0       ')
                print('        |       ')  #it will create body of the hangman
            if turns==6:
                print('6 turns left!!!')
                print('        0       ')
                print('        |       ')  #it will create body of the hangman
                print('       /        ')  #it will gives the left leg of the hang man
            if turns==5:
                print('5 turns left!!!')
                print('        0       ')
                print('        |       ')  #it will create body of the hangman
                print('       / \      ')  
            if turns==4:
                print('4 turns left!!!')
                print('      \ 0       ') #it will create left hand
                print('        |       ')  
                print('       / \      ')  
            if turns==3:
                print('3 turns left!!!')
                print('      \ 0 /      ') #this condition will create both the hands
                print('        |       ')  
                print('       / \      ')   
            if turns==2:
                print('2 turns left!!!')
                print('      \ 0 / |       ') #it will create the rope
                print('        |       ')  
                print('       / \      ') 
            if turns==1:
                print('only 1 turn left!!! for the last breath')
                print('      \ 0 /_|       ') #it will create the rope aside tied with neck
                print('        |       ')  
                print('       / \      ') 
            if turns==0:
                print('you lose the game')
                print('a good man died   ')  
                print('        0 _|       ') #it will create the rope aside tied with neck
                print('      / | \      ')  
                print('       / \      ') 
                break

name=input('enter the player name: ')
print('welcome',name,'!')
print('_ _ _ _ _ _ _ _')
print('try to guess the word in less than 10 attenpts')
hangman()
