#Taking input of string or a word
string=input("Enter a string or a word:",)
#code for printing number of occurences of each word or character in string
if ' ' in string:
    words=string.split()
    for i in words:
        counts=string.count(i)
        print(i,"came",counts,"times")
else:
    for i in string:
        counts=string.count(i)
        print(i,"came",counts,"times")
