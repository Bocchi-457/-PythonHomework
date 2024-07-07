import json
# 定义学生类
class Student:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"ID: {self.id}, 姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}"


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        # 加载学生信息
        self.students = self.load_students()

    def load_students(self):
        try:
            # 尝试打开文件并读取学生信息
            with open(self.filename, 'r', encoding='utf-8') as file:
                # 将读取到的json数据转换为Student对象列表
                return [Student(**student) for student in json.load(file)]
        except FileNotFoundError:
            # 如果文件不存在，则返回空列表
            return []

    def save_students(self):
        # 将学生信息保存到文件中
        with open(self.filename, 'w', encoding='utf-8') as file:
            # 将学生对象的__dict__属性转换为列表，并保存到json文件中
            json.dump([student.__dict__ for student in self.students], file, ensure_ascii=False, indent=4)

    def add_student(self):
        # 添加学生信息
        id = input("请输入学生ID: ")
        name = input("请输入学生姓名: ")
        age = input("请输入学生年龄: ")
        gender = input("请输入学生性别: ")
        student = Student(id, name, int(age), gender)
        # 检查学生ID是否已存在
        if not any(s.id == student.id for s in self.students):
            # 如果不存在，则添加到学生列表中并保存到文件
            self.students.append(student)
            self.save_students()
            print("学生添加成功。")
        else:
            print("学生ID已存在。")

    def delete_student(self):
        # 删除学生信息
        id = input("请输入要删除的学生ID: ")
        # 使用[:]创建一个列表的副本，避免在迭代时修改列表
        for student in self.students[:]:  # 使用[:]创建一个列表的副本，避免在迭代时修改列表
            if student.id == id:
                # 如果找到要删除的学生，则从列表中移除并保存到文件
                self.students.remove(student)
                self.save_students()
                print("学生删除成功。")
                return
        print("未找到该学生ID。")

    def update_student(self):
        # 更新学生信息
        id = input("请输入要更新的学生ID: ")
        for student in self.students:
            if student.id == id:
                # 获取新的学生信息
                name = input("请输入新的学生姓名（留空则不更改）: ") or student.name
                age = input("请输入新的学生年龄（留空则不更改）: ")
                if age:
                    age = int(age)
                else:
                    age = student.age
                gender = input("请输入新的学生性别（留空则不更改）: ") or student.gender
                # 更新学生对象的属性
                student.name = name
                student.age = age
                student.gender = gender
                # 将更新后的学生信息保存到文件
                self.save_students()
                print("学生信息更新成功。")
                return
        print("未找到该学生ID。")

    def query_student(self):
        # 查询学生信息
        id = input("请输入要查询的学生ID: ")
        for student in self.students:
            if student.id == id:
                # 如果找到学生，则打印学生信息
                print(student)
                return
        print("未找到该学生ID。")

    def display_all_students(self):
        # 显示所有学生信息
        if not self.students:
            print("没有学生信息。")
        else:
            # 遍历学生列表并打印学生信息
            for student in self.students:
                print(student)

    def main_menu(self):
        # 主菜单循环
        while True:
            print("\n学员管理系统")
            print("1. 添加学员")
            print("2. 删除学员")
            print("3. 修改学员信息")
            print("4. 查询学员信息")
            print("5. 显示所有学员信息")
            print("6. 退出系统")
            choice = input("请选择操作（1-6）: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.delete_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.query_student()
            elif choice == '5':
                self.display_all_students()
            elif choice == '6':
                print("退出系统。")
                break
            else:
                print("无效输入，请重新选择。")

# 示例使用
if __name__ == "__main__":
    # 创建一个StudentManager对象
    manager = StudentManager()
    # 调用manager对象的main_menu方法，展示主菜单并处理用户输入
    manager.main_menu()
