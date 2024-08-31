from app import naive, reverseComplement, get_genome

#Question 2 How many times does TTAA or its reverse complement occur in the lambda virus genome?  

dna = get_genome('lambda_virus.fa')

p = 'ACTAAGT'
occurence = naive(p, dna)
reverse_occurence = naive(reverseComplement(p), dna)

print(occurence[0], reverse_occurence[0])
print(min(occurence[0], reverse_occurence[0]))
