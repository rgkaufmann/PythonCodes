from gtts import gTTS
import datetime
import numpy as np
import string

MASTERUSER = 'Ryan'
BASEWORDS = ['hi', 'hello', 'is']
DENOTATIONRESTRICTION = 1
User = MASTERUSER


class Knowledge_Tree:
    def __init__(self):
        try:
            tree = open('Tree.txt', 'r')
            self.__graph = eval(tree.read())
            tree.close()

            restricts = open('Restricts.txt', 'r')
            self.__restrictions = eval(restricts.read())
            restricts.close()
        except:
            self.__graph = {'hello': ['hi'], 'hi': ['hi'], 'athena': ['athena'], 'exit': ['exit']}
            self.__restrictions = {'hello': [0], 'hi': [0], 'athena': [0], 'exit': [0]}

    def update_graph(self, newword):
        synonym = input('Athena: Is ' + newword + ' similar to one that I know?\n' + User + ': ').lower()
        if synonym == 'yes':
            while synonym != '0':
                synonym = input('Athena: What word is it similar to?\n' + User + ': ').lower()
                if synonym == '0':
                    break
                elif newword in self.__graph.keys():
                    self.__graph[newword].append(synonym)
                    if synonym in BASEWORDS or newword in BASEWORDS:
                        self.__restrictions[newword].append(0)
                        if newword not in BASEWORDS:
                            BASEWORDS.append(newword)
                    else:
                        self.__restrictions[newword].append(1)
                else:
                    self.__graph[newword] = [synonym]
                    if synonym in BASEWORDS or newword in BASEWORDS:
                        self.__restrictions[newword] = [0]
                        if newword not in BASEWORDS:
                            BASEWORDS.append(newword)
                    else:
                        self.__restrictions[newword] = [1]
                if synonym not in self.__graph[synonym]:
                    self.__graph[synonym].append(newword)
                    if synonym in BASEWORDS:
                        self.__restrictions[synonym].append(0)
                    else:
                        self.__restrictions[synonym].append(1)
        elif synonym == 'no':
            self.__graph[newword] = [newword]
            self.__restrictions[newword] = [0]

        tree = open('Tree.txt', 'w')
        tree.write(str(self.__graph))
        tree.close()

        restricts = open('Restricts.txt', 'w')
        restricts.write(str(self.__restrictions))
        restricts.close()

    def simplify(self, phrase, difference=0):
        phrase = phrase.translate(str.maketrans('', '', string.punctuation))
        simplified_phrase = []
        if difference > DENOTATIONRESTRICTION:
            return False
        for word in phrase.split():
            if word in self.__graph.keys():
                if word in self.__graph[word]:
                    simplified_phrase.append(word)
                else:
                    for index in range(len(self.__graph[word])):
                        simplification = self.simplify(self.__graph[word][index], difference + self.__restrictions[word][index])
                        if simplification != False:
                            simplified_phrase.append(simplification)
                            break
            else:
                self.update_graph(word)
                print(self.__graph)
                simplified_phrase.append(self.simplify(word))
        if len(simplified_phrase) == 1:
            return simplified_phrase[0]
        else:
            return simplified_phrase


def Speak(text):
    print('Athena: ' + text)
    gTTS(text=text, lang='en').save('Response.mp3')


def Greetings():
    if LastFiveResponses == []:
        response_randomizer = np.random.randint(0, 3)
        question_randomizer = np.random.randint(0, 3)
    
        if response_randomizer == 0:
            response = 'Hi ' + User + '.'
        elif response_randomizer == 1:
            response = 'Hello ' + User + '.'
        elif response_randomizer == 2:
            current_hour = int(datetime.datetime.now().hour)
            if current_hour >= 6 and current_hour < 12:
                response = 'Good morning ' + User + '.'
            elif current_hour >= 12 and current_hour < 20:
                response = 'Good afternoon ' + User + '.'
            else:
                response = 'Good evening ' + User + '.'

        if question_randomizer == 0:
            response += ' How are you today?'
            LastFiveResponses.append(0.1)
        elif question_randomizer == 1:
            response += ' How is everything with you?'
            LastFiveResponses.append(0.1)
        elif question_randomizer == 2:
            response += ' What can I do for you right now?'
            LastFiveResponses.append(0.2)
    else:
        response = User + ", you've already said hello to me."
        response += " What can I do for you today?"
        LastFiveResponses.append(0.2)

    Speak(response)

if __name__ == '__main__':
    LastFiveResponses = []
    KT = Knowledge_Tree()
    while 1:
        TestText = KT.simplify(input(User + ': ').lower())
        if type(TestText) is list:
            TestText = ' '.join(Word for Word in TestText)
        print(TestText)
        if TestText == 'hi athena':
            Greetings()
        elif TestText == 'exit':
            quit()
        else:
            print("I haven't learned to do that yet")
        print()
