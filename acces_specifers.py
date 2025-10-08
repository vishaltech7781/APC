class A:
    def _init_(self):
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

    def showA(self):
        print("From Class A:", self._protected_var)
        print("From Class A:", self.__private_var)


class B(A):
    def showB(self):
        print("From Class B:", self._protected_var)


class C(B):
    def showC(self):
        print("From Class C:", self._protected_var)


obj = C()
obj.showA()
obj.showB()
obj.showC()

print("\nDirect Access:")
print(obj._protected_var)