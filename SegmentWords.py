__author__ = 'sharat'

import time

class Segmentation(object):
    _segmentedList=[]
    def segment(self,inputLine):
        t = Trie()
        numerical = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}

        for i in range(inputLine.__len__()):
            sentence = ""
            list = []
            stack = []

            input = inputLine[i]
            if "#" in input:
                words = input.split("#")
                string = words[1].lower()
            elif "." in input:
                words = input.split(".")
                string = words[0].lower()

            last_word_index = 0

            curNode = t.rootNode
            index = 0
            curWord = ""
            curNum = ""
            while index < string.__len__():
                char = string[index]

                if char in numerical:
                    curWord
                    curWord += char

                    if (index + 1) != string.__len__() and string[index + 1] not in numerical:
                        list.append(curWord)
                        stack.append(index)
                        curWord = ""
                    index += 1
                elif curNode.getNext(char):

                    curNode = curNode.getNext(char)

                    if t.is_a_word(curNode):
                        last_word_index = index
                        stack.append(last_word_index)

                        curWord = curNode.string

                        list.append(curWord)
                        curWord = ""

                    index += 1

                else:

                    if curWord is not None:
                        curWord = ""

                        pop_index = stack.pop()

                        index = pop_index + 1

                    curNode = t.rootNode
                if index == string.__len__():
                    if not t.is_a_word(curNode):
                        curNode = t.rootNode
                        index = stack.pop() + 1

            if curWord is not "":
                list.append(curWord)
            

            newstack = []
            prev_index = index - 1
            while list and prev_index >= 0:
                listWord = list.pop()
                start_index = prev_index - listWord.__len__() + 1

                if start_index >= 0:
                    wordIndex = string.index(listWord, start_index)

                    if not newstack or (wordIndex != -1 and wordIndex + listWord.__len__() <= prev_index + 1):
                        newstack.append(listWord)
                        prev_index = start_index - 1

            while newstack:
                sentence += newstack.pop() + " "
            sentence = sentence.rstrip()
            self._segmentedList.append(sentence)


class Node(object):
    def __init__(self, string):
        self.string = string
        self.dict = {}

    def setNext(self, char, aNode):
        self.dict[char] = aNode

    def getNext(self, char):
        if (char in self.dict):
            return self.dict[char]


class Trie(object):
    def __init__(self):
        self.rootNode = Node("")
        for word in file("words.txt"):


            curNode = self.rootNode
            for char in word.lower():

                if (not curNode.getNext(char)):

                    nxtNode = Node(curNode.string + char)
                    curNode.setNext(char, nxtNode)

                    curNode = nxtNode
                else:
                    curNode = curNode.getNext(char)
            nxtNode = None


    def is_a_word(self, Node):
        if '\n' in Node.dict:
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.clock()

    segmentedWords=Segmentation()

    N = raw_input()

    X = []

    for i in range(int(N)):
        input = raw_input()
        X.append(input)

    segmentedWords.segment(X)
    for sentence in segmentedWords._segmentedList:
        print sentence
    print time.clock() - start
