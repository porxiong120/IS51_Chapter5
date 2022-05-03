"""
Afghanistan,Asia,31.8,251772
Albania,Europe,3.0,11100
Algeria,Africa,38.3,919595
"""

continent = "Afghanistan"
# print("Continent", continent)
print("Continent", continent.title())

# if continent != "Antartica":
#     print("Antartica is not part of the UN")
# else: 
#     print("There are no countries in Antartica.")

continent = input("Enter a name of a continent: ") # south america works, but no outputs
continent = continent.title()
if continent != "Antartica":
    infile = open("UN.txt", "r")
    # print("infile", infile)
    for line in infile: 
    #for line in i: - i is not defined, 
        # print("Line", line) 
        #print("Line", i) 
        data = line.split(",")
        print("data[1]: ", data[1])
        # print("data:", data)
        if data[1] == continent:
            print("Found: ", data[0])

else: 
    print("There are no countries in Antartica.")