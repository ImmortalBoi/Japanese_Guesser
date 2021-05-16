import pickle
#creating score_array
#first index (hiragana)
#second index (katakana)
#third index (kanji)
score_array = [
    [['vowel',0],
    ['k',0],
    ['s',0],
    ['t',0],
    ['n',0],
    ['h',0],
    ['m',0],
    ['r',0],
    ['g',0],
    ['z',0],
    ['d',0],
    ['b',0],
    ['p',0],
    ['y',0]]
    ,
    [['vowel',0],
    ['k',0],
    ['s',0],
    ['t',0],
    ['n',0],
    ['h',0],
    ['m',0],
    ['r',0],
    ['g',0],
    ['z',0],
    ['d',0],
    ['b',0],
    ['p',0],
    ['y',0]]
    ,
    [[1,0],
    [2,0],
    [3,0],
    [4,0],
    [5,0],
    [6,0],
    [7,0],
    [8,0],
    [9,0],
    [10,0],
    ]
]

output = open('score.pickle','wb')
pickle.dump(score_array,output)
output.close()