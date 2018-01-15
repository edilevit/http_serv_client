import socket

sock = socket.socket()
sock.bind(('', 12345))
sock.listen(5)

conn, addr = sock.accept()

print('connection: ', conn)
print("addres: " ,  addr[0])
data = conn.recv(1024)
print('Data bin: ', data)
data = data.decode("utf-8")
print('Data UTF-8: ', data)
data1 = data.split("\r\n")

data2 = data.split("\r\n")[0].split()[2]
data3 = data.split('\r\n')[1]
data4 = data.split('\r\n')[2]
print()
print(data1)
print(data2)
print(data3)
print(data4)
print()
#print(len(data))
#print(string)