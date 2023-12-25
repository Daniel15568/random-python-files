Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> c = int(input('Input the value of c: '))
count = 0
while True:
    if c > 1:
        if c%2 == 0:
            c = (c/2)
            print(c)
        elif c%2 == 1:
            c = 3 * c + 1
            print(c)
        elif c != 1:
            continue
    else:
        break
    count += 1
print('steps = ', count)
