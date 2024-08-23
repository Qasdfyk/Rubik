import pygame
import numpy as np
import math

class RubiksCube:
    def __init__(self):
        self.vertices = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Front face
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],  # Back face     
   
        ]
        self.points = [
            [0, 0, 1], [0, 0, -1],
            [0, 1, 0], [0, -1, 0],
            [1, 0, 0], [-1, 0, 0],     
        ]

        # Define face indices
        self.faces = [
            (0, 1, 2, 3),  # Front
            (4, 5, 6, 7),  # Back
            (0, 1, 5, 4),  # Bottom
            (2, 3, 7, 6),  # Top
            (0, 3, 7, 4),  # Left
            (1, 2, 6, 5)   # Right
        ]

        # Initialize face colors
        self.colors = [
            [255, 0, 0],    # Red
            [0, 255, 0],    # Green
            [0, 0, 255],    # Blue
            [255, 255, 0],  # Yellow
            [255, 165, 0],  # Orange
            [255, 255, 255] # White
        ]

        # Initialize face color mappings
        self.face_colors = [color[:] for color in self.colors]

    def rotate(self, angle_x, angle_y):
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

        rotated_points = []
        for vertex in self.vertices:
            rotated_vertex = np.dot(rotation_matrix, vertex)
            rotated_points.append(rotated_vertex)

        return rotated_points

    def project(self, vertices, width, height, scale=300):
        projected_points = []
        for x, y, z in vertices:
            factor = scale / (z + 5)
            x, y = x * factor + width // 2, -y * factor + height // 2
            projected_points.append([x, y])

        return projected_points

    def draw(self, screen, width, height, angle_x, angle_y):
        rotated_points = self.rotate(angle_x, angle_y)
        projected_points = self.project(rotated_points, width, height)

        face_depths = []
        for i, face in enumerate(self.faces):
            depth = sum(rotated_points[vertex][2] for vertex in face) / 4
            face_depths.append((depth, i))

        face_depths.sort(reverse=True)
        for _, i in face_depths:
            face = self.faces[i]
            points = [projected_points[j] for j in face]
            pygame.draw.polygon(screen, self.face_colors[i], points)



       
    def rotate_points(self, angle_x, angle_y):
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

        rotated_points = []
        for point in self.points:
            rotated_point = np.dot(rotation_matrix, point)
            rotated_points.append(rotated_point)

        return rotated_points  


    def draw_points(self, screen, width, height, angle_x, angle_y):
        rotated_points = self.rotate_points(angle_x, angle_y)

        reference_point = np.array([0, 0, -100])
        distances = np.linalg.norm(rotated_points - reference_point, axis=1)
        closest_point_index = np.argmin(distances)

        projected_points = self.project(rotated_points, width, height)
        print(rotated_points[closest_point_index])
        pygame.draw.circle(screen, [76, 0, 140], projected_points[closest_point_index], 5)

