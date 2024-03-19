import matplotlib.pyplot as plt

grade = ["One", "Two", "Three", "Four", "Five"]
students = [10, 25, 37, 48, 69]

plt.subplot(131)  # row col index 
plt.bar(grade, students)
plt.subplot(132)
plt.scatter(grade, students)
plt.subplot(133)
plt.plot(grade, students)

plt.suptitle("Wroking With Different Ploting")
plt.show()
