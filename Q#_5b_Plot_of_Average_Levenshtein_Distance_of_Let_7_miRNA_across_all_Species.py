import os
import Levenshtein
import matplotlib.pyplot as plt

class LevenshteinDistanceAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.let7_sequences = {}
        self.let7_frequency = {}
        self.avg_distances = []
        self.frequencies = []
        self.miRNA_families = []
        self.total_sequences_count = 0

    def analyze(self):
        if not os.path.isfile(self.file_path):
            print("The specified file does not exist.")
            return

        self.process_sequences()

        for let7_code, sequences in self.let7_sequences.items():
            total_distance, total_pairs = self.calculate_total_distance(sequences)
            if total_pairs > 0:
                average_distance = total_distance / total_pairs
                frequency = self.let7_frequency.get(let7_code, 0)
                self.avg_distances.append(average_distance)
                self.frequencies.append(frequency)
                self.miRNA_families.append(let7_code)
                print(f"The Average Levenshtein distance among all pairs for miRNA family {let7_code}: {average_distance:.2f}")
                print(f"The frequency of miRNA family {let7_code}: {frequency}")
                self.total_sequences_count += frequency

        self.plot_results()

    def process_sequences(self):
        with open(self.file_path, 'r') as file:
            let7_code = ""
            sequence = ""
            for line in file:
                if line.startswith('>'):
                    header = line[1:].strip()
                    let7_code = self.extract_let7_code(header)
                    sequence = ""
                else:
                    sequence = line.strip()

                if let7_code and sequence:
                    self.let7_sequences.setdefault(let7_code, []).append(sequence)
                    self.let7_frequency[let7_code] = self.let7_frequency.get(let7_code, 0) + 1

    def extract_let7_code(self, header):
        if 'let-7' in header:
            code = header.split('let-7')[1].strip()[0]
            return f"let-7{code}"
        return ""

    def calculate_total_distance(self, sequences):
        total_distance = 0
        total_pairs = 0
        if len(sequences) < 2:
            return total_distance, total_pairs
        for i in range(len(sequences) - 1):
            for j in range(i + 1, len(sequences)):
                total_distance += Levenshtein.distance(sequences[i], sequences[j])
                total_pairs += 1
        return total_distance, total_pairs

    def plot_results(self):
        x_pos = range(len(self.miRNA_families))
        fig, ax1 = plt.subplots()
        ax1.bar(x_pos, self.avg_distances, align='center', alpha=0.5)
        ax1.set_ylabel('Average Levenshtein Distance')
        ax1.set_title('Average Levenshtein Distance and Frequency for miRNA Families')
        ax2 = ax1.twinx()
        ax2.plot(x_pos, self.frequencies, 'r')
        ax2.set_ylabel('Frequency')
        plt.xticks(x_pos, self.miRNA_families)
        plt.xlabel('miRNA Family')
        plt.show()

# File path
file_path = r"C:\Users\HP\Advancedprogramming\Home_take_Exam_by_Tolina\mature.fa"

analyzer = LevenshteinDistanceAnalyzer(file_path)
analyzer.analyze()
