'''
 Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer

 at position
.
print: Print the list.
remove e: Delete the first occurrence of integer
.
append e: Insert integer
 at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

def main():
    if command[0]=='insert':
        L.insert(int(command[1]),int(command[2]))
    elif command[0]=='print':
        print(L)
    elif command[0]=='append':
        L.append(int(command[1]))
    elif command[0]=='remove':
        L.remove(int(command[1]))
    elif command[0]=='sort':
        L.sort()
    elif command[0]=='reverse':
        L.reverse()
    elif command[0]=='pop':
        L.pop()


if __name__ == '__main__':
    L=[]
    N = int(input())
    for i in range(N):
        command=str(input())
        command=command.split(' ')
        main()