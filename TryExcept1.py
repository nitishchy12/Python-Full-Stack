x = int(input())
y = int(input())

ans = 0
try:
    ans = x / y
    print(ans)

except ZeroDivisionError:
    print("Hello")

except:
    print("Not div by 0")

finally:
    print("This works after try except anyway.")

# Custom Exception
class InvalidTransactionException(Exception):
    pass

def withdraw(x):
    amount = 100
    if x > amount:
        raise InvalidTransactionException("Insufficient balance")
    amount -= x
    print(f"Withdrawal successful. Remaining balance {amount}")

try:
    withdraw(120)
except InvalidTransactionException as e:
    print("Transaction failed:", e)
