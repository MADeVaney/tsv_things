import os, hashlib, base64

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/' # DONT scrape Gutenberg
BK_DIR = './books/'

f = open("./books.tsv", "w")
f.write("TsvHttpData-1.0 \n")

for filename in os.listdir(BK_DIR):
    if filename[:2] == 'pg':
        f.write(PREFIX+filename + '\t' + str(os.path.getsize(BK_DIR+filename)) + '\n')
        #str(base64.b64encode(hashlib.md5((PREFIX+filename).encode()))) +
f.close()