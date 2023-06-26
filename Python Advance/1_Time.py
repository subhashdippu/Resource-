import time as t
Time = t.localtime() # Present Time
print(Time)
print("Time", str(Time.tm_hour) + "h" + str(Time.tm_min) + "m")
a = t.time()  # Python uses the Unix epic which is January 1st 1970 at zero hours zero minutes and zero seconds.So what do we have here is the exact number of seconds elapsed since that day.
print(a)
Time = t.time()
Delivery = Time + (86400 * 7) # Delivery time from today
a = t.localtime(Delivery)
print(a)
t.sleep(6) # It is used to delay the execution of the next line of code.