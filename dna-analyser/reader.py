'''
Functions for reading and cleaning DNA sequences from input text files
'''

def read_file(file_path):
    """Reads text file

    Returns an empty string when there's an error when reading files.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content

    except FileNotFoundError:
        print(f'⚠️ Error: "{file_path}" not found!')
        return ''

    except Exception as e:
        print(f'⚠️ Unexpected error: {e}')
        return ''

def clean_input(input_text):
    """Removes whitespace characters and converts to upper case letters"""

    lines = input_text.splitlines()

    no_comment = ''.join(filter(lambda l: l[:2] not in ['# ', '% ', '//'], lines))
    
    return no_comment.strip().upper().replace(' ', '')

def read_seq_files(file_paths):
    ''' Read a batch of files '''

    sequences = {}

    for fname in file_paths:
        contents = read_file(fname)
        # clean input if file exists
        seq = clean_input(contents) 
        # add a valid seq
        sequences[fname] = seq

    return sequences

