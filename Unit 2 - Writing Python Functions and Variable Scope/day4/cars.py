observations = {
    1: {
        "time": "2:38",
        "cars": 100,
        "pedestrians": 7,
        "bikes": 1,
        "intersection_type": "Traffic Light",
        "infractions": "None",
        "notes": "sunny/busy"
    },
    2: {
        "time": "2:40",
        "cars": 81,
        "pedestrians": 4,
        "bikes": 0,
        "intersection_type": "Traffic Light",
        "infractions": "None",
        "notes": "Air getting warmer"
    },
    3: {
        "time": "2:42",
        "cars": 74,
        "pedestrians": 8,
        "bikes": 0,
        "intersection_type": "Traffic Light",
        "infractions": "None",
        "notes": "2 TTC buses"
    },
    4: {
        "time": "2:44",
        "cars": 60,
        "pedestrians": 11,
        "bikes": 0,
        "intersection_type": "Traffic Light",
        "infractions": "None",
        "notes": "Large dump truck"
    },
    5: {
        "time": "2:46",
        "cars": 80,
        "pedestrians": 3,
        "bikes": 0,
        "intersection_type": "Traffic Light",
        "infractions": "None",
        "notes": "Blue Porsche spotted"
    },
    6: {
        "time": "2:48",
        "cars": 67,
        "pedestrians": 2,
        "bikes": 2,
        "intersection_type": "Traffic Light",
        "infractions": "Bike riding on sidewalk",
        "notes": "Sunny weather"
    },
    7: {
        "time": "2:50",
        "cars": 76,
        "pedestrians": 6,
        "bikes": 0,
        "intersection_type": "Traffic Light",
        "infractions": "None",
        "notes": "Sunny weather, lots of traffic"
    }
}


# ===============================
#   ACCESSING A SINGLE OBSERVATION
# ===============================

def get_observation(observations, number):
    # Returns the observation dictionary for a specific observation number.
    # For example: get_observation(observations, 1) returns the first observation.
    # Returns: dict (e.g. {'time': '10:05', 'cars': 14, ...})
    return observations[number]


# ===============================
#   ACCESSING INDIVIDUAL DATA POINTS
# ===============================

def get_observation_time(obs):
    # Returns the time string from a single observation.
    # Returns: str
    return obs["time"]

def get_observation_cars(obs):
    # Returns the number of cars counted during one observation.
    # Returns: int
    return obs["cars"]

def get_observation_pedestrians(obs):
    # Returns the number of pedestrians counted during one observation.
    # Returns: int
    return obs["pedestrians"]

def get_observation_bikes(obs):
    # Returns the number of bikes counted during one observation.
    # Returns: int
    return obs["bikes"]

def get_observation_type(obs):
    # Returns the type of intersection (e.g. '4-way stop', 'Traffic light').
    # Returns: str
    return obs["intersection_type"]

def get_observation_notes(obs):
    # Returns the notes recorded for a single observation.
    # Returns: str
    return obs["notes"]


# ===============================
#   AGGREGATION FUNCTIONS (WORK FOR ANY SIZE DICTIONARY)
# ===============================

def get_num_observations(observations):
    # Returns the total number of observations recorded.
    # Returns: int
    return len(observations)

def get_total_cars(observations):
    # Calculates the total number of cars across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_cars(obs)
    return total

def get_total_pedestrians(observations):
    # Calculates the total number of pedestrians across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_pedestrians(obs)
    return total

def get_average_bikes(observations):
    # Calculates the average number of bikes per observation.
    # Returns: float
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_bikes(obs)
    return total / get_num_observations(observations)


# ===============================
#   FORMATTING & PRINTING HELPERS
# ===============================

def format_observation_row(obs_num):
    # Takes in an observation number (#1-7)
    # formats a single row of observations for use in the table
    # Returns: str (a nicely formatted line of code)
    obs = get_observation(observations, obs_num)
    print(f"{obs_num:<6} | {get_observation_time(obs)} | {get_observation_cars(obs)} | {get_observation_pedestrians(obs)} | {get_observation_bikes(obs)} | {get_observation_type(obs)} | {get_observation_notes(obs)}") # replace print with your code

def print_table_header():
    # Prints the header section for the table of observations.
    # Returns: None
    return(f" obs # | Time  | Cars | Peds | Bikes | Types   | Notes")

def print_totals(get_total_cars, get_total_pedestrians, get_average_bikes):
    # Prints the total cars, total pedestrians, and average bikes
    # after all observations are displayed.
    # Returns: None
    print(f"TOTAL CARS: {get_total_cars(observations)}")
    print(f"TOTAL PEDESTRIANS: {get_total_pedestrians(observations)}")
    print(f"AVERAGE BIKES: {get_average_bikes(observations)}")

print("INTERSECTION OBSERVATIONS")
print("-"*100) # Prints one hundred dashes in chart
print(print_table_header()) # Prints table header
print("-"*100)

for ob in observations: 
    print(format_observation_row(ob)) # Function prints all of the rows

# starting

print("-"*100)
print_totals(get_total_cars, get_total_pedestrians, get_average_bikes)


