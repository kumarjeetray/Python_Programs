# To check if an english sentence contains all the vowels

def find(text):
    text = text.lower()
    alpha_list = ""
    flag = 0
    for i in range(len(text)):
        if text[i] not in alpha_list:
            alpha_list += text[i]
            if text[i] == 'a':
                flag += 1
            elif text[i] == 'e':
                flag += 2
            elif text[i] == 'i':
                flag += 3
            elif text[i] == 'o':
                flag += 4
            elif text[i] == 'u':
                flag += 5
        else:
            continue
    if flag == 15:
        print("YES")
    else:
        print("NO")


text1 = input()
find(text1)
