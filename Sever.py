import socket

# 创建一个TCP套接字
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到本地主机的8888端口
sever.bind(('localhost', 8888))

# 开始监听连接，最大连接数为5
sever.listen(5)

# 等待客户端连接，并返回客户端套接字和地址
client, addr = sever.accept()

# 打印客户端连接成功的消息和客户端地址
print('客户端连接成功', addr)

# 接收客户端发送的数据，最多接收1024字节
data = client.recv(1024)
# 打印接收到的数据
print('收到数据：', data.decode())

# 提示用户输入要回复的消息
msg = input('请输入你要和客户端回复的消息：')

# 发送回复消息给客户端
client.send(msg.encode())

# 关闭客户端套接字
client.close()