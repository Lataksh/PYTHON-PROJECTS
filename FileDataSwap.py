file1 = input("Please enter the path of first file  ")
file2 = input("Please enter the path of second file ")


def swap_data():
    data1 = open(file1, "r")
    content1 = data1.read()
    data2 = open(file2, "r")
    content2 = data2.read()
    swap_file_1 = open(file1, "w")
    swap = swap_file_1.write(content2)
    swap_file_2 = open(file2, "w")
    swap2 = swap_file_2.write(content1)


userChoice = int(input("Do you want to swap the data of the two file enter 1 for yes and 2 for no"))
if userChoice == 1:
    swap_data()
else:
    print("As you wish")
