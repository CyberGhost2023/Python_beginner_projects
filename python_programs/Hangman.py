import random

print('H A N G M A N')
word_list = ['python','java','kotlin','javascript']
count = 8
def repeat(random_word,word):
    global count
    letter_dict = {}
    while count:
        print()
        letter = input(''.join(word)+'\nInput a letter: ')
        if len(letter)!= 1:
            print('You should input a single letter')
        elif not(letter.islower()):
            print('It is not an ASCII lowercase letter')
        elif letter in letter_dict:
            print('You already typed this letter')
        elif letter not in random_word:
            print('No such letter in the word') 
            letter_dict[letter] = 1
            count -= 1
        else:
            for i in range(len(random_word)):
                if random_word[i]==letter:
                    word[i]=letter
                    letter_dict[letter] = 1
        if '-' not in word:
            print('\n'+''.join(word)+'\nYou guessed the word!'+'\nYou survived!')
            break
    else:
        print('You are hanged!')
random_word =random.choice(word_list)
word = ['-' for i in range(len(random_word))]
repeat(random_word,word)
