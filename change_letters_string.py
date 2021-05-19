'''
To change certain letter is a string using translate table
'''
table=str.maketrans("wy","gf","u")
s="weeksyourweeks"
s=s.translate(table)
print(s)
