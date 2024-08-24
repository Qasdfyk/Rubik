faces = [
    (10, 15, 4, 17), (10, 15, 3, 16), (10, 18, 1, 17), (10, 18, 2, 16),     # Front
    (9, 19, 8, 21), (9, 19, 7, 20), (9, 22, 5, 21), (9, 22, 6, 20),     # Back
    (12, 18, 1, 24), (12, 18, 2, 26), (12, 22, 5, 24), (12, 22, 6, 26),     # Bottom
    (11, 15, 4, 23), (11, 15, 3, 25), (11, 19, 8, 23), (11, 19, 7, 25),     # Top
    (14, 23, 8, 21), (14, 23, 4, 17), (14, 24, 5, 21), (14, 24, 1, 17),     # Left
    (13, 25, 3, 16), (13, 25, 7, 20), (13, 26, 2, 16), (13, 26, 6, 20),     # Right
]

t = enumerate(faces)
faces_dict = {face: i for i, face in enumerate(faces)}
print(faces_dict)
sorted_faces_dict = {}