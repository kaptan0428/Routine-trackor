def getdate():
    import datetime
    return datetime.datetime.now()

a= int(input("enter 1 for harry 2 for rohan 3 for ahammad : "))
if a==1:
    b= int(input("enter 1 for exercise 2 for food : "))
    if b==1:
        c= int(input("enter 1 for log 2 for retrieve : "))
        if c==1:
            with open("hel.txt","a") as hel:
                t1 = str(getdate())
                hel.write(t1)
                hel.write(" :: ")
                hel.write(input())
                hel.write("\n")
                hel.close()

        if c==2:
            with open("hel.txt") as hel:
                print(hel.read())
                hel.close()
    if b==2:
            d = int(input("enter 1 for log 2 for retrieve : "))
            if d == 1:
                with open("hfl.txt", "a") as hfl:
                    t2 = str(getdate())
                    hfl.write(t2)
                    hfl.write(" :: ")
                    hfl.write(input())
                    hfl.write("\n")
                    hfl.close()

            if d == 2:
                with open("hfl.txt") as hfl:

                    print(hfl.read())
                    hfl.close()
if a==2:
    b = int(input("enter 1 for exercise 2 for food : "))
    if b == 1:
        c = int(input("enter 1 for log 2 for retrieve : "))
        if c == 1:
            with open("rel.txt", "a") as rel:
                t3 = str(getdate())
                rel.write(t3)
                rel.write(" :: ")
                rel.write(input())
                rel.write("\n")
                rel.close()

        if c == 2:
            with open("rel.txt") as rel:

                print(rel.read())
                rel.close()
    if b == 2:
            d = int(input("enter 1 for log 2 for retrieve : "))
            if d == 1:
                with open("rfl.txt", "a") as rfl:
                    t4 = str(getdate())
                    rfl.write(t4)
                    rfl.write(" :: ")
                    rfl.write(input())
                    rfl.write("\n")
                    rfl.close()

            if d == 2:
                with open("rfl.txt") as rfl:

                    print(rfl.read())
                    rfl.close()
if a==3:
    b = int(input("enter 1 for exercise 2 for food : "))
    if b == 1:
        c = int(input("enter 1 for log 2 for retrieve : "))
        if c == 1:
            with open("ael.txt", "a") as ael:
                t5 = str(getdate())
                ael.write(t5)
                ael.write(" :: ")
                ael.write(input())
                ael.write("\n")
                ael.close()

        if c == 2:
            with open("ael.txt") as ael:
                print(ael.read())
                ael.close()
    if b == 2:
            d = int(input("enter 1 for log 2 for retrieve : "))
            if d == 1:
                with open("afl.txt", "a") as afl:
                    t6 = str(getdate())
                    afl.write(t6)
                    afl.write(" :: ")
                    afl.write(input())
                    afl.write("\n")
                    afl.close()

            if d == 2:
                with open("afl.txt") as afl:

                    print(afl.read())
                    afl.close()
