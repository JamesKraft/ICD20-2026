# Title: pressure_plate
# Language: Python

# Description:
# You are trying to activate a dungeon pressure plate.
# The plate activates if any of these conditions are true:

# Your weight is at least the plateLevel.

# You have a gem and the gem matches the plate color.

# You have a companion who is heavy and the plateLevel is 50 or below.

# Return True if the plate activates.

# Examples:
# pressure_plate(40, 30, False, False, False, False) → True
# pressure_plate(20, 50, True, True, False, False) → True
# pressure_plate(20, 60, False, False, True, False) → False

# Starter Code:

def pressure_plate(weight, plateLevel, hasGem, gemMatches, hasCompanion, companionHeavy):
    if hasCompanion and companionHeavy and plateLevel <= 50:
        return True
    elif hasGem and gemMatches:
        return True
    elif weight >= plateLevel:
        return True
    else:
        return False



# Title: catches_bus
# Language: Python

# Description:
# A student catches the bus if they arrive 1 to 7 minutes before the bus departure time.
# Times are given in HHMM format, but you must compute real minutes.

# Arriving exactly at departure time or after is too late.
# Arriving more than 7 minutes early is also too early.

# Return True if they catch the bus.

# Examples:
# catches_bus(815, 814) → True
# catches_bus(815, 808) → True
# catches_bus(815, 807) → False

# Starter Code:

def catches_bus(depart, arrive):
    dpt = ((depart//100)*60) + depart%100
    arv = ((arrive//100)*60) + arrive%100
    if (1 <= (dpt - arv) <= 7):
        return True
    else:
        return False






# Title: unsafe
# Language: Python

# Description:
# Two workers are in a lab. The environment is unsafe if:

# Either worker is absent, or

# Both workers are present but neither is wearing gloves.

# Return True if the situation is unsafe.

# Examples:
# unsafe(True, False, True, True) → True
# unsafe(True, True, False, False) → True
# unsafe(True, True, True, False) → False

# Starter Code:

def unsafe(w1_present, w2_present, w1_gloves, w2_gloves):
    if w1_present and w2_present and (w1_gloves == False and w2_gloves == False):
        return True
    elif w1_present == False or w2_present == False:
        return True
    else:
        return False






# Title: gate_unlocks
# Language: Python

# Description:
# An alien gate unlocks if any of these are true:

# Your badgeLevel ≥ requiredLevel

# You have a valid security code (hasCode and not codeExpired)

# A robot assistant is with you, is charged, and requiredLevel ≤ 10

# Return True if the gate unlocks.

# Examples:
# gate_unlocks(4, 3, False, False, False, False) → True
# gate_unlocks(2, 5, True, False, False, False) → True
# gate_unlocks(3, 8, False, False, True, False) → False

# Starter Code:

def gate_unlocks(badgeLevel, requiredLevel, hasCode, codeExpired, robotAssistant, robotCharged):
    if robotAssistant and robotCharged and requiredLevel <= 10:
        return True
    elif hasCode and codeExpired == False:
        return True
    elif badgeLevel >= requiredLevel:
        return True
    else:
        return False






# Title: early_bird
# Language: Python

# Description:
# A store gives an “early bird” discount if a customer arrives
# 3 to 12 minutes before opening.

# Times are HHMM format.
# Arriving earlier than 12 minutes early or at/after opening does not qualify.

# Return True if they get the discount.

# Examples:
# early_bird(900, 852) → True
# early_bird(900, 847) → False
# early_bird(900, 859) → False

# Starter Code:

def early_bird(openTime, arriveTime):
    open = ((openTime//100)*60)+openTime%100
    arrive = ((arriveTime//100)*60)+arriveTime%100
    if (3 <= (open-arrive) <= 12):
        return True
    else:
        return False








# Title: study_trouble
# Language: Python

# Description:
# Two students meet to study. Trouble happens if:

# Either student is absent, or

# Both are present but neither brought notes.

# Return True if they are in trouble.

# Examples:
# study_trouble(True, False, True, True) → True
# study_trouble(True, True, False, False) → True
# study_trouble(True, True, True, False) → False

# Starter Code:

def study_trouble(s1_present, s2_present, s1_notes, s2_notes):
    if s1_present and s2_present and (s1_notes == False and s2_notes == False):
        return True
    elif s1_present == False or s2_present == False:
        return True
    else:
        return False







# Title: bridge_lowers
# Language: Python

# Description:
# A castle drawbridge lowers if:

# You have the royal token and bridgeDiff ≤ 7

# You know the chant and bridgeDiff ≤ 10

# Your bravery ≥ 3 × bridgeDiff

# Your squire is with you, not scared, and bridgeDiff ≤ 12

# Return True if the bridge lowers.

# Examples:
# bridge_lowers(True, False, 10, 7, False, False) → True
# bridge_lowers(False, True, 5, 11, False, False) → False
# bridge_lowers(False, False, 36, 12, False, False) → True

# Starter Code:

def bridge_lowers(hasRoyalToken, knowsChant, bravery, bridgeDiff, squire, squireScared):
    if squire and squireScared == False and bridgeDiff <= 12:
        return True
    elif bravery >= (3*bridgeDiff):
        return True
    elif knowsChant and bridgeDiff <= 10:
        return True
    elif hasRoyalToken and bridgeDiff <= 7:
        return True
    else:
        return False






# Title: precise
# Language: Python

# Description:
# A delivery is considered “precisely timed” if the driver arrives
# 2–4 minutes before the scheduled time.

# Times are HHMM format.
# Arriving earlier than 4 minutes early or at/after scheduled time is invalid.

# Return True if arrival is precise.

# Examples:
# precise(1100, 1058) → True
# precise(1100, 1056) → False
# precise(1100, 1100) → False

# Starter Code:

def precise(scheduled, arrive):
    sch = ((scheduled//100)*60)+scheduled%100
    arv = ((arrive//100)*60)+arrive%100
    if (2 <= (sch - arv) <= 4):
        return True
    else:
        return False








# Title: robot_trouble
# Language: Python

# Description:
# You work with a robot assistant. Trouble happens if:

# The robot is offline, or

# You are absent, or

# Both are present but neither has a safety shield active.

# Return True if there is trouble.

# Examples:
# robot_trouble(True, False, True, True) → True
# robot_trouble(False, True, True, True) → True
# robot_trouble(True, True, False, False) → True

# Starter Code:

def robot_trouble(you_present, robot_online, you_shield, robot_shield):
    if you_present and robot_online and (you_shield == False and robot_shield == False):
        return True
    elif robot_online == False or you_present == False:
        return True
    else:
        return False







# Title: elevator_on
# Language: Python

# Description:
# An enchanted tower elevator activates if:

# You have the correct rune (hasRune and runeMatches),

# OR your energy ≥ 4 × floorDifficulty,

# OR the spirit guide is with you, not distracted, and floorDifficulty ≤ 15

# Return True if the elevator activates.

# Examples:
# elevator_on(True, True, 10, 20, False, False) → True
# elevator_on(False, False, 100, 30, False, False) → True
# elevator_on(True, False, 5, 3, False, False) → False

# Starter Code:

def elevator_on(hasRune, runeMatches, energy, floorDifficulty, spiritGuide, guideDistracted):
    if spiritGuide and guideDistracted == False and floorDifficulty <= 15:
        return True
    elif energy >= (4*floorDifficulty):
        return True
    elif hasRune and runeMatches:
        return True
    else:
        return False