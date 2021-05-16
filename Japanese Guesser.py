from jap_chars.jap_chars import new_kanji, Hiragana, Katakana
import pickle
import random

#loading the kanji array
infile1 = open('D:\\projects\\VScode\\Japanese Trainer\\jap_chars\\Kanji_lvls.pickle','rb')
kanji_lvls = pickle.load(infile1)

#loading the score array
infile2 = open('D:\\projects\\VScode\\Japanese Trainer\\score.pickle','rb')
score_array = pickle.load(infile2)

categoryHKK_score = 0
categoryHKK_letter = ''
external_exiter = 0
while True:
    chars = ''
    shuffled_array = []
    #shuffler function
    def HiKa_CharArrayGetter(charGroup,arrayName):
        for i in range(0,len(arrayName),2):
            if arrayName[i] == charGroup:
                guesser_array = arrayName[i+1]
                random.shuffle(guesser_array)
                return guesser_array

    #shuffling the array
    while True:
        guesser_choice = input('Enter guessing choice (Hiragana/Katakana/Kanji/Exit): ').lower()
        if guesser_choice == 'hiragana':
            chars = input('Select a Char group (vowel/k/s/t/h/n/m/r/g/z/d/b/p/y): ')
            categoryHKK_letter = chars
            shuffled_array = HiKa_CharArrayGetter(chars,Hiragana)
            break

        if guesser_choice == 'katakana':
            chars = input('Select a Char group (vowel/k/s/t/h/n/m/r/g/z/d/b/p/y): ')
            categoryHKK_letter = chars
            categoryHKK_score = 1
            shuffled_array = HiKa_CharArrayGetter(chars,Katakana)
            break

        if guesser_choice == 'kanji':
            difficulty = int(input('Select a difficulty (1-10):'))
            categoryHKK_letter = int(difficulty)
            categoryHKK_score = 2
            shuffled_array = kanji_lvls[difficulty-1]
            random.shuffle(shuffled_array)
            break

        if guesser_choice == 'exit':
            exit()

    #scoring array
    #getting the category 
    score_category = 0
    for i in range(len(score_array[categoryHKK_score])):
        if(score_array[categoryHKK_score][i]==categoryHKK_letter):
            score_category = i
        pass

    #showing the Hira or kata array
    if categoryHKK_score == 0 or categoryHKK_score == 1:
        print('Previous Highscore for this category is :' + str(score_array[categoryHKK_score][score_category][1]))
        score_total = 0
        for i in range(len(shuffled_array)):
            question = shuffled_array[i][1] + ': '
            answer = input(question)
            if answer.lower() == shuffled_array[i][0].lower():
                print('Correct! ')
                score_total = score_total +10
            else:
                print('Wrong! ')
        if score_total > score_array[categoryHKK_score][score_category][1]:
            score_array[categoryHKK_score][score_category][1] = score_total
        print('Your score is :' + str(score_total))

    #showing the Kanji array
    #TODO
    #Have a loop for pronounciation and search for it, so that it doesn't order by 3
    #
    if categoryHKK_score == 2:
        print('Previous Highscore for this category is: ' + str(score_array[categoryHKK_score][score_category][1]))
        score_total = 0
        for i in shuffled_array:
            question = i.kanjiChar + ': '
            answer = input(question).lower()
            correctness = 0
            for j in i.pronounciation:
                if answer == j:
                    correctness = 1

            if correctness==1:
                print('Correct!')
                score_total = score_total+ 10
            else:
                print('Wrong!')

        if score_total > score_array[categoryHKK_score][score_category][1]:
            score_array[categoryHKK_score][score_category][1] = score_total
        print('Your score is: ' + str(score_total))
    
#returning the score array to be saved
    output = open('D:\\projects\\VScode\\Japanese Trainer\\score.pickle','wb')
    pickle.dump(score_array,output)
    output.close()