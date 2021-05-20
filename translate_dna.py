def translate(seq,frame):
    BASES = 'ACGT'
    # standard code translation
    AA = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
    # transform DNA sequence in numbers A=0; C=1; G=2; T=3
    seqn = [str(BASES.find(i)) for i in seq.upper()]
    # list of all codons in all forward frames
    allframes = [seqn[n:n+3] for n,j in enumerate(seqn) if n <= (len(seq)-3)]
    # list of codons in the given frame
    translated = [allframes[k] for k in range(frame,len(allframes),3)]
    # translate the codons taking the aa in AA at position given by the number(in base 4)
    return ''.join([AA[int(i,4)] for i in [''.join(i) for i in translated]])


if __name__ == '__main__':
    print(translate('ggggcagctgggaggg',1))

