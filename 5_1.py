file_name = "./infile.txt"
infile = open(file_name, "r")
# print("infile", infile)
# for line in infile:
#     print("Line: ", line)
names = [line.rstrip() for line in infile]
print("names: ", names)

infile.close()

def main():
    display_with_forloop(file_name) # display_with_forloop() - missing arguments

def display_with_forloop(file):
    infile = open(file_name, "r") # infile_object = open(file_name, "r") also works
    for line in infile:
        print(line, end="")
    infile.close()

def display_with_list_comprehension(file_name): 
    infile = open(file_name, "r")
    items = [line.rstrip() for line in infile]
    print("items: ", items)
    infile.close()


def open_file(file_name, mode): open_file
    return open(file_name, mode)



main()


