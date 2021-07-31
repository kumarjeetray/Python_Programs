# Name - Kumarjeet Ray
# Roll Number - 1928170
# Batch - CSSE3

num_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : ", num_list)
res = []
for i in num_list:
	if i not in res:
		res.append(i)

print ("The list after removing duplicates : " + str(res))
