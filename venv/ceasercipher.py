
str = input()
str1 = input()
key = int(str1)
strlen = len(str)
result = ""

for r in range(strlen):
    strchr = str[r]
    if strchr.isupper():
        result += chr((ord(strchr) + key - 65) %26+65)
    else:
        result += chr((ord(strchr) + key-97) %26+97)
encrstr=result
print(encrstr)

print("")
print("")
strlen2 = len(encrstr)
result2 = ""

for i in range(strlen2):
    if encrstr.isupper():
        #print("Uper charecter is",encrstr[i])
        result2 += chr((ord(encrstr[i]) - key - 65) %26+65)
    else:
        #print("Lower charecter is",encrstr[i])
        result2 += chr((ord(encrstr[i]) - key - 97) %26+97)

dcerstr = result2
print(dcerstr)
