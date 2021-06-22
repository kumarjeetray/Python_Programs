bag_of_books = [
        {"title": "Diary of a Wimpy Kid:Rodrick Rules",
            "Author": "Jeff Kinney",
            "Pages": 300
         },
        {"title": "Diary of a Wimpy Kid:Old School",
            "Author": "Jeff Kinney",
            "Pages": 300
         }
        ]
items = 0
total = len(bag_of_books)
while items < total:
    print(bag_of_books[items])
    items = items + 1
