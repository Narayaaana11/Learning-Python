"""
Object-Oriented Programming in Python

This module demonstrates classes, objects, inheritance, and OOP concepts.
"""

# Basic Class
class Dog:
    """A simple Dog class"""
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a dog with name and age"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def __str__(self):
        """String representation of the dog"""
        return f"{self.name} is {self.age} years old"

# Inheritance
class GoldenRetriever(Dog):
    """A Golden Retriever is a type of Dog"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def fetch(self):
        """Golden Retrievers love to fetch"""
        return f"{self.name} loves to fetch!"

# Encapsulation
class BankAccount:
    """Demonstrating encapsulation with private attributes"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get the current balance"""
        return self.__balance

# Main execution
if __name__ == "__main__":
    print("=== Basic Class ===")
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)
    print(dog1)
    print(dog2)
    print(dog1.bark())
    
    print("\n=== Inheritance ===")
    golden = GoldenRetriever("Charlie", 2, "Golden")
    print(golden)
    print(golden.bark())
    print(golden.fetch())
    
    print("\n=== Encapsulation ===")
    account = BankAccount("John Doe", 1000)
    print(f"Initial balance: ${account.get_balance()}")
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(2000))  # Should fail
