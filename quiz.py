import random

def popword(wordlist,worddict):
    random_index=random.randrange(len(wordlist))
    word=wordlist.pop(random_index)
    defn=worddict.get(word)
    return word, defn

def getWord(rawstring):
    word, defn = rawstring.split(',',1)
    return word, defn

fh = open("vocabulary_list.csv",'r')
wdlist=fh.readlines()
wdlist.pop(0)  # To remove the first line
wdset=set(wdlist)
fh = open("Vocabulary_set",'w')
fh.writelines(wdset)

dic=dict()
for i in wdset:
    word, defn = getWord(i)
    dic[word]=defn

while True:
    wdlist = list(dic)
    choicelist=[]
    for i in range(4):
        word,defn = popword(wdlist,dic)
        choicelist.append(defn)
    random.shuffle(choicelist)
    print(word,"-----")
    for idx, choice in enumerate(choicelist):
        print(idx+1,"|>", choice)
    choice=int(input("1,2,3,4 or 0 to exit: "))
    if choicelist[choice-1] == defn:
        print("\n Correct")
    elif choice == 0:
        exit()
    else:
        print("Incorrect")
