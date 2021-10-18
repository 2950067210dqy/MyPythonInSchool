import socket
import threading
import time
def tcpLink(sock,addr):
    print(f"接收一个来自{addr}的请求")
    sock.send('服务器连接成功'.encode("utf-8"))
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send((('hello,%s')%data.decode('utf-8')).encode('utf-8'))
        print(data.decode('utf-8'))
    sock.close()
    print(f"来自{addr}的请求关闭了")
    pass
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8809))
s.listen(4)
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcpLink,args=(sock,addr))
    t.start()