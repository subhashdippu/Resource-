import requests
import json  #  JavaScript Object Notation. JSON is an open standard file format and data interchange format
import pprint
r = requests.get("https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple")
a = r.status_code
print(a)
# b = r.text
# print(b)

# print(type(r.text))
# question = json.loads(r.text) # This is going to change the string into python dict
# print(type(question)) 

# pprint.pprint(question) # This is going to print HTML Code into python Dict
# c = question['results'][0]['category'] # This is going to print a perticular thing
# print(c)

person = {"Apple" : "Seb",
          "Mango" : "Aam"
}
person_json = json.dumps(person)  # This is going to change the python dict(Json) into string
print(person_json)
print(type(person_json))