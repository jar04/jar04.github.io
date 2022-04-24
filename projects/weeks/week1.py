#!/usr/bin/python3
InfoDB = []

InfoDB.append({"First Name": "Brian",
               "Last Name": "Green",
               "Date of Birth": "01/14/1984",
               "Employment": "Teacher",
               "Email": "davgreen@gmai.com",
               "Hobbies": ["Reading", "Soccer", "Woodworking"]
})

InfoDB.append({"First Name": "James",
               "Last Name": "Slater",
               "Date of Birth": "04/23/1953",
               "Employment": "Lawyer",
               "Email": "jslater@gmai.com",
               "Hobbies": ["Running", "Woodworking"]
})


def print_data(n):
  print(InfoDB[n]["First Name"], InfoDB[n]["Last Name"])
  print(InfoDB[n]["Date of Birth"], InfoDB[n]["Employment"])
  print(InfoDB[n]["Email"])
  print(InfoDB[n]["Hobbies"])

def for_loop():
  for i in range(len(InfoDB)):
    print_data(i)

def while_loop(i):
  while i < len(InfoDB):
    print_data(i)
    i = i + 1
  return

def recursive_loop(x):
  if(x < len(InfoDB)):
    print_data(InfoDB[x])
    recursive_loop(x+1)
  return
  
    