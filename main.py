class Fruit:
    # This is a constructor
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price


class Car:
    def __init__(self, model, color, horse_power, price):
        self.model = model
        self.color = color
        self.horse_power = horse_power
        self.price = price



class Employee:
    def __init__(self, name, post, experience, salary):
        self.name = name
        self.post = post
        self.experience = experience
        self.salary = salary

class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print("you registered with email",self.email,"and password",self.password)

    def login(self):
        #assume the user has already registered
        if self.email == "abc@example.com" and self.password == "123":
            print("login successful")
        else:
            print("Please enter the correct username or password")