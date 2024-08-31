from app import naive, get_genome, reverseComplement

dna = get_genome('lambda_virus.fa')

p = 'AGTCGA'
occurence = naive(p, dna)
reverse_occurence = naive(reverseComplement(p), dna)

print(occurence[0], reverse_occurence[0])
print(min(occurence[0], reverse_occurence[0]))
