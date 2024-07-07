import socket

# 创建一个TCP套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到指定的服务器地址和端口
client.connect(('127.0.0.1', 8888))

# 发送数据到服务器，需要先将数据编码为字节流
client.send('苏卡不列!'.encode())

# 接收服务器返回的数据，最多接收1024字节
data = client.recv(1024)

# 将接收到的字节流解码为字符串并打印
print('客户端收到数据：', data.decode())

# 关闭客户端套接字连接
client.close()