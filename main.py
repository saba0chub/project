from random import randint         # gamovidzaxe randint

words = [
    "house", "car", "tree", "book", "phone",
    "table", "street", "sun", "sea", "wind",         #random sityvebi romelic chemi mogoniuli araa
    "friend", "city", "time", "window", "door",
    "chair", "computer", "mountain", "sky", "flower"
]



wordInd = randint(0, 20)    # am cvlads mieniweba random cifri 0-20 chatvlit romelic gamoieneba index ad

secretWord = words[wordInd]     # am cvlads wordInd is daxmarebit eniweba random sityva



letter1 = secretWord[0] # am cvlads eniweba random sityvis pirveli aso (chamoxrchobanashi pirveli aso xo cnobilia)


for i in range(len(secretWord)- 1):
    letter1 += " _"                     # pirveli asos garda yvela asos magivrad iwereba _




while True:
    print(f"sityvaa ------->   {letter1}")
    a = input("gamoicani aso ----> ")   # sheuchereblad gekitxeba asos sheyvanas

