from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) # 使用 UDP 协议，这个套接字可以用于「接收」和「发送」数据包。
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort)) # 客户端，通过「套接字」发送报文
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 客户端，通过「套接字」接受修改的报文
print(modifiedMessage.decode())
print(clientSocket.fileno())  # 打印套接字的文件描述符
clientSocket.close()