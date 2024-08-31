from app import naive, naive_with_rc, reverseComplement, get_genome

#How many times does AGGT or its reverse complement (ACCT) occur in the lambda virus genome? E.g. if AGGT occurs 10 times and ACCT occurs 12 times, you should report 22


p = 'AGGT'

dna = get_genome('lambda_virus.fa')

print(len(naive_with_rc(p, dna)))