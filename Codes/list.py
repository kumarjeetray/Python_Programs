lucky_numbers=[4, 8, 15, 16, 23, 42]
friends=["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Oscar", "Toby"]
friends.append("Josh")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop(3)
friends.pop()
print(friends)
print(friends.index("Kelly"))
print(friends.count("Oscar"))
friends.sort()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)
friends2 = friends.copy()
friends2.extend(lucky_numbers)
print(friends2)