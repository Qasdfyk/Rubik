import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Cube Rotation")

# Define colors for each face of the cube
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255)   # Magenta
]

# Define cube vertices
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Define cube faces
faces = [
    (0, 1, 2, 3),  # Back
    (4, 5, 6, 7),  # Front
    (0, 1, 5, 4),  # Bottom
    (2, 3, 7, 6),  # Top
    (0, 3, 7, 4),  # Left
    (1, 2, 6, 5)   # Right
]

# Function to rotate points in 3D
def rotate(vertices, angle_x, angle_y):
    rotated_vertices = []
    cos_x = math.cos(angle_x)
    sin_x = math.sin(angle_x)
    cos_y = math.cos(angle_y)
    sin_y = math.sin(angle_y)

    for x, y, z in vertices:
        # Rotate around y-axis first (horizontal rotation)
        x, z = x * cos_y - z * sin_y, x * sin_y + z * cos_y
        # Rotate around x-axis (vertical rotation)
        y, z = y * cos_x + z * sin_x, -y * sin_x + z * cos_x
        rotated_vertices.append([x, y, z])

    return rotated_vertices

# Function to project 3D points to 2D
def project(vertices):
    projected_points = []
    scale = 300
    for x, y, z in vertices:
        factor = scale / (z + 5)  # Perspective division
        x, y = x * factor + width // 2, -y * factor + height // 2
        projected_points.append([x, y])

    return projected_points

# Main loop
running = True
angle_x = 0
angle_y = 0
clock = pygame.time.Clock()
dragging = False

while running:
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            dragging = True
            pygame.mouse.get_rel()  # Reset mouse movement
        elif event.type == MOUSEBUTTONUP:
            dragging = False

    if dragging:
        # Get mouse movement
        mx, my = pygame.mouse.get_rel()

        # Rotate cube based on mouse movement
        angle_x += my * 0.01  # Adjust X-axis rotation
        angle_y += mx * 0.01  # Adjust Y-axis rotation

    # Rotate and project cube vertices
    rotated_vertices = rotate(vertices, angle_x, angle_y)
    projected_points = project(rotated_vertices)

    # Calculate depth for sorting faces
    face_depths = []
    for i, face in enumerate(faces):
        depth = sum(rotated_vertices[vertex][2] for vertex in face) / 4
        face_depths.append((depth, i))

    # Sort faces by depth (from closest to farthest)
    face_depths.sort(reverse=True)  # Reverse to make closest faces drawn last

    # Draw faces sorted by depth
    for _, i in face_depths:
        face = faces[i]
        points = [projected_points[j] for j in face]
        pygame.draw.polygon(screen, colors[i], points)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
