from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) # 客户端和服务端之间建立 TCP 连接，执行三次握手，
sentence = input('Input lowercase sentence: ') # 字符串 sentence 连续收集字符直到用户键入回车以终止该行为止。
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
