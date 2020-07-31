# Your name
# Your class-section

# DO NOT CHANGE
import random
import math

# DO NOT CHANGE
# num_points = 100
# seed = 1073
# stdev = 10
# round_places = 2
# centers = "-1 25 -30 -12 17 -22"
SAMPLE = [
    [-32.97, -21.06], [9.01, -31.63], [-20.35, 28.73], [-0.18, 26.73], [-25.05, -9.56], [-0.13, 23.83], [19.88, -18.32], [17.49, -14.09], [17.85, 27.17], [-30.94, -8.85],
    [4.81, 42.22], [-4.59, 11.18], [9.96, -35.64], [24.72, -11.39], [14.44, -43.31], [-10.49, 33.55], [4.24, 31.54], [-27.12, -17.34], [25.24, -12.61], [20.26, -4.7],
    [-16.4, -19.22], [-15.31, -7.65], [-26.61, -20.31], [15.22, -30.33], [-29.3, -12.42], [-50.24, -21.18], [-32.67, -13.11], [-30.47, -17.6], [-23.25, -6.72], [23.08, -9.34],
    [-25.44, -6.09], [-37.91, -4.55], [0.14, 34.76], [7.93, 49.21], [-6.76, 12.14], [-19.13, -2.24], [12.65, -7.23], [11.25, 25.98], [-9.03, 22.77], [9.29, -26.2],
    [15.83, -1.45], [-22.98, -27.37], [-25.12, -23.35], [21.12, -26.68], [20.39, -24.66], [26.69, -28.45], [-45.42, -25.22], [-8.37, -21.09], [11.52, -16.15], [7.43, -32.89],
    [-31.94, -11.86], [14.48, -10.08], [0.63, -20.52], [9.86, 13.79], [-28.87, -17.15], [-29.67, -22.44], [-20.94, -22.59], [11.85, -9.23], [30.86, -21.06], [-3.8, 22.54],
    [-5.84, 21.71], [-7.01, 23.65], [22.5, -11.17], [-25.71, -14.13], [-32.62, -15.93], [-7.27, 12.77], [26.57, -13.77], [9.94, 26.95], [-22.45, -23.18], [-34.7, -5.62],
    [29.53, -22.88], [0.7, 31.02], [-22.52, -10.02], [-23.36, -14.54], [-19.44, -12.94], [-0.5, 23.36], [-45.27, -19.8], [8.95, 13.63], [47.16, -14.46], [5.57, 4.85],
    [-19.03, -25.41], [28.16, -13.86], [-15.42, -14.68], [10.19, -25.08], [0.44, 23.65], [-20.71, -20.94], [35.91, -20.07], [42.81, -21.88], [5.1, 9.33], [-15.8, -18.47],
    [5.39, -26.82], [-40.53, -17.16], [-29.54, 23.72], [7.8, 23.4], [-22.19, -27.76], [-23.48, -25.01], [-21.2, -21.74], [23.14, -24.14], [-28.13, -13.04], [-24.38, -6.79]]


# TODO
# Generate a random integer that is a valid
# index into the supplied list. All possible
# integers should have an equal chance of
# being selected (i.e. uniformly distrubuted).
# Input: list
# Output: valid index into list
def generate_center(centers):
    return 0 # your code here


# TODO
# Generate a number that has been rounded to the
# supplied number of decimal places.
# The number should be drawn from a Normal/Gaussian
# distribution with supplied mean and standard deviation.
# Input: mean, standard deviation, number of decimal places to round
# Output: rounded number
def generate_coordinate(mean, stdev, round_places):
    return 0 # your code here

# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def generate_point(centers, stdev, round_places):
    source = generate_center(centers)

    x = generate_coordinate(centers[source][0], stdev, round_places)
    y = generate_coordinate(centers[source][1], stdev, round_places)

    return [x, y]

# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def generate_dataset(num_points, seed, stdev, round_places, centers):
    dataset = []

    random.seed(seed)
    for i in range(num_points):
        dataset.append(generate_point(centers, stdev, round_places))

    return dataset


# TODO
# Finds the biggest or smallest value of a single dimension
# across a full dataset
# Input: list of points (each of equal dimension),
#        dimension of interest,
#        True if seeking the biggest value or False for smallest
# Output: biggest/smallest value that occurs in the dimension
#         of a dataset
def biggestsmallest(dataset, dimension, biggest):
    return 0 # your code here


# TODO
# Converts a space-separated list of
# numbers into a list-of-lists, each
# of a specified length.
# Input: space-separated string of numbers,
#        length of lists to be generated
# Output: list of lists where each sublist
#         is of the specified size
def numstring_to_lol(strnums, sublist_size):
    return [] # your code here


# DO NOT CHANGE
if __name__ == "__main__":
    num_points = int(input("Enter number of points to generate: "))
    seed = int(input("Enter seed for random number generator: "))
    stdev = float(input("Enter standard deviation: "))
    round_places = int(input("Enter places to round values: "))
    centers = input("Enter centroid centers (x1 y1 x2 y2 ...): ")

    #

    centers = numstring_to_lol(centers, 2)
    dataset = generate_dataset(num_points, seed, stdev, round_places, centers)

    #

    smallest_x = biggestsmallest(dataset, 0, False)
    biggest_x = biggestsmallest(dataset, 0, True)
    smallest_y = biggestsmallest(dataset, 1, False)
    biggest_y = biggestsmallest(dataset, 1, True)

    #

    print(dataset)
    print("X range:", math.floor(smallest_x), "to", math.ceil(biggest_x))
    print("Y range:", math.floor(smallest_y), "to", math.ceil(biggest_y))
