str1 = "hello"
str2 = "alpha"
str3 = "bet"
str4 = "alphabet"


print(len(str1)) # len() is the number of characters in a string
print(len(str4)) # the length is one more than the largest positive index
print(len("Ryan")) # It has a length of 4, the largest positive index is 3. 
print(len("Enzo")) # It has a length of 4, the largest positive index is 3. 

print(str4[3]) # accesses individual characters. You are printing character index #3. 
print(str4[-5]) # accesses the negative indecesses. You are still printing "h"

print("hello"[2]) # It prints out L and in H E L L O, L is index #2. 
print("hello"[-3]) # Accesses the negative indecesses. 

# print("hello"[1])  - IndexError: string index out of range
# print("hello"[len("hello")]) - IndexError: string index out of range ---- because hello[5] biggest index is 4


# [star:end:step] is the general formula for more than one letter. 

print(str4[2:5]) # You must do one too many indexes as Python is non-inclusive. it will not count the value we stop at. 

print("Enzo"[2:4]) # notice how we go one index too many to get "Zo".2 inclusive and 4 exclusive which means indexes 2 to 3 inclusive. 

print("alphabet"[5:8]) # 5 inclusive to 8 exclusive which is the same as 5 to 7 inclusive. 
print("alphabet"[-3:0]) # this does not work as you cannot go to 0. 
print("alphabet"[-3:]) # prints "bet"
print("alphabet"[5:]) # prints "bet"

# All four of these version WILL work. 

print("0123456789"[0:10:2]) # "02468" this goes from 0 to 9, but the "2" skips every other number. 
print("0123456789"[0:10:3]) # "0369" goes from 0 to 9 and skips by 3
print("0123456789"[-1:-11:-1]) # "9876543210" goes backwards with all negatives

# This is teaches stepping

print("alphabet"[::2]) # "apae" steps from 2. 
print("alphabet"[2::2]) # "pae" starts from p, and skips 2. 


