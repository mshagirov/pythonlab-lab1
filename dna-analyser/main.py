#!/usr/bin/env python3

import sys
import os
from pathlib import Path

from banner import display_banner
from reader import *
from dnatools import *

TEXT_WIDTH = os.get_terminal_size().columns

def main(*input_files):
    display_banner()

    print("\nAnalysing sequences:")

    border = f'+{"-"*20}+{"-"*6}+{"-"*8}+{"-"*8}+{"-"*8}+{"-"*8}+{"-"*8}+'

    print(border)
    print(f'┊{"Sequence File":^20}┊{"DNA?":^6}┊{"#bases":^8}┊{"ssMW kDa":^8}┊{"GC%":^8}┊{"AT/GC":^8}┊{"Tm C°":^8}┊')
    print(border)

    sequences = read_seq_files(input_files)

    for seq in sequences:
        print(f'┊{Path(seq).name:^20}', end='')
        if not is_dna(sequences[seq]):
            print('┊  ❌  ┊')
            print(border)
            continue
        else:
            print('┊  🧬  ', end='')
        print(f'┊{len(sequences[seq]):^8}', end='')

        bases = count_bases(sequences[seq])
        print(f'┊{ss_wight(bases)/1000:^8.2f}', end='')

        GC_to_total = f'{gc_percent(bases):.2f}' + '%'
        print(f"┊{GC_to_total:^8}", end='')

        AT_GC_ratio = f'{at_to_gc_ratio(bases):.2f}'
        print(f"┊{AT_GC_ratio:^8}", end='')

        print(f'┊{wallace_rule_melting_temperature(bases):^8}',end='')
        print("┊")
        print(border)

    #print(border)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('DNA Analyser requires at least 1 input file\n')
        print(f'\t{sys.argv[0]} input_file1 [ input_file2 [ input_file3 ... ] ... ]\n')
        
        sys.exit(1)

    main(*sys.argv[1:])
