# 1
# a = int(input())
# b = int(input())
# try:
#     print(f"Result: {a/b}")
# except ValueError:
#     print("It's letter")
# except ZeroDivisionError:
#     print("Don't divide by zero")
# finally:
#     print("Calculation finished")


# 2
# Cities = ['Dushanbe', 'Khujand', 'Bokhtar']
# a = int(input())
# try:
#     print(Cities[a])
# except ValueError:
#     print("Enter number")
# except IndexError:
#     print("Position does not exist")

# 3
# Prices = {
#     'mouse': 100,
#     'keyboard': 250,
#     'monitor': 1200
#     }
# try:
#     b = input()
#     a = int(input())
#     print(f"Total:", Prices[b] * a)
# except KeyError:
#     print("Wrong key")
# except ValueError:
#     print("Wrong value")

# 4
# def calculate_average(values):
#     try:
#         l = []
#         for i in values:
#             l.append(int(i))
#         print("Average:",sum(l)/ len(l))
#     except ValueError as error:
#         print("ValueError:",error)
#     except ZeroDivisionError  as error:
#         print("ZeroDivisionError:",error)
# k = input().split()
# calculate_average(k)

# 5
# def register_participant(name, age):
#     if type(name) != str:
#         return "TypeError: name must be a string"
#     if type(age) != int:
#         return "TypeError: age must be an integer"
#     if age < 18 or age > 100:
#         return "ValueError: age must be from 18 to 100"
#     return {"name": name, "age": age}
# print("Registered:", register_participant("Ali", 22))
# print(register_participant("Sara", "seventeen"))
# print(register_participant(22, "15"))


# 6


# 7
# def process_payment(balance, amount):
#     if amount <= 0:
#         return "amount must be positive"
#     elif amount > balance:
#         return "insufficient funds"
#     return balance - amount
# balance = 1000
# amount = 1150
# try:
#     new_balance = process_payment(balance, amount)
# except ValueError as error:
#     print("ValueError:", error)
# else:
#     print("New balance:", new_balance)
# finally:
#     print("Payment attempt finished")


# 8
# def price_per_item(total, quantity):
#     return total / quantity
# def build_report(order):
#     return price_per_item(order["total"], order["quantity"])
# def main():
#     order = {"total": 600, "quantity": 3}
#     print(build_report(order))
# main()

# 9
# def line_total(price, quantity):
#     return price * quantity
# def cart_total(items):
#     total = 0
#     for index, item in enumerate(items):
#         price = item["price"]
#         quantity = item["quantity"]
#         total += line_total(price, quantity)
#     return total
# cart = [
#     {"name": "Mouse", "price": 100, "quantity": 2},
#     {"name": "Keyboard", "price": 250, "quantity": 1},
#     {"name": "Cable", "price": 30, "quantity": 3},
# ]
# print(cart_total(cart))


# 10
# from datetime import datetime
# def parse_date(text):
#     return datetime.strptime(text, "%d.%m.%Y")
# text = input()
# print(parse_date(text).strftime("%Y-%m-%d"))