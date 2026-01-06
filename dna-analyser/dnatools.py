def is_dna(seq):
    """Check if sequence contains only A, T, G, C"""
    return set('ATGC') == set(seq)

def count_bases_withloop(seq):
    count = {'A':0, 'T':0, 'G':0, 'C':0}
    for base in seq:
        count[base] += 1
    return count

def count_bases(seq):
    return {base: seq.count(base) for base in 'ATGC'}

def gc_percent(seq_info):
    '''seq_info can be base count or a DNA sequence str'''
    if isinstance(seq_info, dict):
        gc_count = seq_info['G'] + seq_info['C']
        total = seq_info['A'] + seq_info['T'] + seq_info['G'] + seq_info['C']
    elif isinstance(seq_info, str):
        gc_count = seq_info.count('G') + seq_info.count('C')
        total = len(seq_info)
    else:
        raise TypeError(f"Expected str or dict, but got {type(seq_info).__name__}")
    return 100 * gc_count / total

def at_to_gc_ratio(seq_info):
    '''matching types requires Python 3.10 or newer'''

    match seq_info:
        case dict():
            pass
        case str():
            seq_info = count_bases(seq_info)
        case _:
            raise TypeError(f"Expected str or dict, but got {type(seq_info).__name__}")
    return (seq_info['A'] + seq_info['T']) / (seq_info['G'] + seq_info['C'])


# https://www.thermofisher.com/sg/en/home/references/ambion-tech-support/rna-tools-and-calculators/dna-and-rna-molecular-weights-and-conversions.html
def ss_wight(base_count):
    weight = 313.2*base_count['A'] + \
        304.2*base_count['T'] + \
        329.2*base_count['G'] + \
        289.2*base_count['C']
    return weight

def wallace_rule_melting_temperature(base_count):
    Tm = 4*(base_count['G'] + base_count['C']) + 2*(base_count['A']+ base_count['T'])
    return Tm

# complementary strand
def complementary_strand(seq):
    convert = {'A': 'T', 'T':'A', 'G': 'C', 'C':'G'}
    return ''.join([convert[k] for k in seq])

# mRNA seq
def transcribe_to_rna(seq):
    convert = {'A': 'U', 'T':'A', 'G': 'C', 'C':'G'}
    return ''.join([convert[k] for k in seq])
