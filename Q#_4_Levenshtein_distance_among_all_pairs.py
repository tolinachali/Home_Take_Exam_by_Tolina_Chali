import Levenshtein
import matplotlib.pyplot as plt


def calculate_levenshtein_distances(mirnas):
    distances = []
    for mirna, seq in mirnas:
        print("Pairwise Levenshtein distances for", mirna)
        for other_mirna, other_seq in mirnas:
            if mirna != other_mirna:
                distance = Levenshtein.distance(seq, other_seq)
                distances.append(distance)
                print(f"Levenshtein distance between {mirna} and {other_mirna}: {distance}")
    return distances


def plot_histogram(distances):
    plt.hist(distances, bins=10)  # Adjust the number of bins as needed
    plt.xlabel("Levenshtein Distance")
    plt.ylabel("Frequency")
    plt.title("Distribution of Levenshtein Distances")
    plt.show()


let7a_mirnas = []


with open(r"C:\Users\HP\Advancedprogramming\Home_take_Exam_by_Tolina\mature.fa", "r") as file:
    miRNA_name = ""
    sequence = ""
    for line in file:
        if line.startswith(">"):
            if miRNA_name != "":
                if miRNA_name.startswith("hsa-let-7"):
                    let7a_mirnas.append((miRNA_name, sequence))
            miRNA_name = line.strip()[1:]
            sequence = ""
        else:
            sequence += line.strip()

    if miRNA_name.startswith("-let-7"):
        let7a_mirnas.append((miRNA_name, sequence))


print("let-7 miRNA codes:")
for mirna, _ in let7a_mirnas:
    print(mirna)

distances = calculate_levenshtein_distances(let7a_mirnas)
plot_histogram(distances)
