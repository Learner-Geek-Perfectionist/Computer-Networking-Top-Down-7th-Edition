from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) # 使用 UDP 协议，这个套接字可以用于「接收」和「发送」数据包。
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
print(clientSocket.fileno())  # 打印套接字的文件描述符
clientSocket.close()