class student:
    school="Seemax"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print(("This is student class"))


m1=student(34,35,36)
m2=student(33,34,35)
print(m1.avg())
print(student.info())
