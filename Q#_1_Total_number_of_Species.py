'''
Created on May 28, 2023

@author: HP
'''

import re
from collections import Counter
import matplotlib.pyplot as plt

file_path = r"C:\Users\HP\Advancedprogramming\Home_take_Exam_by_Tolina\mature.fa"
species_codes = []

with open(file_path, 'r') as file:
    for line in file:
        match = re.match(r'^>(\w+)', line)
        if match:
            species_codes.append(match.group(1))

species_counts = Counter(species_codes)
total_species = len(species_counts)
print("Total number of species:", total_species)

# Filter species with counts greater than 300
filtered_species_counts = {species: count for species, count in species_counts.items() if count >= 300}

# Sort filtered species based on microRNA counts in ascending order
sorted_species_counts = sorted(filtered_species_counts.items(), key=lambda x: x[1])

# Extract species and their counts from sorted list
species = [item[0] for item in sorted_species_counts]
counts = [item[1] for item in sorted_species_counts]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(species, counts)
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Number of miRNA per Species (Lowest to Highest)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
