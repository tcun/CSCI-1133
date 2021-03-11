
def cg_ratio(dna):
    '''
    Purpose: Find the ratio between the number of 'cg' and the rest of the dna sequence pairs 
    Input Parameter(s):
        dna (string) - the dna sequence 
    Return Value:
        (float) the ratio between cg_counter and pair_iteration
    '''

    dna_sequence = dna.lower()
    dna_string_length = len(dna_sequence)
    cg_counter = 0
    for i in range(dna_string_length):
        pair_iterations = i
        if(dna_sequence[i:i+2] == "cg"): cg_counter += 1
        
    return cg_counter / pair_iterations

def mark(dna_str, target, codon_break):
    '''
    Purpose: Read the codons at indexes 0-2, and return a new string in which the same sequence return but with upper case instances of the target codon
    Input Parameter(s):
        dna_str (String) - Initial DNA sequence
        target (String) - Target codon that is being looking for in string
        codon_break (Int) - the index at which the reading frame is 
    Return Value:
        returns the new dna_str (string) in which instances of the target in dna_str are replaced to be upper case
    '''
    n = 3
    for i in range(codon_break, len(dna_str), n):
        if(dna_str[i:i+n] == target): 
            dna_str = dna_str[:i] + target.upper() + dna_str[i+ + n:]
    return dna_str   

def extract_url(url):
    '''
    Purpose: Find the URL within HTML source code
    Input Parameter(s):
        url (string) - html source code in string format
    Return Value:
        (string) returns the url within source code
    '''
    url_list = url.split('"')
    for i in url_list:
        if("://" in i):
            return i

