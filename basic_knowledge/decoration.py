def funA(desA):
    print("funA")
    print(desA)


def middle(mids):
    print("mid")
    mids()


def funB(desB):
    print("funB")
    print("params：", desB)
    return middle


print("name: ", __name__)


@funA("What are you doing, A?")
@funB("I am b")
def funC():
    print("funC")
