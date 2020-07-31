# Your name
# Your class-section

# DO NOT CHANGE
import random
import math
import kmeans_viz
import kmeans_data

# TODO
# Returns a list (of length pigeons) in which
# each value is a valid and distinct number
# in the range [0, holes).
# When selecting each value, each should have an
# equal chance of being selected.
# Input: number of pigeons,
#        number of holes
# Output: list of length pigeons assigning
#         each pigeon to a hole
def distinct_random_assignment(pigeons, holes):
    result = []

    # == Follow these directions! ==
    # 1. Loop for each pigeon
    #    (a) Loop until done
    #        i.  Randomly select a value for the current pigeon
    #        ii. If it hasn't been previously assigned,
    #            add to the end of the result

    return result


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def init_centroids(data, colors):
    k = len(colors)

    assignment = distinct_random_assignment(k, len(data))

    initcentroids = []
    for i in range(k):
        initcentroids.append([colors[i], data[assignment[i]]])

    return initcentroids


# TODO
# Compute the Euclidean distance
# between the supplied points
# Input: point1 point2 (assumed same length)
# Output: distance
def dist(p1, p2):
    # You MUST use at least one function
    # from the math module
    return 0 # your code here


# TODO
# Using a supplied distance function,
# find the index of the point in a dataset
# of options that is closest to a supplied point
# Input: point,
#        list of points,
#        distance function: df(p1, p2) -> #
# Output: index of closest option
def find_closest(p, options, df):
    return 0 # your code here


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def assign_to_closest(data, centroids):
    k = len(centroids)

    assignment = []
    options = []
    for c in range(k):
        assignment.append([])
        options.append(centroids[c][1])

    for p in data:
        assignment[find_closest(p, options, dist)].append(p)

    return assignment


# TODO
# Given a list of points,
# produce a point that is the dimension-wise
# average (i.e. dimension k is the average
# of all the dimension k values in the dataset)
# Input: dataset of points
# Output: list of average values
def avg_point(coordinates):
    return 0 # your code here


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def update_centroids(centroids, assignment):
    for c in range(len(centroids)):
        centroids[c][1] = avg_point(assignment[c])


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def kmeans(data, colors):
    kmeans_viz.title("Draw Data")
    for p in data:
        kmeans_viz.draw_point("purple", p[0], p[1])
    kmeans_viz.wait()

    kmeans_viz.title("Draw Initial Centroids")
    centroids = init_centroids(data, colors)
    kmeans_viz.draw_centroids(centroids)
    kmeans_viz.wait()

    kmeans_viz.title("Draw Initial Assignment")
    oldassignment = assign_to_closest(data, centroids)
    kmeans_viz.draw_assignment(centroids, oldassignment)

    kmeans_viz.title("Update Centroids")
    update_centroids(centroids, oldassignment)
    kmeans_viz.draw_centroids(centroids)
    kmeans_viz.wait()

    done = False
    iteration = 1
    while not done:
        kmeans_viz.title("Iteration " + str(iteration))
        newassignment = assign_to_closest(data, centroids)
        update_centroids(centroids, newassignment)

        kmeans_viz.clear()
        kmeans_viz.draw_centroids(centroids)
        kmeans_viz.draw_assignment(centroids, newassignment)

        done = (oldassignment == newassignment)
        if not done:
            oldassignment = newassignment
            iteration += 1
            kmeans_viz.wait()

    return centroids


# DO NOT CHANGE
if __name__ == "__main__":

    random.seed(55513)
    kmeans_viz.setup(-60, -60, 60, 60, 0)

    centroids = kmeans(kmeans_data.SAMPLE, ["red", "blue", "black"])
    print(centroids)

    kmeans_viz.done()
