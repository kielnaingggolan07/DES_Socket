import socket
import des



def Main():
    host = "127.0.0.1"
    port = 5002
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(2)
    conn, addr = mySocket.accept()
    print ("terhubung dengan port: " + str(addr))

    while True:
            data = conn.recv(1024).decode()
            print("Menerima data dari client = " + data)
           
            key = "0A1B2C3D4E5F6071"
            decryptedMessage = des.decrypt(data, key)
            if not data:
                    break
            print ("Pesan Terdeskripsi = ", des.bin2text(decryptedMessage))
            print("\n")
            message = input("Masukkan kata yang mau di enkripsi -> ")
            #encrypting the message using DES
            finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
            print("Pesan Tereskripsi = " + finalEncryptedMessage)
            #prints the pretty loading bar
            des.sending()
            #sending the message
            conn.send(finalEncryptedMessage.encode())
 
    conn.close()
     
if __name__ == '__main__':
    Main()