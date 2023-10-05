class Students():
    def __init__(self, name, age, classroom, average_score):
        self.name = name
        self.age = age 
        self.classroom = classroom
        self.average_score = average_score
        return 

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Classroom: {self.classroom}"

test1 = int(input("Enter the score for test 1: "))
test2 = int(input("Enter the score for test 2: "))
test3 = int(input("Enter the score for test 3: "))


Student1 = Students("David", "20", "5")

print(Student1)
