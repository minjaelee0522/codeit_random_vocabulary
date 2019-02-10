from random import randint

in_file = open("vocabulary.txt", "r")
dict = {}

for line in in_file:
    data = line.strip().split(" : ")
    english_word = data[0]
    korean_meaning = data[1]
    dict[korean_meaning] = english_word

keys = list(dict.keys())

while True:
    random_num = randint(0, len(keys)-1)
    korean_meaning = keys[random_num]
    english_word = dict[korean_meaning]
    guess = input("%s : " % korean_meaning)
    if guess == english_word:
        print("맞았습니다!")
    elif guess == "q":
        break
    else:
        print("아쉽습니다. 정답은 %s입니다." % english_word)

in_file.close()
