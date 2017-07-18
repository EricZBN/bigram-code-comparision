import string
import sys


def readFile(file_in):
    f = open(file_in)
    contents = f.read()
    f.close()
    return contents


def cleanText(string_in):
    exclude = set(string.punctuation)
    contents_no_punct = ''.join(ch for ch in string_in if ch not in exclude)
    stringout = contents_no_punct.lower().split()
    return stringout


def createBigramList(string_in):
    bigram_list = []
    for i in range(len(string_in) - 1):
        bigram_list.append((string_in[i], string_in[i+1]))
    return bigram_list


def createListSet(list_in):
    output_list = list(set(list_in))
    return output_list


def bigramCounts(bgramList):
    resultsList = []
    listSet = createListSet(bgramList)
    for bgTuple in listSet:
        bgCount = 0
        for j in range(len(bgramList)):
            if(bgTuple == bgramList[j]):
                bgCount = bgCount + 1
        resultsList.append((bgTuple, bgCount))
    return resultsList


def brgramHistogram(list_in):
    max_word1, max_word2 = 0, 0
    for bgTuple in list_in:
        max_word1 = max(max_word1, len(bgTuple[0][0]))
        max_word2 = max(max_word2, len(bgTuple[0][1]))

    for i in range(len(list_in)):
        print("%-*s %-*s" % (max_word1, list_in[i][0][0], max_word2, list_in[i][0][1]), end="", flush=True)
        print(" |", end="", flush=True)
        for j in range(list_in[i][1]):
            print("*", end="", flush=True)
        print()


def bigramMain():
    try:
        file_in = sys.argv[1]
    except:
        print("Please run the program again with an input file.")
        return False

    bigramResults = bigramCounts(createBigramList(cleanText(readFile(file_in))))
    brgramHistogram(bigramResults)
    return True


if __name__ == "__main__":
    bigramMain()

