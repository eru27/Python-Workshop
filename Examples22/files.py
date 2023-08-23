FOLDER = 'D:\\ISP\\2022\\PythonWorkshop\\Examples22\\'


file1 = open(FOLDER + 'print1.txt', 'w')

file1.write('Hello there!')

file1.close()

with open('print2.txt', 'w') as file2:
    file2.write('Plain text document.')

with open('print1.txt', 'r') as file2:
    message = file2.read()

print(message + "\n", "> General Kenobi")

inp = input()

print('\n' + inp)