import os, hashlib, base64

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
BK_DIR = './books/'

f = open("./books.tsv", "w")
f.write("TsvHttpData-1.0\n")

for filename in os.listdir(BK_DIR):
    if filename[:2] == 'pg':
        with open(BK_DIR + filename) as current:
            text = current.read()
            f.write(PREFIX+filename + '\t' + str(os.path.getsize(BK_DIR+filename)) + '\t' + str(base64.b64encode(hashlib.md5((text).encode()).digest()))[2:26] + '\n')
f.close()