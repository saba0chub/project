from random import randint         # gamovidzaxe randint



words = [
    "house", "car", "tree", "book", "phone",
    "table", "street", "sun", "sea", "wind",
    "friend", "city", "time", "window", "door",
    "chair", "computer", "mountain", "sky", "flower"
]

lives = 6  # damatebulia skeletonistvis(momkmarebels ar enaxeba) da im miznit rom programam icodes eqvsisve sicocxlis daxarjvis mere rom tamashi sruldeba.
wordInd = randint(0, 19)  #indexebi shevcvale

secretWord = words[wordInd]

letter1 = secretWord[0]  

for i in range(len(secretWord) - 1):
    letter1 += " _"  
# gavakete cvladi gamocnobili asoebis shesanaxad
guessed_letters = [secretWord[0]]  # am listshi avtomaturad vamatebt pirvel asos

while True:
    #ganaxlebuli sityva loopshi ronm asoebi ar daikargos
    display_word = ""
    for letter in secretWord:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(" ")
    print(f"sityvaa ------->   {display_word.strip()}")

    
    a = input("\033[34mGAMOICANI ASO-----> \033[0m")
    guess = a.lower()  

    # ukve gamocnobili asoebis shemowmeba rom ar gamoerdes
    if guess in guessed_letters:
        print("ukve sheyvanilia aso!") 
        continue

    # swor asos tu gamoicnobs
    if guess in secretWord:
        guessed_letters.append(guess)  # swor guess amatebs listshi
        print(" ")

        print("\033[32mSWORIA\033[0m") # es mwvaned bewdavs kods \033[ aris dawyeba, 32m aris mwvane da boloshi racaa egaa dasruleba

    else:
        #araswor asos tu gamoicnobs
        lives -= 1  #araswor guess-ze akldeba sicocxle
        print(" ")

        print("\033[31mARASWORI ASO\033[0m") # witeli teqsti

        if lives == 0:  #tu sicocxle mivida 0amde sruldeba tamashi
            print("Game over! sityvaa:", f"\033[34m{secretWord}\033[0m")
            break

    #vamowmebt tu yvela aso gamocnobilia
    word_complete = True  
    for letter in secretWord:
        if letter not in guessed_letters:
            word_complete = False
            break  
    if word_complete:
        print(" ")
        print("mogebulia! sityvaa:", f"\033[34m{secretWord}\033[0m")
        break
    if lives == 6:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           ')
        print('|            ')
        print('|            ')
        print('|')
        print('|')
    elif lives == 5:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           O')
        print('|            ')
        print('|            ')
        print('|')
        print('|')
    elif lives == 4:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           O')
        print('|           |')
        print('|            ')
        print('|')
        print('|')
    elif lives == 3:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           O')
        print('|          /|')
        print('|            ')
        print('|')
        print('|')
    elif lives == 2:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           O')
        print('|          /|\\')
        print('|            ')
        print('|')
        print('|')
    elif lives == 1:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           O')
        print('|          /|\\')
        print('|          / ')
        print('|')
        print('|')
    elif lives == 0:
        print(" ")
        print(" ")
        print('=============')
        print('|           |')
        print('|           |')
        print('|           O')
        print('|          /|\\')
        print('|          / \\')
        print('|')
        print('|')