from socket import *
import os

class TCPclient:
    def __init__(self):
        pass

    def send(self, serverName='Chris', msg='message.txt', serverPort=16000):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))  # establish the TCP connection
        file1 = open(msg, "r") # opening the txt file with read privileges
        msg = file1.readlines()[0]  # extract the data from the txt file
        morseMsg = ''
        Morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
                 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                 '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
                 '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
        # alphanumeric to morse dictionary
        for i in msg:
            if i != ' ':
                morseMsg += Morse[i]
                morseMsg += " "
            else:
                morseMsg += '   '  # explained in UDP client
        clientSocket.send(morseMsg.encode())  # send the message with send function (only in TCP)
        clientSocket.close()
        file1.close()

    def receive(self, serverName='Chris', serverPort=16000):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))  # Establishing TCP connection

        morseMsg = clientSocket.recv(1024)  # Using the recv function (TCP only) to receive the data from the server

        Morse1 = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
                  '....': 'h',
                  '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                  '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                  '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                  '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ',
                  '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}
        # morse to alphanumeric dictionary
        recoveredMsg = ''
        sentence = morseMsg.decode().split('   ')
        for word in sentence:
            for letter in word.split(' '):
                if letter != '':
                    recoveredMsg += Morse1[letter]
            recoveredMsg += ' '
        for i in range(1, 100):
            if not os.path.exists('./recoveredFile.txt'):
                file2 = open(r"recoveredFile.txt", "w")
                file2.write(recoveredMsg)
                break
            elif not os.path.exists('./recoveredFile('+str(i)+').txt'):
                file2 = open('recoveredFile('+str(i)+').txt', "w")
                file2.write(recoveredMsg)
                break  # explained in UDPclient
        file2.close()
        clientSocket.close()  # closing the client socket

