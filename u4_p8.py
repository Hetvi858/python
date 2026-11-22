#Write a program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod

# Abstraction
class Bank(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

# Encapsulation
class SBI(Bank):
    def __init__(self, balance):
        self.__balance = balance

    def calculate_interest(self):
        print("Interest rate is 5%")

    def display_balance(self):
        print("Account Balance:", self.__balance)

# Create object
obj = SBI(10000)

obj.display_balance()
obj.calculate_interest()
