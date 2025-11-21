# 1. Smart Thermostat Temperature Alert
# Your house has a smart thermostat that decides when to send you a temperature alert.
# Parameters:
#   temp        – current indoor temperature
#   away        – True if you are not home
#   windowsOpen – True if any windows are open
#   ecoMode     – True if eco mode is enabled
#
# Rules:
# Normal mode (ecoMode == False):
#   - If you are away AND the temperature goes below 15°C, alert = True
#   - If the windows are open AND temp > 28°C, alert = True
#
# Eco mode:
#   - Alerts only happen if temp < 10°C OR temp > 30°C
#
# Write a function that returns True if an alert should be sent.
#
# Examples:
# temp_alert(14, True, False, False) → True
# temp_alert(29, False, True, False) → True
# temp_alert(31, False, False, True) → True

def temp_alert(temp, away, windowsOpen, ecoMode):
    if ecoMode and (temp < 10 or temp > 30):
        return True
    elif ecoMode == False and windowsOpen and temp > 28:
        return True
    elif ecoMode == False and temp < 15 and away:
        return True
    else:
        return False





# 2. Smart Refrigerator Warning System
# Your smart fridge warns you under certain food-related conditions.
# Parameters:
#   milkDays     – how many days old the milk is
#   doorOpen     – True if the fridge door is currently open
#   powerSaving  – True if the fridge is in power-saving mode
#   overload     – True if the fridge is overloaded with items
#
# Rules:
# - If the milk is 7+ days old, warn = True
# - If the door is open for more than 30 seconds (doorOpen == True), warn = True
# - If in power-saving mode:
#       warnings only occur if the fridge is overloaded OR the milk is 10+ days old
# - If not in power-saving mode:
#       normal rules apply (milk 7+, or doorOpen)
#
# Write a function that returns True if a warning should be displayed.
#
# Examples:
# fridge_warning(8, False, False, False) → True
# fridge_warning(5, True, False, False) → True
# fridge_warning(9, False, True, True) → True

def fridge_warning(milkDays, doorOpen, powerSaving, overload):
    if powerSaving == False and (milkDays >= 7 or doorOpen):
        return True
    elif powerSaving and (overload or milkDays >= 10):
        return True
    elif doorOpen == True and powerSaving == False:
        return True
    elif milkDays >= 7 and powerSaving == False:
        return True
    else:
        return False










# 3. Dragon Encounter Safety Check
# You encounter a dragon in a fantasy game.
# Parameters:
#   hasShield     – True if you have a dragon-proof shield
#   stealthSkill  – your stealth level (0–10)
#   dragonAwake   – True if the dragon is awake
#   fireResist    – True if you have fire resistance
#   distance      – distance from the dragon in meters
#
# Rules:
# - You are safe if:
#       • The dragon is asleep AND your stealthSkill >= 4
#       • OR you have a shield AND you are at least 5 meters away
#       • OR you have fire resistance AND you are more than 10 meters away
#
# - But:
#       If the dragon is awake AND you have no shield AND no fire resistance,
#       you are NEVER safe regardless of distance.
#
# Write a function that returns True if you are safe.
#
# Examples:
# dragon_safe(True, 3, True, False, 6) → True
# dragon_safe(False, 7, False, False, 12) → True
# dragon_safe(False, 3, True, False, 20) → False

def dragon_safe(hasShield, stealthSkill, dragonAwake, fireResist, distance):
    if dragonAwake and hasShield == False and fireResist == False:
        return False
    elif fireResist and distance > 10:
        return True
    elif hasShield and distance > 5:
        return True
    elif dragonAwake == False and stealthSkill >= 4:
        return True
    else:
        return False
