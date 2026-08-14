import csv
import random

# ------------------------------
# READ examples
# ------------------------------

read_sentences = [
    "Machine learning improves healthcare.",
    "Artificial intelligence is transforming education.",
    "Python is a popular programming language.",
    "Data science combines statistics and computing.",
    "Neural networks are inspired by the human brain.",
    "This chapter introduces machine learning concepts.",
    "The experiment achieved excellent accuracy.",
    "Cloud computing provides scalable resources.",
    "Cybersecurity protects digital systems.",
    "Deep learning performs well on image recognition.",
    "Natural language processing helps computers understand text.",
    "The proposed system converts PDF documents into speech.",
    "Accessibility technology assists visually impaired users.",
    "Speech synthesis converts text into spoken words.",
    "The model was trained using supervised learning."
]

# ------------------------------
# Ignore examples
# ------------------------------

ignore_examples = []

# Page numbers
for i in range(1, 301):
    ignore_examples.append(f"Page {i}")

# Figures
for i in range(1, 201):
    ignore_examples.append(f"Figure {i}")

# Tables
for i in range(1, 201):
    ignore_examples.append(f"Table {i}")

# URLs
domains = [
    "google.com",
    "school.edu",
    "example.com",
    "github.com",
    "wikipedia.org"
]

for d in domains:
    ignore_examples.append(f"www.{d}")
    ignore_examples.append(f"https://{d}")

# Miscellaneous
ignore_examples.extend([
    "Copyright 2025",
    "Confidential",
    "All Rights Reserved",
    "Table of Contents",
    "Index",
    "Appendix",
    "References"
])

# ------------------------------
# Create dataset
# ------------------------------

dataset = []

# Repeat READ examples many times
for _ in range(40):
    for sentence in read_sentences:
        dataset.append([sentence, "Read"])

# Add Ignore examples
for item in ignore_examples:
    dataset.append([item, "Ignore"])

# Shuffle
random.shuffle(dataset)

# Save CSV
with open("ml/dataset.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["text", "label"])

    writer.writerows(dataset)

print("Dataset created successfully!")
print(f"Total samples: {len(dataset)}")