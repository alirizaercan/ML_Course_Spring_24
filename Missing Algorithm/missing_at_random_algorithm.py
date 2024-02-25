import random

file_path = "Missing Algorithm\data_second_week.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

data = []
for line in lines[1:]: 
    values = line.strip().split('\t')
    data.append([float(value) if value != '?' else None for value in values])

for col_index in range(len(data[0])):
    col_values = [row[col_index] for row in data]

    if any(value is None for value in col_values):
        for i in range(len(col_values)):
            if col_values[i] is None:
                buf = [value for value in col_values if value is not None]

                if buf:
                    mean_buf = sum(buf) / len(buf)

                    dis = [abs(mean_buf - value) for value in buf]

                    num_elements = len(buf)

                    min_index = max(0, int(i - max(dis)))
                    max_index = min(num_elements - 1, int(i + max(dis)))

                    random_index = random.randint(min_index, max_index)

                    data[i][col_index] = buf[random_index]

print("After Algorithm Dataset:")
for row in data:
    print("\t".join(map(str, row)))