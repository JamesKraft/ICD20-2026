# 1
height_cm = 12
threshold_cm = 20
print(height_cm >= threshold_cm)

# 2
balance = -20
print(balance >= 0)

# 3
temp = 26
print((18 <= temp <= 24) == False)

# 4
new_score = 24
old_score = 20
print((new_score - old_score) >= 5)

# 5
email = "atolani@school.ca"
email_version = email[-10:]
print(email_version.lower() == "@school.ca")

# 6
course = input("Enter course code:")
course_v2 = course[0:3]
print(course_v2.lower() == "ics")

# 7
s = input("Enter a word that maybe begins with a and ends with m maybe...")
s_v2 = s[0]
s_v3 = s[-1]
print(s_v2.lower() == "a" and s_v3.lower() == "m")

# 8
python = input("Enter a word:")
python_len = len(python)
python_v2 = python[-2:]
print(python_len == 5 and python_v2.lower() == "py")