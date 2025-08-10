'''
# functional way
def joinClass():
    print("Student joining the classes")


def completeAssigment():
    print("Students completing assignments")

# Calling the function
joinClass()
completeAssigment()

'''

# OOP programming

class ETLQALabs:

    course1 = "ETL Automation Tesitng"
    course2 = "Data Engineering"


    def joinClass(self):
        print("Student joining the classes")

    def completeAssigment(self):
        print("Students completing assignments")

'''
ref1 = ETLQALabs()
print(ref1.course1)
print(ref1.course2)
ref1.joinClass()
ref1.completeAssigment()

ref2 = ETLQALabs()
print(ref2.course1)
print(ref2.course2)
ref2.joinClass()
ref2.completeAssigment()
'''

print(ETLQALabs.course2);