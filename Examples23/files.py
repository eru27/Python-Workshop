FOLDER = 'D:\\ISP\\2022\\PythonWorkshop\\Examples23\\'


file1 = open(FOLDER + 'print.txt', 'w')

file1.write(input())

file1.close()

with open('print.txt', 'r') as file2:
    print(file2.read())
