bag = {
    "books": [{"title": "Diary of a Wimpy Kid:Rodrick Rules",
                "Author": "Jeff Kinney",
                 "Pages": 300
             },
              {"title": "Diary of a Wimpy Kid:Old School",
                  "Author": "Jeff Kinney",
                  "Pages": 300
               }
              ],
    "stationary": {
        "type": "pen",
        "color": "blue",
        "body": "metal",
        "body_color": "black"
        },
    "pad": [{
        "style": "single-line",
        "pages": 200,
        "margins": "absent"
            },
        {
        "style": "blank",
        "pages": 200,
        "margins": "absent"
            }]
        }
# full dictionary
for key in bag:
    print(bag[key])
# only the keys
for key in bag:
    print(key)