from random import shuffle

liste = "amazing excited gorgeous stunning tremendous greatest best fantastic fenomenal delightful ambitious outstanding incredible \
        spectacular magical revolutionary beautiful".upper().split()

shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM",end=" ")
        print()
    print("{} SPAM, {} SPAM".format(liste.pop(), liste.pop()))
    print()
print()