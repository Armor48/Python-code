def typing():
    import random
    import os
    clear = lambda:os.system('cls')

    sentence = "the quick brown fox jumps over the lazy dog"

    words = ["apple", "banana", "chair", "dog", "elephant", "friend", "guitar", "happy", "internet", "jacket", "kite", "love", "mountain", "notebook", "ocean", "purple", "quiet", "rainbow", "sunny", "tiger", "umbrella", "violet", "water", "xylophone", "yellow", "zebra","bird", "book", "camera", "coffee", "dance", "dolphin", "ear", "fire", "house", "ink", "jeans", "key", "lion", "monkey", "night", "pencil", "queen", "snake", "turtle", "vase", "whistle", "yoga", "zoo", "ball", "cat", "desk", "egg", "flower", "garden", "hat", "ice", "jam", "lemon", "orange", "sun", "tree"]

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    up_row = ['q','w','e','r','t','y','u','i','o','p']
    hm_row = ['a','s','d','f','g','h','j','k','l',';']
    lw_row = ['z','x','c','v','b','n','m']

    num = ['1','2','3','4','5','6','7','8','9','0']

    loop=True
    name = input("Enter your name:- ").capitalize()
    point = 0

    print("What do you want to practice:\n",
            "1. Sentence\n",
            "2. Random word\n",
            "3. Alphabet\n",
            "4. Upper row\n",
            "5. Home row\n",
            "6. Lower row\n",
            "7. Numeric pad",)
    opt = int(input())

    if opt == 1:
        print('Start writing : "the quick brown fox jumps over the lazy dog"')
        while loop:
            typ = input()
            
            if typ == "exit":
                loop = False
            else:
                if typ == sentence:
                    point = point + 10
                else:
                    print("...Retry...".center(60))
                    point = point - 5

    if opt == 2:
        print('Start Your Practice:')
        while loop:
            display = random.choice(words)
            print(display)
            typ = input()
            clear()
            print("WORDS".center(60))
            print()
            if typ == "exit":
                loop = False
            else:
                if typ == display:
                    print("...Correct...".center(60))
                    point = point + 5
                else:
                    print("...Retry...".center(60))
                    point = point - 2

    if opt == 3:
        print('Start Your Practice:')
        while loop:
            display = random.choice(alphabet)
            print(display)
            typ = input()
            clear()
            print("ALPHABET".center(60))
            print()

            if typ == "exit":
                loop = False
            else:
                if typ == display:
                    print("...Correct...".center(60))
                    point = point + 2
                else:
                    print("...Retry...".center(60))
                    point = point - 1

    if opt == 4:
        print('Start Your Practice:')
        while loop:
            display = random.choice(up_row)
            print(display)
            typ = input()
            clear()
            print("UPPER ROW".center(60))
            print()

            if typ == "exit":
                loop = False
            else:
                if typ == display:
                    print("...Correct...".center(60))
                    point = point + 2
                else:
                    print("...Retry...".center(60))
                    point = point - 1

    if opt == 5:
        print('Start Your Practice:')
        while loop:
            display = random.choice(hm_row)
            print(display)
            typ = input()
            clear()
            print("HOME ROW".center(60))
            print()

            if typ == "exit":
                loop = False
            else:
                if typ == display:
                    print("...Correct...".center(60))
                    point = point + 2
                else:
                    print("...Retry...".center(60))
                    point = point - 1
                    
    if opt == 6:
        print('Start Your Practice:')
        while loop:
            display = random.choice(lw_row)
            print(display)
            typ = input()
            clear()
            print("LOWER ROW".center(60))
            print()

            if typ == "exit":
                loop = False
            else:
                if typ == display:
                    print("...Correct...".center(60))
                    point = point + 2
                else:
                    print("...Retry...".center(60))
                    point = point - 1

    if opt == 7:
        print('Start Your Practice:')
        while loop:
            display = random.choice(num)
            print(display)
            typ = input()
            clear()
            print("NUMERIC PAD".center(60))
            print()

            if typ == "exit":
                loop = False
            else:
                if typ == display:
                    print("...Correct...".center(60))
                    point = point + 2
                else:
                    print("...Wrong...".center(60))
                    point = point - 1

    print(name,"Your Score is: ",point)
typing()