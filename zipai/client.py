import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('47.94.164.171',8809))
print(s.recv(1024))
print("你发送了123123：")
s.send("123123".encode("utf-8"))
print("服务器向你返回了："+s.recv(1024).decode('utf-8'))
s.send(b"exit")
s.close()
