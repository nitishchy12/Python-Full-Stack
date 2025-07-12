# class BankAccount:
#     def __init__(self, amount, holder):
#         self.amount = amount
#         self.holder = holder

#     def deposite(self, x):
#             self.amount+=x
#             def withdrawl(self,x):
#                  self.ammount-=x
             
            
# encapsulation
# class BankAccount:
#     def __init__(self,ammount,holder):
#             self --ammount+=ammount ## private
#             self -holder=holder ## protected

#     def deposite(self,x):
#           self.ammount+=x
#           def withdrwal(self,x):
#                 self.ammount-=x


## inheritance
# class currentAccount(BankAccount):
#       def __init__(self,ammount,owner,overdraft):
#             super().__init__(ammount,owner)
#             self.ammount=overdraft



## polymorphism
# Base class: BankAccount
# class BankAccount:
#     def __init__(self, amount, holder):
#         self.__amount = amount       # Private attribute
#         self._holder = holder        # Protected attribute

#     def deposit(self, x):
#         self.__amount += x

#     def withdrawal(self, x):
#         if x <= self.__amount:
#             self.__amount -= x
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__amount

#     def display(self):  
#         print(f"[BankAccount] Holder: {self._holder}, Balance: {self.__amount}")


# # Derived class: CurrentAccount
# class CurrentAccount(BankAccount):
#     def __init__(self, amount, holder, overdraft):
#         super().__init__(amount, holder)
#         self.overdraft = overdraft

#     def display(self):  # Polymorphism: overriding display()
#         print(f"[CurrentAccount] Holder: {self._holder}, Overdraft Limit: ₹{self.overdraft}, Balance: ₹{self.get_balance()}")


# # Polymorphic behavior
# def show_account_info(account):  # accepts any BankAccount type
#     account.display()


# # Testing
# ba = BankAccount(5000, "Nitish")
# ca = CurrentAccount(7000, "Rahul", 2000)

# show_account_info(ba)
# show_account_info(ca)




## ABstraction
# class BankAccount(ABC):
#     def __init__(self, amount, holder):
#         self.__amount = amount       # Private
#         self._holder = holder        # Protected

#     def deposit(self, x):
#         self.__amount += x

#     def withdrawal(self, x):
#         if x <= self.__amount:
#             self.__amount -= x
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__amount

#     @abstractmethod
#     def display(self):  # Abstract method
#         pass


# # Concrete class inheriting from BankAccount
# class CurrentAccount(BankAccount):
#     def __init__(self, amount, holder, overdraft):
#         super().__init__(amount, holder)
#         self.overdraft = overdraft

#     def display(self):  # Must override abstract method
#         print(f"[CurrentAccount] Holder: {self._holder}, Overdraft Limit: ₹{self.overdraft}, Balance: {self.get_balance()}")



# Polymorphic function
# def show_account_info(account: BankAccount):
#     account.display()

# #
# ca = CurrentAccount(7000, "Rahul", 2000)

# show_account_info(ca)
# show_account_info(sa)



## operator overloading
## Vector3D class in Python, demonstrating OOP principles and operator overloading:
import math

class Vector3D:
    # Constructor
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # String representation
    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    # Equality check
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # Addition
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # Scalar multiplication
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
        print("Scalar must be int or float")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Dot product
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Cross product
    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # Magnitude
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Normalize
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            print("Cannot normalize a zero vector")
            return Vector3D()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)
   
    ## comparsion
    def __lt__(self,other):
         return self.magnitude() < other.magnitude()
    
    def __le__(self,other):
         return self.magnitude() <= other.magnitude()
    
    def __gt__(self,other):
         return self.magnitude() > other.magnitude()
    
    def __ge__(self,other):
         return self.magnitude() > other.magnitude()

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1:", v1)
print("v2:", v2)
print("v1 == v2:", v1 == v2)
print("v1 + v2:", v1 + v2)
print("3 * v1:", 3 * v1)
print("Dot product:", v1.dot(v2))
print("Cross product:", v1.cross(v2))
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())
print("v1 < v2:", v1 < v2)
print("v1 <= v2:", v1 <= v2)
print("v1 > v2:", v1 > v2)
print("v1 >= v2:", v1 >= v2)

