# Question #1
height_cm = 2
threshold_cm = 0
print(height_cm >= threshold_cm)

# Question #2
balance = -1
print(balance >= 0)

# Question #3
temperature = 16
print(temperature <= 18 or temperature >= 24)

# Question #4
old_score = 10
new_score = 16
print(new_score >= old_score)

# Question #5
email = input("Enter your full email")
email_v2 = email[-10:]
print(email_v2.lower() == "@school.ca")

# Question #6
course = input("Enter your course code")
course_v2 = course[:3]
print(course_v2.lower() == "ics")

# Question #7
s = input("Enter a string")
print(s != "" and s[1] == "a" and s[-1] == "m")

# Question #8
python = input("Enter a string:")
print(len(python) == 5 and (python[:2]).lower() == "py")