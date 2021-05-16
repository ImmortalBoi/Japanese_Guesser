import pickle
#creating the kanji class
class new_kanji:
    def __init__(self, difficulty,kanjiChar,pronounciation,id):
        self.difficulty = difficulty
        self.kanjiChar = kanjiChar
        self.pronounciation = pronounciation
        self.id = id
    def __repr__(self): 
        return '(Difficulty: % s ,Kanji: %s , Pronounciation: %s , ID: %s)' % (self.difficulty,self.kanjiChar,self.pronounciation,self.id)

Hiragana = [
    'vowel',[['a','あ'],['i','い'],['u','う'],['e','え'],['o','お']],
    'k',[['ka','か'],['ki','き'],['ku','く'],['ke','け'],['ko','こ']],
    's',[['sa','さ'],['shi','し'],['su','す'],['se','せ'],['so','そ']],
    't',[['ta','た'],['chi','ち'],['tsu','つ'],['te','て'],['to','と']],
    'n',[['na','な'],['ni','に'],['nu','ぬ'],['ne','ね'],['no','の'],['n','ん']],
    'h',[['ha','は'],['hi','ひ'],['fu','ふ'],['he','へ'],['ho','ほ']],
    'm',[['ma','ま'],['mi','み'],['mu','む'],['me','め'],['mo','も']],
    'r',[['ra','ら'],['ri','り'],['ru','る'],['re','れ'],['ro','ろ']],
    'g',[['ga','が'],['gi','ぎ'],['gu','ぐ'],['ge','げ'],['go','ご']],
    'z',[['za','ざ'],['ji','じ'],['zu','ず'],['ze','ぜ'],['zo','ぞ']],
    'd',[['da','だ'],['dji','ぢ'],['dzu','づ'],['de','で'],['do','ど']],
    'b',[['ba','ば'],['bi','び'],['bu','ぶ'],['be','べ'],['bo','ぼ'],['v','ゔ']],
    'p',[['pa','ぱ'],['pi','ぴ'],['pu','ぷ'],['pe','ぺ'],['po','ぽ']],
    'y',[['ya','や'],['yu','ゆ'],['yo','よ']]
]

Katakana = [
    'vowel',[['a','ア'],['i','イ'],['u','ウ'],['e','エ'],['o','オ']],
    'k',[['ka','カ'],['ki','キ'],['ku','ク'],['ke','ケ'],['ko','コ']],
    's',[['sa','サ'],['shi','シ'],['su','ス'],['se','セ'],['so','ソ']],
    't',[['ta','タ'],['chi','チ'],['tsu','ツ'],['te','テ'],['to','ト']],
    'n',[['na','ナ'],['ni','ニ'],['nu','ヌ'],['ne','ネ'],['no','ノ'],['n','ン']],
    'h',[['ha','ハ'],['hi','ヒ'],['fu','フ'],['he','ヘ'],['ho','ホ']],
    'm',[['ma','マ'],['mi','ミ'],['mu','ム'],['me','メ'],['mo','モ']],
    'r',[['ra','ラ'],['ri','リ'],['ru','ル'],['re','レ'],['ro','ロ']],
    'g',[['ga','ガ'],['gi','ギ'],['gu','グ'],['ge','ゲ'],['go','ゴ']],
    'z',[['za','ザ'],['ji','ジ'],['zu','ズ'],['ze','ゼ'],['zo','ゾ']],
    'd',[['da','ダ'],['dji','ヂ'],['dzu','ヅ'],['de','デ'],['do','ド']],
    'b',[['ba','バ'],['bi','ビ'],['bu','ブ'],['be','ベ'],['bo','ボ'],['v','ヴ']],
    'p',[['pa','パ'],['pi','ピ'],['pu','プ'],['pe','ペ'],['po','ポ']],
    'y',[['ya','ヤ'],['yu','ユ'],['yo','ヨ']]
]

if __name__ == "__main__": 
    filename1 = 'D:\projects\VScode\Japanese Trainer\jap_chars\Kanji_lvls.pickle'
    filename2 = 'D:\projects\VScode\Japanese Trainer\jap_chars\KanjiID.pickle'
    infile1 = open(filename1,'rb')
    kanji_lvls = pickle.load(infile1)
    infile2 = open(filename2,'rb')
    kanji_ID = pickle.load(infile2)
    external_exiter = 0
    while external_exiter == 0:
        exiter = 0
        answer = input("What do you want to do? (Insert/Delete/Exit/Display): ").lower()

        #on wanting to insert Kanji into array
        if answer == 'insert':
            while exiter != 1:
                #Inputting the class parameters
                hard = int(input("Insert difficulty: "))
                kanji = input("Insert kanji: ")
                saying = []
                
                #Creating the cancel case
                if hard == 'cancel' or kanji == 'cancel':
                    exiter = 1
                    break

                #Creating the romaji 
                times = int(input('How many pronounciations do you want to put ?: '))
                for i in range(times):
                    romaji = input("Insert pronounciation: ")
                    if romaji == 'cancel':
                        break
                    saying.append(romaji)
                kanji_lvls[int(hard)-1].append(new_kanji(hard,kanji,saying,kanji_ID))
                kanji_ID += 1
                cont = input("Do you want to insert another character ? (y/n): ")
                if cont == 'n':
                    exiter = 1
            print(kanji_lvls)

        #On wanting to delete an object
        elif answer == 'delete':
            difficulty = int(input('Insert Difficulty: '))
            kanID = int(input('Insert Kanji ID: '))
            for index, item in enumerate(kanji_lvls[difficulty-1]):
                if item.id == kanID:
                    kanji_lvls[difficulty-1].pop(index)
                    break
            else:
                index = -1
            print(kanji_lvls)

        #Displaying the kanji array
        elif answer == 'display':
            print(kanji_lvls)

        #Exiting the program
        elif answer == 'exit':
            external_exiter = 1
    #Externally saving the program

    output = open(filename1,'wb')
    pickle.dump(kanji_lvls,output)
    output.close()

    output = open(filename2,'wb')
    pickle.dump(kanji_ID,output)
    output.close()
