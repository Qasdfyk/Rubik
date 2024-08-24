import pygame
import numpy as np
import math
import random

class RubiksCube:
    def __init__(self):
        self.vertices = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Front face (corners) 1-4
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],  # Back face (corners) 5-8

            [0, 0, 1], [0, 0, -1],      
            [0, 1, 0], [0, -1, 0],      # Center points 9-14
            [1, 0, 0], [-1, 0, 0], 
              
            [0, 1, -1], [1, 0, -1], 
            [-1, 0, -1], [0, -1, -1],   # Front middle points 15-18

            [0, 1, 1], [1, 0, 1],
            [-1, 0, 1], [0, -1, 1],     # Back middle point 19-22

            [-1, 1, 0], [-1, -1, 0],    # Left middle 23-24
            [1, 1, 0], [1, -1, 0],      # Right middle 25 -26
        ]


        # Define face indices
        self.faces = [
            (10, 15, 4, 17), (10, 15, 3, 16), (10, 18, 1, 17), (10, 18, 2, 16),     # Front
            (9, 19, 8, 21), (9, 19, 7, 20), (9, 22, 5, 21), (9, 22, 6, 20),     # Back
            (12, 18, 1, 24), (12, 18, 2, 26), (12, 22, 5, 24), (12, 22, 6, 26),     # Bottom
            (11, 15, 4, 23), (11, 15, 3, 25), (11, 19, 8, 23), (11, 19, 7, 25),     # Top
            (14, 23, 8, 21), (14, 23, 4, 17), (14, 24, 5, 21), (14, 24, 1, 17),     # Left
            (13, 25, 3, 16), (13, 25, 7, 20), (13, 26, 2, 16), (13, 26, 6, 20),     # Right
        ]

        # Keeping indexes
        self.faces_dict = {face: i for i, face in enumerate(self.faces)}

        # Initialize face colors
        self.colors = [
            [255, 0, 0],    # Red
            [255, 165, 0],  # Orange            
            [0, 0, 255],    # Blue
            [0, 255, 0],    # Green
            [255, 255, 0],  # Yellow
            [255, 255, 255] # White
        ]
        self.face_colors = []
        for element in self.colors:
            self.face_colors.extend([element] * 4)
        

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

        t = self.find_closest_points(rotated_points[8:14], np.array([0,0,-10]))
        closest_centers_indexes = [index + 8 for index in t]

        sorted_faces = []
        for face in self.faces:
            if (face[0]-1) == closest_centers_indexes[0]:
                sorted_faces.insert(0, face)   
            elif (face[0]-1) == closest_centers_indexes[1]:
                sorted_faces.insert(4, face)
            elif (face[0]-1) == closest_centers_indexes[2]:
                sorted_faces.insert(8, face)
        sorted_faces.reverse()

        for face in sorted_faces:
            i = self.faces_dict[face]
            points = [projected_points[j-1] for j in face]
            pygame.draw.polygon(screen, self.face_colors[i], points)
        

    def find_closest_points(self, points, reference_point, n=3):
        distances = np.linalg.norm(points - reference_point, axis=1)
        distance_index_pairs = list(enumerate(distances))
        sorted_pairs = sorted(distance_index_pairs, key=lambda x: x[1])
        
        unique_indices = []
        seen_points = set()

        for index, dist in sorted_pairs:
            point_tuple = tuple(points[index])
            if point_tuple not in seen_points:
                unique_indices.append(index)
                seen_points.add(point_tuple)
            if len(unique_indices) == n:
                break
        return unique_indices
