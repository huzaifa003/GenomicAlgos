import collections
import requests
def get_genome(filename):
    #curl -o lambda_virus.fa  https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa 
    file = open(filename, "r")
    with file as f:
        genome = ''
        for line in f:
            if not line[0] == '>':
                print(line)
                genome += line.rstrip()
        return genome
    
    
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities



def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


def naive_with_rc(p, t):
    return list(set(naive(p, t) + naive(reverseComplement(p), t)))
 
 
 ##Reading Fasta File   
# if __name__ == "__main__":
#     filename = "lambda_virus.fa"
#     file_content = get_genome(filename)
    
#     frequency = {}
#     for char in file_content:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1

#     print(frequency)
    
    
    
#     print(collections.Counter(file_content))
    
def download_file(filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Download completed: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

download_file('phix.fa', 'http://d396qusza40orc.cloudfront.net/ads1/data/phix.fa')

# p = 'CCC'
# ten_as = 'AAAAAAAAAA'
# t = ten_as + 'CCC' + ten_as + 'GGG' + ten_as

# occurrences = naive_with_rc(p, t)
# print(occurrences)


# p = 'CGCG'
# t = ten_as + 'CGCG' + ten_as + 'CGCG' + ten_as
# occurrences = naive_with_rc(p, t)
# print(occurrences)



