# 1
# a
score = 66
print(50 <= score <= 80)

# b
temp = 17
print((18 <= temp <= 24) == False)

# c
speed = 38
school_zone = 40
print(speed < school_zone or speed == 0)

# d
fuel = 60
tank_capacity = 60
print(fuel >= 0 and fuel <= tank_capacity)

# 2
# a
file = "togemaru.tsv"
file_v2 = file[-3:]
print(file_v2.lower() == ".tsv" or file_v2.lower() == ".csv")

# b
course = "ics4u"
course_v2 = course[0:3]
course_v3 = course[0:4]
print(course_v2.lower() == "ics" and not course_v3.lower() == "ics0")

# c
s = input("Enter a random string:")
s_len = len(s)
s_v2 = s[0]
print(s_len > 0 and ("a" or "e" or "i" or "o" or " u ") in s_v2.lower())

# d
message = input("Enter a message (error or fatal)")
if "fatal" in message.lower():
    print(False)
else:
    print(True)



