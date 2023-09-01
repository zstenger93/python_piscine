from new_student import Student


print("\n		TEST 1\n")
student = Student(name="Edward", surname="agle")
print(student)
print("\n\n		TEST 2: Wrong initialization\n")
student = Student(name="Edward", surname="agle", id="toto")
print(student)
