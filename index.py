from main import Fruit

# Start creating fruits out of the fruit class
fruit_one = Fruit("Mango", "200g", "Green", "Ksh. 50.00")
fruit_two = Fruit("Apple", "150g", "pink", "Ksh. 30.00")

print(fruit_two.name)

from main import Car, Employee

cars1 = Car('Audi', 'Matte Green', '300Hp', 'KSH 2,300,000')
cars2 = Car('FORD', 'chrome', '600Hp', 'KSH 4,100,000')
cars3 = Car('Mercedes', 'Matte Black', '340Hp', 'KSH 23,000,000')

print(cars1.horse_power)

employee1 = Employee('Bill Claxton', 'C.E.O', '14 Years', '800,000')
employee2 = Employee('Stephen Poole', 'Assistant Director', '10 Years', '700,000')
employee3 = Employee('Tommy Hardaway', 'IT Mnager', '6 Years', '620,000')
employee4 = Employee('Fred Vanvleet', 'Software Developer', '2 Years', '400,000')

print(employee1.name, employee2.name, employee3.name, employee4.name)
print(employee1.post, employee2.post, employee3.post, employee4.post)
print(employee1.experience, employee2.experience, employee3.experience, employee4.experience)
print(employee1.salary, employee2.salary, employee3.salary, employee4.salary, )
