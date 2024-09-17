# Python script that manages student records using tuples, sets, and frozen sets,
# and demonstrates various operations and methods.
from operator import index

# Create tuples to store student information (name, age, grade).
student1 = ("Emma Lee", 17, "A")
student2 = ("Stuart Smith", 18, "B")
student3 = ("Ann Rose", 17, "A+")
student4 = ("John Wolf", 19, "C")

#  Use tuple methods to count and index elements.
students = (student1, student2, student3, student4) # Create new tuple "students" to count all students
print("Total amount of students:", len(students))
print ("Index of Ann Rose", students.index(student3))

#  Create sets to store unique student IDs and courses.
student1_ID = 10
student2_ID = 11
student3_ID = 12
student4_ID = 13

students_IDs = {student1_ID, student2_ID, student3_ID, student4_ID}
courses_term1 = {"Biology", "Art", "Economy", "Geography"}
courses_term2 = {"Science", "Modern Technology", "French"}
print("Students IDs:", students_IDs)
print("Students courses in term 1:", courses_term1)
print("Students courses in term 2:", courses_term2)


# Perform set operations like union, intersection, and difference.

# Creating the union of the two sets
all_courses = courses_term1.union(courses_term2)
print("List of all courses:", all_courses)

# Creating the intersection of the two sets
courses_term1.add("French")
course_in_both_terms = courses_term1.intersection(courses_term2)
print("Course in both terms:", course_in_both_terms)

# Creating the difference between the two sets
different_courses_term2 = courses_term2.difference(courses_term1)
print("Different courses in term 2:", different_courses_term2)

# Creating frozen set
frozen_courses = frozenset(all_courses)
print("Frozen courses:", frozen_courses)


