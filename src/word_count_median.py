from collections import Counter
from glob import iglob


def removepunctuation(text):
    # Remove ".",",","?",":",";","-","'"
    things_to_remove = [".", ",", "?", ":", ";", "-", "'"]
    text = text.lower()
    for thing in things_to_remove:
        if thing in text:
            text = text.replace(thing, "")
    return text


def median(lst):
    sortedlst = sorted(lst)
    lstlen = len(lst)
    index = (lstlen - 1) // 2

    if lstlen % 2:
        return sortedlst[index]
    else:
        return (sortedlst[index] + sortedlst[index + 1])/2.0

folderpath = './wc_input/*.txt'
counter = Counter()
files = iglob(folderpath)
for filepath in files:
    with open(filepath) as filehandle:
        counter.update(removepunctuation(filehandle.read()).split())

sortedbyword = sorted(counter.items())

max_len = 0
for word, count in sortedbyword:
    if len(word) > max_len:
        max_len = len(word)

with open('./wc_output/wc_result.txt', 'w') as file:

    for word, count in sortedbyword:
        file.write(str(word).ljust(max_len + 10) + str(count)+'\n')

myList = []
files = iglob(folderpath)
with open('./wc_output/med_result.txt', 'w') as medfile:
    num_lines = 0
    for file in files:
        with open(file, "r") as f:
            for line in f:
                num_words = 0
                words = removepunctuation(line).split()
                num_lines += 1
                num_words += len(words)
                myList.append(num_words)
                num = format(median(myList),'.1f')
                # print(words)
                # print(num)
                # print(num_lines)
                # print(num_words)
                medfile.write(str(num)+'\n')