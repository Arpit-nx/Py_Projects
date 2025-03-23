import random as rd
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

word_list = [
    "no", "pet", "run", "code", "hello", "world", "banana", "computer", "generate", "randomly",
    "fox", "jump", "high", "cloudy", "weather", "forecast", "beautiful", "sunny", "day", "night",
    "apple", "tree", "house", "car", "bicycle", "football", "basketball", "volleyball", "tennis",
    "python", "java", "cplus", "ruby", "swift", "kotlin", "javascript", "typescript", "go",
    "machine", "learning", "artificial", "intelligence", "natural", "language", "processing",
    "data", "science", "analytics", "visualization", "statistics", "mathematics", "physics",
    "chemistry", "biology", "zoology", "botany", "ecology", "environment", "conservation",
    "music", "art", "dance", "theater", "film", "photography", "literature", "poetry",
    "history", "geography", "politics", "economy", "business", "management", "marketing",
    "sales", "finance", "accounting", "law", "medicine", "healthcare", "nursing",
    "education", "teaching", "learning", "training", "development", "growth", "success",
    "happiness", "joy", "love", "peace", "harmony", "freedom", "justice", "equality",
    "friendship", "family", "relationship", "communication", "teamwork", "leadership",
    "innovation", "creativity", "imagination", "inspiration", "motivation", "encouragement",
    "support", "help", "care", "kindness", "empathy", "compassion", "forgiveness",
    "patience", "perseverance", "determination", "hardwork", "dedication", "commitment",
    "responsibility", "accountability", "transparency", "honesty", "integrity", "authenticity"
]

end_of_game = False
Chosen_word = rd.choice(word_list)
word_length = len(Chosen_word)

word = []
for i in range(word_length):
    word += "_"
    #word.append("_")

print(f"{word}\n")

lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #if we apply the variable of for loop with range...it moves as index or number or position...
    #if we apply the variable of for loop with the list directly...it moves from one item in the list to another...
    for position in range(word_length):
        letter = Chosen_word[position]
        if letter == guess:
            word[position] = guess
    if guess not in Chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Wrong choice, lives left = {lives}")
        if lives == 0:
            end_of_game = True
            print("Your man is hanged to death👿👿...\nYou lost!!!")
            print(f'Pssst, the solution was {Chosen_word}.')
    print(f"{' '.join(word)}")

    if "_" not in word:
        end_of_game = True
        print("You won")