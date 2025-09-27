##1
students_set = {"Alice", "Bob", "Charlie", "David", "Eve"}
students_set.add("Frank")
print(students_set)

# students_set.pop()
# print(students_set)

# students_set.clear()
# print(students_set)



##2
frozenset_students = ("Sara", "Alice", "Islam")
frozenset_students.__add__= ("Frank")
print(frozenset_students)



##3
student_info = ("Alice" ,"18 years" , "favorite languase" "Python", "Java", "C++")
# print(student_info)

# print(student_info[1])

# count = student_info.count("Alice")
# print(count)



##4
student_dict = {"Alice": "18", "Bob": "12", "Ale": "16"}
student_dict["Islam"] = "20"
print(student_dict)

# student_dict ["Alice"] = 25
# print(student_dict)

# student_dict.pop("Bob")
# print(student_dict)

# print(student_dict.keys())
# print(student_dict.values())