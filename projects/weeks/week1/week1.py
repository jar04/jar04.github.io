#!/usr/bin/python3
InfoDB = []

InfoDB.append({"First Name": "Brian",
               "Last Name": "Green",
               "Date of Birth": "01/14/1984",
               "Employment": "Teacher",
               "Email": "davgreen@gmai.com",
               "Hobbies": ["Reading", "Soccer", "Woodworking"]
})

x = len(InfoDB)

def forLoop():
  for x in InfoDB:
    print(x)