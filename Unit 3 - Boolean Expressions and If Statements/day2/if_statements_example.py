# 1) Temperature classifier (°C):
#    Print one of: cold (<0), cool (0–15), warm (16–25), hot (>25) based on temp_c.
temp_c = 23
if temp_c < 0:
    print("cold")
elif temp_c < 15: # else means that the stuff above was not true 
    print("cool")
elif temp_c < 25:
    print("warm")
else: # This means the "thing" above was NOT true
    print("hot")


# 2) Letter grades:
#    Print A (90+), B (80–89), C (70–79), D (60–69), or F (<60) based on percent.
percent = 85
if percent >= 90:
    print("A")
elif percent >= 80:
    print("B")
elif percent >= 70: 
    print("C")
elif percent >= 60:
    print("D")
else:
    print("F")

# 3) Password strength by length:
#    Print weak (<8), ok (8–11), or strong (12+) using len(password).
password = "qwerty"
if len(password) < 8:
    print("weak")
elif len(password) < 11:
    print("ok")
else:
    print("strong")

# 4) Greeting by hour (0–23):
#    Print Good morning (5–11), Good afternoon (12–16), Good evening (17–21), or Good night (other).

# Slow way to write
hour = 14
if hour >= 5 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 21:
    print("Good Evening")
else:
    print("Good Night")

# Quicker way to write, you cannot do it in Java!
hour = 14
if 5>= hour <=11:
    print("Good Morning")
elif 12>= hour <=16:
    print("Good Afternoon")
elif 17>= hour <=21:
    print("Good Evening")
else:
    print("Good Night")



# 5) Course code (strings):
#    If it begins with "ics" (case-insensitive) print "Computer Studies".
#    Elif it ends with "py" print "Python file".
#    Else print "Unknown".
#    (Use only lower(), len(), and slicing.)
course = "ICS3u"
if (course[:3].lower() == "ics"):
    print("Computer Science")
elif (course[-2:].lower() == "py"):
    print("Python File")
else:
    "Unknown"

# Homework

# 6) Ticket price category by age:
#    Print child (0–12), student (13–17), adult (18–64), or senior (65+).
age = 23
if age <=12:
    print("child")
elif age <=17:
    print("Student")
elif age <=64:
    print("Adult")
else:
    print("Senior")

# 7) Shipping fee by weight (kg):
#    Print light (<=1.0), standard (<=5.0), or heavy (>5.0).
weight = 6
if weight <=1:
    print("Light")
elif weight <=5:
    print("Standard")
else:
    print("Heavy")

# 8) Honour roll:
#    If gpa >= 3.7 and attendance >= 95, print "Honour Roll".
#    Elif gpa >= 3.0, print "Good Standing".
#    Else print "Keep Going".

gpa = 4
attendance = 95
if gpa >=3.7 and attendance >=95:
    print("Honour Roll")
elif gpa >=3:
    print("Good Standing")
else: 
    print("Keep Going")

# 9) File type by extension (strings):
#    If filename ends with ".py" -> print "Python".
#    Elif it ends with ".txt" -> print "Text".
#    Else -> "Other".
#    (Use only lower() and slicing.)

file = "kraft.py"
if file.lower()[-3:] == ".py":
    print("Python File")
elif file.lower()[-4:] == ".txt":
    print("Text File")
else:
    print("Other")

# 10) Team placement (ints/floats):
#    If age < 13 -> "U13".
#    Elif 13–14 and height_m >= 1.65 -> "U15-Tall".
#    Elif 13–14 and height_m < 1.65 -> "U15".
#    Else -> "U17+".

age = 15
height = 1.6
if age < 13:
    print("U13")
elif 13>= age <=14 and height >=1.65:
    print("U15-Tall")
elif 13>= age <=14 and height >1.65:
    print("U15")
else:
    print("U17+")

# Challenge (optional):
#    Rewrite #8 using a nested if inside the gpa >= 3.7 branch (check attendance inside).