# General "if" structure
# if condition_1:
    # do something
# elif condition_2:
    # do something else
# else:
# if nothing is true, do this
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

# This Question is ON THE TEST AKA what will the code read and in which order. 
# The most likely version should be the first one to read, as the code will be more efficient. 
# The answer is time complexity and it will be more efficient. 