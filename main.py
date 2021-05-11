import random

print("H A N G M A N")
while True:
    print('Type "play" to play the game, "exit" to quit:')
    answer = input()
    if answer == "play":
        word_list = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(word_list)
        long = int(len(word))
        tab_cher = ""
        new_word = "-" * long
        new_word2 = new_word
        conter = -1
        test = 8
        while test > 0:
            print("")
            print(new_word2)
            x = input("Input a letter: ")
            if x == " ":
                print("You should input a single letter")
                continue
            if len(x) != 1:
                print("You should input a single letter")
                continue
            if not x.islower():
                print("Please enter a lowercase English letter")
                continue
            if tab_cher.find(x) >= 0:
                print("You've already guessed this letter")
                continue
            if word.find(x) >= 0:
                where = word.find(x)
                new_word2 = new_word2[0:where] + x + new_word2[where+1:len(new_word2)+1]
                tab_cher += str(x)
                if word.find(x, where + 1) > where:
                    where = word.find(x, where + 1)
                    new_word2 = new_word2[0:where] + x + new_word2[where + 1:len(new_word2) + 1]
            else:
                test -= 1
                print("That letter doesn't appear in the word")
                tab_cher += str(x)
            if new_word2.find("-") < 0:
                print("You guessed the word!")
                print("You survived!")
                break
        if new_word2.find("-") > 0 or test == 0:
            print("You lost!")
    if answer == "exit":
        break
    else:
        continue
