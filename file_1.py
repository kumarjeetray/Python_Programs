my_file = open("Myself.txt", "r")
if my_file.readable() == True:
    #print(my_file.read())
    #print(my_file.readline())
    #print(my_file.readlines())
    for my_story in my_file.readlines():
        print(my_story)
my_file.close()