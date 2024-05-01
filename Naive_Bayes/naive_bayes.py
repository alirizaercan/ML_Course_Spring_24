# Pseudo code for a Naive Bayes Classifier in Python-like syntax

# Function to read the dataset
def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        for line in file:
            dataset.append(line.strip().split(','))
    return dataset

# Function to split dataset by class
def split_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

# Function to calculate the probability of each attribute value given a class
def summarize_dataset(dataset):
    summaries = [(attribute, {value: (attribute.count(value) / len(attribute)) 
                for value in set(attribute)}) for attribute in zip(*dataset)]
    return summaries[:-1]  # Exclude label from summaries

# Function to calculate class probabilities
def class_probabilities(summaries, input_vector):
    probabilities = {}
    total_rows = sum([len(summaries[label][0][1]) for label in summaries])
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = len(class_summaries[0][1]) / float(total_rows)
        for i in range(len(class_summaries)):
            attribute, attribute_probs = class_summaries[i]
            if input_vector[i] in attribute_probs:
                probabilities[class_value] *= attribute_probs[input_vector[i]]
            else:
                probabilities[class_value] *= 0  # Attribute value not seen during training
    return probabilities

# Function to predict the class for an input vector
def predict(summaries, input_vector):
    probabilities = class_probabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

# Main function to control the Naive Bayes algorithm
def naive_bayes(train_file, test_file):
    # Load and prepare data
    training_data = read_dataset(train_file)
    test_data = read_dataset(test_file)
    # Prepare model
    separated = split_by_class(training_data)
    summaries = {label: summarize_dataset(rows) for label, rows in separated.items()}
    # Test model
    predictions = []
    for row in test_data:
        output = predict(summaries, row[:-1])
        predictions.append(output)
    return predictions

# Example of using the Naive Bayes function
train_file = 'train_data.txt'
test_file = 'test_data.txt'
predictions = naive_bayes(train_file, test_file)
print(predictions)
