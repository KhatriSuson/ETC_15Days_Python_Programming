import matplotlib.pyplot as plt

grade = ["One", "Two", "Three", "Four", "Five"]
students = [10, 25, 37, 48, 69]

plt.figure(figsize=(10, 5))

plt.bar(grade, students)

plt.title("Student Bar Graph")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()
