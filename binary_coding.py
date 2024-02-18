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

category_columns = ["Cam", "Metal", "Plastik", "Kagit"]

for row in data:
    for category in category_columns:
        row.append(1 if category in row else 0)
        
for row in data:
    print(row)