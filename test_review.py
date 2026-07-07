import os

API_KEY = "sk-test-12345"  # hardcoded secret, bad practice

def divide(a, b):
    return a / b  # no check for b == 0

def get_user(users, user_id):
    for u in users:
        if u["id"] == user_id:
            return u
    # no return / None handling if not found

def save_file(path, data):
    f = open(path, "w")  # file never closed
    f.write(data)

def calculate_discount(price, discount_percent):
    return price - (price * discount_percent)  # missing / 100

class OrderProcessor:
    orders = []  # mutable default shared across all instances

    def add_order(self, order):
        self.orders.append(order)
        print("Order added: " + order)  # will crash on non-string input

if __name__ == "__main__":
    result = divide(10, 0)
    print(result)