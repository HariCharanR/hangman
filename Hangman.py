import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
answers = [
    "Lewis Hamilton",
    "Max Verstappen",
    "Valtteri Bottas",
    "Charles Leclerc",
    "Carlos Sainz",
    "Lando Norris",
    "Daniel Ricciardo",
    "Pierre Gasly",
    "Fernando Alonso",
    "Esteban Ocon",
    "Sebastian Vettel",
    "Lance Stroll",
    "Yuki Tsunoda",
    "Kimi Räikkönen",
    "Antonio Giovinazzi",
    "Mick Schumacher",
    "Nikita Mazepin",
    "George Russell",
    "Nicholas Latifi",
    "Nikita Mazepin"
]

print(logo)
curr_ans = str(random.choice(answers)).lower()

number_of_spaces = 0
for ch in curr_ans:
    if ch == ' ':
        number_of_spaces+=1
print(number_of_spaces)
number_of_guesses = len(stages)
word = []
for i in range(0,len(curr_ans)):
    word.append(' ')
print(f'current answer : {word}')
flag=0
req = len(curr_ans)
while number_of_guesses != 0:
    flag = 0
    print(f'number of guesses left :{number_of_guesses}')
    guess = input("Guess the letters of the final word:")
    for i, ch in enumerate(curr_ans):
        if ch == guess:
            if word[i] == guess:
                flag = 2
                break
            word[i] = guess
            flag = 1
    if flag == 1:
        print("Correct!")
        req -= curr_ans.count(guess)
    elif flag == 2:
        print("Already Guessed!")
    else:
        print("Wrong!")
        number_of_guesses -= 1
        print(stages[number_of_guesses])
    print(f'current answer : {word}')

    if req == 0:
        break



if req != 0:
    print("You have not guessed the final word")
else:
    print("You have guessed the final word")



