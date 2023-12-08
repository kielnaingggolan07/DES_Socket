import socket
import des
import sys
from time import sleep

def Main():
        host = "127.0.0.1"
        port = 5002
        mySocket = socket.socket()
        mySocket.connect((host,port))
        
        message = input("Masukkan pesan yang di enskripsi -> ")
        key = "0A1B2C3D4E5F6071"
        finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
        print("Pesan Tereskripsi = " + finalEncryptedMessage)
        while message != 'q':
                des.sending()
                finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
                #sending the message
                mySocket.send(finalEncryptedMessage.encode())
                #receiving the response from the other user
                data = mySocket.recv(1024).decode()
                print("menerima dari server = " + data)
                #decrypting the other user's message
                decryptedMessage = des.decrypt(data, key)
                if not data:
                        break
                print ("Pesan Terdeskripsi = ", des.bin2text(decryptedMessage))
                print("\n")
                #setting up the message all over again....
                message = input("Masukkan kata yang mau di enkripsi -> ")
                finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
                print("Pesan Tereskripsi = " + finalEncryptedMessage)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
    