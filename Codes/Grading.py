'''
    Input pattern
    56
    67
    34
    76
    98
    Output pattern
    EDFCA
'''

marks = []
for i in range(5):
    marks.append(int(input()))
output = ""
for i in marks:
    if marks[i] > 0 and marks[i] <= 49:
        output += 'F'
    elif marks[i] > 49 and marks[i] <= 59:
        output += 'E'
    elif marks[i] > 59 and marks[i] <= 69:
        output += 'D'
    elif marks[i] > 69 and marks[i] <= 79:
        output += 'C'
    elif marks[i] > 79 and marks[i] <= 89:
        output += 'B'
    else:
        output += 'A'
print(output)
