import socket
import urllib.request, urllib.parse, urllib.error

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

fhand = urllib.request.urlopen('http://kopigeek.com')

counts = dict()

#### Counts the number of unique occurences of a word
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
# print(counts)

for line in fhand:
    print(line.decode().strip())

