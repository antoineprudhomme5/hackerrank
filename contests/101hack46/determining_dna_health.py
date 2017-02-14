# number of genes
n = int(input())
# the genes
genes = input().split()
# genes values
values = list(map(int, input().split()))
# number of strands of DNA to process
s = int(input())

unhealthiest = 100000000
healthiest = 0

def search_values(dna, dna_i, first, last):
    counter = 0

    # go throught the genes. If there is a match, add the related value
    for i in range(first, last+1):
        # if len(1) => just look if equals
        if len(genes[i]) == 1:
            if genes[i] == dna[dna_i]:
                counter += values[i]
        # else find if the full pattern follow
        else:
            # compare the len(genes[i]) following characters to the pattern
            if len(dna[dna_i:]) >= len(genes[i]):
                if dna[dna_i:dna_i + len(genes[i])] == genes[i]:
                    counter += values[i]

    return counter

# for each DNA strand to process
for _ in range(s):
    # first - last => indexes in genes and values
    first, last, d = input().split()
    first, last = int(first), int(last)

    total = 0

    # go throught the DNA
    for i in range(len(d)):
        total += search_values(d, i, first, last)


    if total < unhealthiest:
        unhealthiest = total
    if total > healthiest:
        healthiest = total

print('%d %d' % (unhealthiest, healthiest))
