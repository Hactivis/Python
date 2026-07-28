class A:
    label = "A: Base Class"

class B:
    label = "B: Aveneger's Doomsday"

class C(A):
    label = "C: Aveneger's Endgame"

class D(C,B):
    pass

cup = D()
print(cup.label)
print(D.__mro__)