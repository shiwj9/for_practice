import task_01 as tk


class GraduateStudent(tk.Student):
    def __init__(self, name, age, score, thesis_title):
        # 调用父类的构造函数来初始化继承的属性
        super().__init__(name, age, score)
        # 初始化子类特有的属性
        self.thesis_title = thesis_title

    def print_info(self):
        print(f'姓名：{self.name}，年龄：{self.age}，成绩：{self.score}，论文题目：{self.thesis_title}')

    # 添加submit_thesis方法
    def submit_thesis(self):
        print(f"{self.name} 已提交论文: {self.thesis_title}")


if __name__ == "__main__":
    # 创建一个GraduateStudent对象
    grad_student = GraduateStudent("Alice", 18, 99, "Python")

    # 打印学生信息
    grad_student.print_info()

    # 模拟提交论文
    grad_student.submit_thesis()
