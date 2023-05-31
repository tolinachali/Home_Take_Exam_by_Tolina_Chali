'''
Created on May 28, 2023

@author: HP
'''
import matplotlib.pyplot as plt
import numpy as np
import os


class Let7FamilyPresencePlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.let7_species = {}
        self.species_list = []
        self.let7_codes = []
        self.presence_matrix = None

    def extract_let7_code(self, header):
        if 'let-7' in header:
            code = header.split('let-7')[1].split()[0]
            return f"let-7{code[0]}"
        return ""

    def extract_species_code(self, header):
        start_index = header.find('>') + 1
        end_index = header.find('-', start_index)
        if start_index < end_index:
            return header[start_index:end_index]
        return ""

    def load_data(self):
        if not os.path.isfile(self.file_path):
            print("The specified file does not exist.")
            return
        current_species = ""
        with open(self.file_path, 'r') as file:
            for line in file:
                if line.startswith('>'):
                    header = line[1:].strip()
                    current_species = self.extract_species_code(header)
                else:
                    let7_code = self.extract_let7_code(header)
                    if let7_code:
                        self.let7_species.setdefault(current_species, {}).setdefault(let7_code, 0)
                        self.let7_species[current_species][let7_code] += 1

        self.species_list = [species for species, counts in self.let7_species.items() if sum(counts.values()) >= 6]
        self.let7_codes = list(set().union(*[d.keys() for d in self.let7_species.values()]))
        self.presence_matrix = np.zeros((len(self.species_list), len(self.let7_codes)))
        for i, species in enumerate(self.species_list):
            for j, let7_code in enumerate(self.let7_codes):
                self.presence_matrix[i, j] = self.let7_species[species].get(let7_code, 0)

    def plot_presence(self):
        x = np.arange(len(self.species_list))
        bar_width = 0.35
        fig, ax = plt.subplots(figsize=(10, 6))
        bottom = np.zeros(len(self.species_list))
        for i, let7_code in enumerate(self.let7_codes):
            ax.bar(x, self.presence_matrix[:, i], bottom=bottom, label=let7_code)
            bottom += self.presence_matrix[:, i]
            for j, species in enumerate(self.species_list):
                count = self.presence_matrix[j, i]
                if count > 0:
                    ax.text(x[j], bottom[j] - count / 2, str(int(count)), ha='center', va='center')

        ax.set_xlabel('Species')
        ax.set_ylabel('Presence Count')
        ax.set_title('Presence of let-7 Family per Species (Frequency >= 10)')
        ax.set_xticks(x)
        ax.set_xticklabels(self.species_list, rotation=45, ha='right')
        ax.legend()
        plt.tight_layout()
        plt.show()


# File path
file_path = r"C:\Users\HP\Advancedprogramming\Home_take_Exam_by_Tolina\mature.fa"

plotter = Let7FamilyPresencePlotter(file_path)
plotter.load_data()
plotter.plot_presence()
