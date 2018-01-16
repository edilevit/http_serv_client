
import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 12345))
conn.send(b"Hello!")
conn.send(" Vasya".encode("utf-8"))
data = conn.recv(1000)
print(data)