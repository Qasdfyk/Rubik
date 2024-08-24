colors = [
        [255, 0, 0],    # Red
        [0, 255, 0],    # Green
        [0, 0, 255],    # Blue
        [255, 255, 0],  # Yellow
        [255, 165, 0],  # Orange
        [255, 255, 255] # White
    ]

expanded_list = []
for element in colors:
    expanded_list.extend([element] * 4)

print(expanded_list)