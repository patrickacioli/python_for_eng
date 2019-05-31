import hashlib 
for i in range(0,100):
    print(hashlib.md5(open("md5_text.txt", "rb").read()).hexdigest())