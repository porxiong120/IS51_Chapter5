#file_name = "./infile.txt"
#infile = open(file_name, "r")
# # # print("infile", infile)
# # # for line in infile:
# # #     print("Line: ", line)
#names = [line.rstrip() for line in infile]
# # print("names: ", names)

#infile.close()

# def main():
#     display_with_forloop(file_name) # display_with_forloop() - missing arguments
#     print()
#     display_with_list_comprehension(file_name)

# def display_with_forloop(file_name):
#     infile = open(file_name, "r") # infile_object = open(file_name, "r") also works
#     for line in infile:
#         print(line, end="")
     
#     infile.close()

# def display_with_list_comprehension(file_name): 
#     infile = open(file_name, "r")
#     items = [line.rstrip() for line in infile]
#     print("items: ", items)
#     infile.close()


# def open_file(file_name, mode): 
#     return open(file_name, mode)



# main()

# Create a file object in write mode 

#def main():
#    save_to_outfile("./outfile.txt")

#def open_file(file_name, mode):
#    return open(file_name, mode)


#def save_to_outfile(file_name): 
#    outfile = open_file("./outfile.txt", "w")
# print("outfile: ", outfile)

# for name in names: 
#     print("name: ", name) 
#     check = "Doe" in name 

#     print("check", check)

#    for name in names: 
#        if "Doe" not in name: 
            # print("NAme 2 b persisted: ", name)
#            outfile.write(name + "\n")
            # data.append(name)
        # else: 
        #     print("Names 2 b excluded: ", name)
        #     outfile.write()

#    outfile.close()
#main()


# a_list = []
# a_set = {}

# a_list.append("A")

#a_set.add("A")
#a_set.add("A")
#a_set.add("B")
#a_set.add("C")

# def main():
#     words = ["nudge", "nudge", "wink", "wink"]
#     terms = set(words)
#     print("terms", terms)
#     terms.add("wink")
#     terms.add("new wink")
#     terms.deiscard("nudge")

# main()

arr1 = ["Alpha", "Bravo", "Charlie"]
arr2 = ["Bravo", "Delta"]
set1 = set(arr1)
set2 = set(arr2)

print("set1", set1)
print("set2", set2)

# built-in Set methods: 1 .union, 2 .intersection, 3. .difference()

print("union: ", set1.union(set2))
print("intersection: ", set1.intersection(set2))
print("difference: ", set1.difference(set2))