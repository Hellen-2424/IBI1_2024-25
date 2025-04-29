import matplotlib.pyplot as plt
from collections import Counter

# 1. Find the most frequent trinucleotide
def most_frequent_trinucleotide(mrna_sequence):
    """
    Input: mRNA sequence (string)
    Output: The most frequent trinucleotide and its count
    Assumption: The sequence starts with the start codon 'AUG' and contains a stop codon
    """
    # List of stop codons
    stop_codons = ['UAA', 'UAG', 'UGA']
    
    # Ensure the sequence starts with 'AUG'
    if not mrna_sequence.startswith('AUG'):
        return "Sequence must start with 'AUG'", 0
    
    # Find the position of the first stop codon
    end_pos = len(mrna_sequence)
    for i in range(0, len(mrna_sequence) - 2, 3):
        codon = mrna_sequence[i:i+3]
        if codon in stop_codons:
            end_pos = i
            break
    
    # Extract the coding region (from AUG to before the stop codon)
    coding_sequence = mrna_sequence[0:end_pos]
    
    # Count the frequency of all trinucleotides
    trinucleotides = [coding_sequence[i:i+3] for i in range(0, len(coding_sequence), 3)]
    if not trinucleotides:
        return "No valid trinucleotides", 0
    
    # Use Counter to find the most frequent trinucleotide
    trinucleotide_counts = Counter(trinucleotides)
    most_common = trinucleotide_counts.most_common(1)[0]  # Get the most frequent trinucleotide
    
    return most_common[0], most_common[1]

# 2. Find the most frequent amino acid
def most_frequent_amino_acid(mrna_sequence):
    """
    Input: mRNA sequence (string)
    Output: The most frequent amino acid and its count
    """
    # Codon table (partial, includes only the necessary codons and those mentioned in the problem)
    codon_table = {
        'AUG': 'Met',  # Start codon
        'CCG': 'Pro',  # Proline
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys',
        'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu',
        'UGU': 'Cys', 'UGC': 'Cys',
        'UGG': 'Trp',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    }
    
    stop_codons = ['UAA', 'UAG', 'UGA']
    
    if not mrna_sequence.startswith('AUG'):
        return "Sequence must start with 'AUG'", 0
    
    # Find the coding region
    end_pos = len(mrna_sequence)
    for i in range(0, len(mrna_sequence) - 2, 3):
        codon = mrna_sequence[i:i+3]
        if codon in stop_codons:
            end_pos = i
            break
    
    coding_sequence = mrna_sequence[0:end_pos]
    
    # Translate to amino acids
    amino_acids = []
    for i in range(0, len(coding_sequence), 3):
        codon = coding_sequence[i:i+3]
        if codon in codon_table:
            amino_acids.append(codon_table[codon])
    
    if not amino_acids:
        return "No valid amino acids", 0
    
    # Count the frequency of amino acids
    amino_acid_counts = Counter(amino_acids)
    most_common = amino_acid_counts.most_common(1)[0]
    
    return most_common[0], most_common[1]

# 3. Plot the frequency distribution of amino acids
def plot_amino_acid_frequencies(mrna_sequence):
    """
    Input: mRNA sequence (string)
    Output: Plots a bar chart of the frequency distribution of amino acids
    """
    # Use the same codon table as above
    codon_table = {
        'AUG': 'Met', 'CCG': 'Pro', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro',
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys',
        'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu',
        'UGU': 'Cys', 'UGC': 'Cys',
        'UGG': 'Trp',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    }
    
    stop_codons = ['UAA', 'UAG', 'UGA']
    
    if not mrna_sequence.startswith('AUG'):
        print("Sequence must start with 'AUG'")
        return
    
    # Find the coding region
    end_pos = len(mrna_sequence)
    for i in range(0, len(mrna_sequence) - 2, 3):
        codon = mrna_sequence[i:i+3]
        if codon in stop_codons:
            end_pos = i
            break
    
    coding_sequence = mrna_sequence[0:end_pos]
    
    # Translate to amino acids
    amino_acids = []
    for i in range(0, len(coding_sequence), 3):
        codon = coding_sequence[i:i+3]
        if codon in codon_table:
            amino_acids.append(codon_table[codon])
    
    if not amino_acids:
        print("No valid amino acids")
        return
    
    # Count frequencies
    amino_acid_counts = Counter(amino_acids)
    
    # Plot the bar chart
    amino_acids_list = list(amino_acid_counts.keys())
    frequencies = list(amino_acid_counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(amino_acids_list, frequencies, color='skyblue')
    plt.xlabel('Amino Acid')
    plt.ylabel('Frequency')
    plt.title('Amino Acid Frequency Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Test the code
# Test mRNA sequence
test_sequence="AUGGUGCUCCUCGUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUGCUUCCUCGGACUUGGACUGCCUCCGACUGGUG"

# 1. Most frequent trinucleotide
trinucleotide, count = most_frequent_trinucleotide(test_sequence)
print(f"Most frequent trinucleotide: {trinucleotide}, Count: {count}")

# 2. Most frequent amino acid
amino_acid, aa_count = most_frequent_amino_acid(test_sequence)
print(f"Most frequent amino acid: {amino_acid}, Count: {aa_count}")

# 3. Plot amino acid frequencies
plot_amino_acid_frequencies(test_sequence)
