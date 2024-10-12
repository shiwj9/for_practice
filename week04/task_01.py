class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 打印属性
    def print_info(self):
        print(f'姓名：{self.name}，年龄：{self.age}，成绩：{self.score}')

    # 计算平均值
    @classmethod
    def get_average_score(cls, student_list):
        average_score = sum(student.score for student in student_list) / len(student_list)
        return average_score


if __name__ == "__main__":
    # 创建多个 Student 对象
    student1 = Student("Tom", 20, 85)
    student2 = Student("Bob", 22, 90)
    student3 = Student("Alice", 21, 78)

    # 打印学生信息
    student1.print_info()
    student2.print_info()
    student3.print_info()

    # 计算并打印平均成绩
    students = [student1, student2, student3]
    average_score = Student.get_average_score(students)
    print(f"所有学生的平均成绩是: {average_score}")
