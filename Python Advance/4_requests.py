import requests
r = requests.get("https://www.google.com") # This is going to request for google 
a = r.status_code # This is going to show the status of our request
print(a) # print 200 for ok, print 403 
b = r.headers # This will show us about our request like date,time and sec etc
print(b)
c = r.headers["date"] # This will show us the perticular thing about our request like date
print(c)
d = r.text # This will show us the HTML Code of our requested page
print(d)