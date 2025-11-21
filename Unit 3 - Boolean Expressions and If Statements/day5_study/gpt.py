# 1. Library Late-Night Access
# A student can stay in the library after 9 pm only if:
# - They are working on a verified school project AND have their ID card
#   OR
# - They are with a tutor who has late-access permission
# Write a function late_access(project, hasID, withTutor) that returns True if they may stay.

def late_access(project, hasID, withTutor):
    if withTutor:
        return True
    elif project and hasID:
        return True
    else:
        return False


# 2. Robot Malfunction Warning
# A robot is malfunctioning if:
# - Its temperature is above 80°, OR
# - Its battery is below 10% AND it is currently moving, OR
# - Someone pressed the emergency stop button
# Write malfunction(temp, battery, moving, emergency).

def malfunction(temp, battery, moving, emergency):
    if emergency:
        return True
    elif battery < 10 and moving:
        return True
    elif temp > 80:
        return True
    else:
        return False


# 3. Arcade Bonus Ticket Machine
# BONUS ticket rules:
# - Score < 1000 → 0 bonus
# - Score 1000–1999 → 10 bonus
# - Score ≥ 2000 → 20 bonus
# - If it’s double-ticket hour, add +10
# Write bonus_tickets(score, doubleHour).

def bonus_tickets(score, doubleHour):
    if doubleHour and score >= 2000:
        return 30
    elif doubleHour and 1000 <= score <= 1999:
        return 20
    elif doubleHour and score < 1000:
        return 10
    elif doubleHour and score >= 2000:
        return 20
    elif doubleHour and score < 1000:
        return 0
    else:
        return 10



# 4. Near a Multiple of 9
# A number counts as “close to a multiple of 9” if:
# - It is exactly 1 or 2 away from a positive multiple of 9,
# - AND the number is ≥ 10
# Write near_nine(n).

def near_nine(n):
    if n < 10:
        return False
    elif n % 9 <= 2 or n % 9 >= 7:
        return True
    else:
        return False


# 5. Almost Perfect Attendance
# A student is “almost perfect” if:
# - They attended at least 95% of classes, OR
# - They attended 90–94% AND completed all assignments
# Write almost_perfect(attendPercent, assignmentsDone).

def almost_perfect(attendPercent, assignmentsDone):
    if 90 <= attendPercent <= 94 and assignmentsDone:
        return True
    elif attendPercent >= 95:
        return True
    else:
        return False


# 6. Cookie Thief Detector 2.0
# A cookie was stolen if ANY of these are true:
# - Crumbs on the floor AND the cookie jar is open
# - The dog is suspiciously quiet
# - The camera caught movement near the jar
# Write cookie_stolen(openJar, crumbs, quietDog, movement).

def cookie_stolen(openJar, crumbs, quietDog, movement):
    if movement:
        return True
    elif quietDog:
        return True
    elif crumbs and openJar:
        return True
    else:
        return False


# 7. Angry Blender
# The blender is angry if:
# - Speed is 5, OR
# - Someone pressed “blend” while the lid is off
# BUT:
# - If it’s unplugged, it cannot be angry
# Write angry_blender(speed, lidOn, pluggedIn).

def angry_blender(speed, lidOn, pluggedIn, pressedBlend):
    if pluggedIn == False:
        return False
    elif lidOn == False and pressedBlend:
        return True
    elif speed == 5:
        return True
    else:
        return False


# 8. Drama Goat
# A goat becomes dramatic if:
# - You approach closer than 1 meter, OR
# - It sees another goat being fed, OR
# - There is loud music nearby
# Write drama_goat(distance, seesFeeding, loudMusic).

def drama_goat(distance, seesFeeding, loudMusic):
    if loudMusic:
        return True
    elif seesFeeding:
        return True
    elif distance < 1:
        return True
    else:
        return False


# 9. Laptop Overheat Panic
# The laptop panics if:
# - CPU > 90% AND temperature > 85°C
# UNLESS it is in cooling mode → then no panic.
# Write overheat(cpu, temp, coolingMode).

def overheat(cpu, temp, coolingMode):
    if coolingMode:
        return False
    elif cpu > 90 and temp > 85:
        return True
    else:
        return False


# 10. Spaceship Auto-Launch Check
# The ship may auto-launch if:
# - Fuel ≥ 70%, OR
# - The pilot is on board, OR
# - Mission control gives remote clearance
# BUT:
# - If a critical warning is active, auto-launch never occurs
# Write launch_ready(fuel, pilot, remoteOK, criticalWarning).

def launch_ready(fuel, pilot, remoteOK, criticalWarning):
    if criticalWarning:
        return False
    elif remoteOK or pilot or fuel >= 70:
        return True
    else:
        return False
       
