from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) # 同样地，使用 UDP 协议
serverSocket.bind(('', serverPort)) # server 端的套接字和 12000 端口号绑定，
print('The Server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper() # 将字符串转换为大写
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # 转换之后的字符串发送给客户端