# 1
# a
score = 65
print((50 <= score <= 80))

# b
temp = 19
print((18 <= temp <= 24) == False)

# c
school_zone = 40
speed = 52
print((speed <= school_zone) or speed == 0)

# d
tank_capacity = 60
fuel = 66
print(fuel >= 0 and fuel <= tank_capacity)

# 2
# a
filename = "gobi.csv"
filename_v2 = filename[-4:]
print(filename_v2.lower() == ".csv" or filename_v2.lower() == ".tsv")

# b
course = "ics0u"
course_v2 = course[0:3]
course_v3 = course[0:4]
print(course_v2.lower() == "ics" and course_v3.lower() != "ics0")

# c
s = "animated"
s_v2 = s[0]
print(s_v2.lower() == "a" or s_v2.lower() == "e" or s_v2.lower() == "i" or s_v2.lower() == "o" or s_v2.lower() == "u")

# d
message = "errorfatal"
if "fatal" in message.lower():
    print(False)
elif "error" in message.lower():
    print(True)
else:
    print(False)

# 3
# a
