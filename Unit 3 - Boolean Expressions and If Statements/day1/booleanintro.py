age = 15
print(age >= 16)         # license threshold

temp_c = -2
print(temp_c <= 0)       # freezing or below

speed = 72
limit = 80
print(speed > limit)     # speeding?

length = 19.9
target = 20.0
print(length != target)

username = "Admin"
print(username.lower() == "admin") # true

msg = "System OK"
print("ok" in msg.lower()) # True, ok is in "System OK".lower()

password = "secret42"
print(len(password) >= 8) # True

word = "preheating"
print(word[:3].lower() == "pre")  # starts with
print(word[-3:].lower() == "ing") # ends with

title = "The Hobbit"
print(title[:3].lower() == "the") # True

name = "maria"
print(name != "" and name[0].lower() < "m")  # alphabet check (guard empty)
# Making sure that name is not an empty string. If name was an empty string, it would crash. 
# And means that both of them have to be true. 