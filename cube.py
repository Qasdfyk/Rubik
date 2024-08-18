import pygame
import math
import numpy as np
from pygame.locals import *

class Cube:
    def __init__(self):
        self.vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ]
        
        self.faces = [
            (0, 1, 2, 3),  # Back
            (4, 5, 6, 7),  # Front
            (0, 1, 5, 4),  # Bottom
            (2, 3, 7, 6),  # Top
            (0, 3, 7, 4),  # Left
            (1, 2, 6, 5)   # Right
        ]

        self.colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (0, 255, 255),
            (255, 0, 255)
        ]

        # Identity matrix (no rotation initially)
        self.rotation_matrix = np.identity(3)

    def rotate(self, angle_x, angle_y):
        # Reset the rotation matrix for each frame
        self.rotation_matrix = np.identity(3)
        
        # Rotation matrices around the X and Y axes
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

        # Combine the new rotations with the current rotation matrix
        self.rotation_matrix = np.dot(rotation_y, rotation_x)

        rotated_vertices = []
        for vertex in self.vertices:
            rotated_vertex = np.dot(self.rotation_matrix, vertex)
            rotated_vertices.append(rotated_vertex)

        return rotated_vertices


    def project(self, vertices, width, height, scale=300):
        projected_points = []
        for x, y, z in vertices:
            factor = scale / (z + 5)
            x, y = x * factor + width // 2, -y * factor + height // 2
            projected_points.append([x, y])

        return projected_points

    def draw(self, screen, width, height, angle_x, angle_y):
        rotated_vertices = self.rotate(angle_x, angle_y)
        projected_points = self.project(rotated_vertices, width, height)

        face_depths = []
        for i, face in enumerate(self.faces):
            depth = sum(rotated_vertices[vertex][2] for vertex in face) / 4
            face_depths.append((depth, i))

        face_depths.sort(reverse=True)

        for _, i in face_depths:
            face = self.faces[i]
            points = [projected_points[j] for j in face]
            pygame.draw.polygon(screen, self.colors[i], points)