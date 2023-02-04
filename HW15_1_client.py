import socket

client = socket.socket()
client.connect(('127.0.0.1', 5000))
text = None

try:
    text = input('Enter your text: ')
except KeyboardInterrupt:
    print('/nSorry, time is over')

if text:
    client.send(bytes(text, encoding='UTF-8'))

b = client.recv(1024)
print((str(b)).replace("b'","").replace("'", ""))

client.close()
