notArrayWord = "casa"
word = []
lifes = 5

for char in notArrayWord.lower():
  word.append(char)

w = word[0]
guessedRight = []

def guess(w):
  if input("\nAdivinhe uma letra: ").lower() == w:
    print(f"{w} está na palavra!")
    return 1
  else:
    print("wrong!")
    return 0

while lifes > 0 and word != []:
  print(f"Right guesses: {guessedRight}")
  w = word[0]
  if guess(w) == 1:
    guessedRight.append(word.pop(0))
  else:
    lifes -= 1
else:
  if word == []: #elif doesn't work
    print(f"\nCONGRATULATIONS! \nYou've won this hangman game! \nWord: {guessedRight}")
  else:
    print("\nYOU LOST.")
    