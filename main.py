#creating a dictionary
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}


#Adding new items to dictionary
programming_dictionary["Something New"] = "The value of the new item to add to the dictionary"


#looping through dictionaries

#for key in programming_dictionary:
  #print(key)
  #print(programming_dictionary[key])


#Nesting dictionaries and lists within a dictionary.
travel_log = {
  "France":{"Visited": ["Paris", "Lille", "Dijon"]},
  "South Africa": ["Pretoria","Johannesburg", "Cape Town"],
  "United States" : "Washington DC",
}

print(travel_log["France"])

#Nesting a dictionary within a list
travel_log =[ 
  {
  "country": "France",
  "Visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12
  },
  {
    "country": "South Africa",
    "Visited": ["Pretoria","Johannesburg","Cape Town"]
  }
]
