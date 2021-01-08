# Function defintion here
import sys


class Encrpyt():

    def __init__(self, shift, message):
        self.shift = shift
        self.message = message

    def lowerCaseShift(self, character):
        c = ord(character) + shift

        if c > 122:
            c = c - 122 + 96
            return chr(c)
        else:
            return chr(ord(character) + shift)

    def upperCaseShift(self, character):
        c = ord(character) + shift

        if c > 90:
            c = c - 90 + 64
            return chr(c)
        else:
            return chr(ord(character) + shift)

    def encrypt(self, message):
        secondMessage = ""

        for mes in message:
            if mes >= 'a' and mes <= 'z':
                secondMessage += self.lowerCaseShift(mes)
            elif mes >= 'A' and mes <= 'Z':
                secondMessage += self.upperCaseShift(mes)
            else:
                secondMessage += mes

        return secondMessage


class Decrypt():

    def __init__(self, shift, message):
        self.shift = shift
        self.message = message

    def lowerCaseShift(self, character):
        c = ord(character) - self.shift

        if c < 97:
            c = 122 - (96 - c)
            return chr(c)
        else:
            return chr(ord(character) - self.shift)

    def upperCaseShift(self, character):
        c = ord(character) - self.shift

        if c < 65:
            c = 90 - (64 - c)
            return chr(c)
        else:
            return chr(ord(character) - self.shift)

    def decrypt(self, message):
        secondMessage = ""

        for mes in message:
            if mes >= 'a' and mes <= 'z':
                secondMessage += self.lowerCaseShift(mes)
            elif mes >= 'A' and mes <= 'Z':
                secondMessage += self.upperCaseShift(mes)
            else:
                secondMessage += mes

        return secondMessage


class CeaserCipher:

    def __init__(self, shift, user, option):
        self.shift = shift
        self.user = user
        self.option = option

    def writeToFile(self, word):
        output.write(word)

    def readArrayofWords(self, string):
        for word in string:
            if option == 'encrypt':
                foo = Encrpyt(shift, word)
                x = foo.encrypt(word)
                self.writeToFile(x)
            elif option == 'decrypt':
                foo = Decrypt(shift, word)
                x = foo.decrypt(word)
                self.writeToFile(x)

    def readFile(self):

        try:
            reader = open('input.txt', 'r')
            line = reader.readline()

            while line != '':

                self.readArrayofWords(line)
                line = reader.readline()

        except:
            print("Error reading file. File doesn't exit ")
            exit()

        finally:
            reader.close()

    def validate(self):
        if shift < 1 or shift > 26:
            print(str(shift) + " is not a valid shift")
            exit()


output = open('output.txt', 'w')

option = "encrpyt"


if len(sys.argv) > 3:
    user = str(sys.argv[1])
    shift = int(sys.argv[2])
    option = str(sys.argv[3])

    main = CeaserCipher(shift, user, option)
    CeaserCipher.validate(main)
    main.readFile()

elif len(sys.argv) > 2:
    user = str(sys.argv[1])
    option = str(sys.argv[2])
    shift = 1
    main = CeaserCipher(shift, user, option)
    CeaserCipher.validate(main)
    while shift <= 26:
        CeaserCipher.writeToFile(main, "\n\n\n\n\n")
        string = "Shift = " + str(shift)
        CeaserCipher.writeToFile(main, string)
        CeaserCipher.writeToFile(main, "\n\n")
        main.readFile()
        shift += 1
