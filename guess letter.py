import random

word=["car","mottor","truck","vichcle"]

computer=random.choice(word)

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


print(f"computer chose {computer}")
length= len(computer)
display=[]
live=6
for _ in range(length):
  display+="_"
end_of_game= False
while not end_of_game:
  user=input("Guess the letter: ").lower()
  print(f"you chose {user}")
  for position in range(length):
    letter=computer[position]
    if letter== user:
      display[position]=letter
  print(display)  
  if user not in computer:
    live-=1
    if live==0:
      end_of_game=True
      print("You lose")
  
  if "_" not in display:
    end_of_game=True
    print("You Win!")
  print(stages[live])
