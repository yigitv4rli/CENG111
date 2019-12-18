def hangman(word, guesses, limit):
    wrong = 0
    num = 0
    for char in guesses:
        if char in word:
            num += word.count(char)
            if num == len(word):
                return 'win'
        else:
            wrong +=1
            if wrong > limit:
                return 'lose'
    else:
        return 'lose'
         
                
