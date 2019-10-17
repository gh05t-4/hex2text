# Created by SKS bros.

hexval = input("Enter the hex values: ")
hexval = hexval.replace(" ","")

i = 0
l = len(hexval)
j = int(l/4)
text = ""

while i<j:
    h = hexval[:4]
    text = text + chr(int(h,16))
    hexval = hexval[4:l]
    i = i + 1

print("\nText:\n\n" + text)
print("\n")
