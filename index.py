from main import Fruit, Car, Employee , Student

# Start creating fruits out of the fruit class

fruit_one = Fruit("Mango", "200g", "Green", "Ksh. 50.00")
fruit_two = Fruit("Apple", "150g", "pink", "Ksh. 30.00")

print(fruit_two.name)

# Start creating cars out of the car class

cars1 = Car('Audi', 'Matte Green', '300Hp', 'KSH 2,300,000')
cars2 = Car('FORD', 'chrome', '600Hp', 'KSH 4,100,000')
cars3 = Car('Mercedes', 'Matte Black', '340Hp', 'KSH 23,000,000')

print(cars1.horse_power)
# Start creating employees out of the employee class

employee1 = Employee('Bill Claxton', 'C.E.O', '14 Years', '800,000')
employee2 = Employee('Stephen Poole', 'Assistant Director', '10 Years', '700,000')
employee3 = Employee('Tommy Hardaway', 'IT Mnager', '6 Years', '620,000')
employee4 = Employee('Fred Vanvleet', 'Software Developer', '2 Years', '400,000')

print(employee1.name)


# Start creating students out of the student class
student_one = Student("Josiah","josiah@gmail.com","josia123")
student_two = Student("James","james@gmail.com","james123")

print(student_one.email)
