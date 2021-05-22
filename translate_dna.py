def translate(seq,frame):
    BASES = 'ACGT'
    # standard code translation
    AA = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
    # transform DNA sequence in numbers: A=0; C=1; G=2; T=3
    seqn = [str(BASES.find(i)) for i in seq.upper()]
    # list of all codons in all forward frames
    allframes = [seqn[n:n+3] for n,j in enumerate(seqn) if n <= (len(seq)-3)]
    # translate the codons at the given frame taking the aa in AA string at position given by the number (in base 4) in allframes list
    return ''.join([AA[int(i,4)] for i in [''.join(i) for i in allframes[frame::3]]])


if __name__ == '__main__':
    query_seq = input('seq DNA: ')
    for k in range(3):
        print('frame {}: '.format(k+1), translate(query_seq,k))
