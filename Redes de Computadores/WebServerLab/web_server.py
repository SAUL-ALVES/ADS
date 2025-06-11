from socket import *
import os


serverPort = 6789  
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1) 

print(f"Servidor pronto para receber conexões na porta {serverPort}")

while True:
    print("Aguardando conexão...")
    connectionSocket, addr = serverSocket.accept()  
    print(f"Conexão estabelecida com {addr}")

    try:
        
        message = connectionSocket.recv(1024).decode()  
        print("Mensagem recebida:")
        print(message)

        
        filename = message.split()[1][1:]  
        print(f"Arquivo requisitado: {filename}")

        
        with open(filename, 'rb') as f:
            outputdata = f.read()

        
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

        
        connectionSocket.send(outputdata)
        print("Arquivo enviado com sucesso.")

    except FileNotFoundError:
        
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send(b"<html><body><h1>404 Not Found</h1></body></html>")
        print("Arquivo não encontrado. Enviado 404.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

    finally:
       
        connectionSocket.close()
        print("Conexão encerrada.")
