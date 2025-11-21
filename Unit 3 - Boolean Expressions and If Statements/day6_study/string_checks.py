# string checks (part b2)
# 1
email = "james@school.ca"
email_v2 = email[-10:]
print(email_v2.lower() == "@school.ca")

# 2
course = "ics"
course_v2 = course[0:3]
print(course_v2.lower() == "ics")

# 3
s = input("Enter a random string")
s_len = len(s)
s_v2 = s[0]
print(s_len > 0 and 'a' <= s_v2.lower() <= 'm')

# 4
code = input("Enter a document name in python:")
code_len = len(code)
code_v2 = code[-2:]
print(code_len == 5 and code_v2.lower() == "py")

# Numeric Gates
# 1
height_cm = 20
threshold_cm = 54
print(height_cm >= threshold_cm)

# 2
balance = -1000000000000000000
print(balance >= 0)

# 3
temp = 18.001
print(temp < 18 or temp > 24)

# 4
new_score = 18
old_score = 14
print(new_score >= (old_score + 5))