'''
Created on May 28, 2023

@author: HP
'''
def count_let7_miRNAs(file_path):
    let7_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(">"):
                # Extract the miRNA name from the header line
                miRNA_name = line.strip()[1:]

                # Check if the miRNA name contains "let-7"
                if "let-7" in miRNA_name:
                    let7_count += 1

    return let7_count

# Usage
file_path = r"C:\Users\HP\Advancedprogramming\Home_take_Exam_by_Tolina\mature.fa"
let7_count = count_let7_miRNAs(file_path)
print("Total number of let-7 miRNAs across all species:", let7_count)
