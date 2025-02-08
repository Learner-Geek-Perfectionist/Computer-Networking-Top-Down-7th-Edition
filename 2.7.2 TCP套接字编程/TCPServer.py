from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # serverSocket 是「欢迎套接字」
serverSocket.bind(('', serverPort))
serverSocket.listen(1) # 进入监听状态，最多允许 1 个连接排队
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept() # 这是阻塞式操作，意味着服务器在执行到这里时会暂停，直到有客户端发起连接请求。
    sentence = connectionSocket.recv(1024).decode() # connectionSocket 是连接套接字，专门用于与该客户端的通信。
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
