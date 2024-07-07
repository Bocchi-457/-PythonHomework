# class

class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.age = age

    def __str__(self):  # 专有方法，用于打印对象信息
        return f"{self.__class__.__name__}: {self.__name} is {self.age} years old."

    def greet(self):  # 公有方法
        print(f"Hello, my name is {self.__name}.")

    def _private_method(self):  # 保护方法（约定俗成的私有方法，实际上Python没有强制私有）
        print("This is a protected method.")

    @staticmethod
    def static_method_example():
        print("This is a static method.")

    @classmethod
    def class_method_example(cls):
        print(f"This is a class method of {cls}.")

        # 运算符重载示例

    def __add__(self, other):
        return self.age + other.age


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)  # 调用父类初始化方法
        self.position = position

    def greet(self):  # 方法重写
        super().greet()  # 调用父类方法
        print(f"I work as a {self.position}.")

        # 私有方法

    def __private_method(self):
        print("This is a truly private method.")


class Manager(Employee, Person):  # 多继承，但注意Python中的方法解析顺序（MRO）
    def __init__(self, name, age, position, department):
        super().__init__(name, age, position)  # 注意这里的super可能不总是指向Employee
        self.department = department

    def __str__(self):  # 方法重写
        return f"{super().__str__()} Department: {self.department}"

    # 使用示例


person = Person("Alice", 30)
print(person)
person.greet()

employee = Employee("Bob", 28, "Software Engineer")
print(employee)
employee.greet()

# 运算符重载示例
employee2 = Employee("Charlie", 32, "Data Scientist")
print(employee.age + employee2.age)

manager = Manager("David", 35, "CTO", "Tech")
print(manager)