data = [
    ["Kirmizi", 20, "Kum", 42, "Cam"],
    ["Kirmizi", 45, "Demir", 34, "Metal"],
    ["Kirmizi", 12, "Petrol", 25, "Plastik"],
    ["Kirmizi", 7, "Agac", 9, "Kagit"],
    ["Kirmizi", 18, "Kum", 40, "Cam"],
    ["Kirmizi", 41, "Demir", 39, "Metal"],
    ["Kirmizi", 15, "Petrol", 22, "Plastik"],
    ["Kirmizi", 5, "Agac", 7, "Kagit"]
]

color_index = 0
color_no = {}
index = 1

for row in data:
    for i in range(len(row)):
        if i != color_index and isinstance(row[i], str):
            if row[i] not in color_no:
                color_no[row[i]] = index
                index += 1
            row[i] = color_no[row[i]]

for row in data:
    print(row)