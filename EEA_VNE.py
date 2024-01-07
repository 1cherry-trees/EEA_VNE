"""
Entropy Estimation Algorithm and von Neumann extractor
python implementation

"""
import math
import random

def eea(sample):
    """Entropy Estimation Algorithm (EEA) implementation"""
    n = len(sample)
    counts = {}
    for x in sample:
        counts[x] = counts.get(x, 0) + 1
    entropy = 0
    for count in counts.values():
        p = count / n
        entropy -= p * math.log2(p)
    return entropy

def von_neumann_extractor(sample):
    """von Neumann extractor implementation"""
    extracted_bits = ""
    for i in range(0, len(sample), 2):
        if sample[i] == sample[i+1]:
            continue
        extracted_bits += "0" if sample[i] == "1" else "1"
    return extracted_bits

# Example usage
random_bits = ''.join(str(random.randint(0, 1)) for _ in range(100))
print("Random bits:", random_bits)
entropy_estimate = eea(random_bits)
print("Entropy estimate:", entropy_estimate)
extracted_bits = von_neumann_extractor(random_bits)
print("Extracted bits:", extracted_bits)
