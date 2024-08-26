import numpy as np
import math

pi = np.pi

def normalize(angle):
    while angle<=-pi:
        angle+=2*pi
    while angle>pi:
        angle-=2*pi
    return angle

def get_rotation_matrix(angle_x, angle_y):
    rotation_x = np.array([
        [1, 0, 0],
        [0, math.cos(angle_x), -math.sin(angle_x)],
        [0, math.sin(angle_x), math.cos(angle_x)]
    ])

    rotation_y = np.array([
        [math.cos(angle_y), 0, math.sin(angle_y)],
        [0, 1, 0],
        [-math.sin(angle_y), 0, math.cos(angle_y)]
    ])

    rotation_matrix = np.dot(rotation_y, rotation_x)
    return rotation_matrix
