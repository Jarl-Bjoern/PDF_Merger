# Rainer C. B. Herold
# Vers 0.1 03.10.2022

# Libraries
try:
    from PyPDF2 import PdfMerger
    from os.path import expanduser, join
    from os import walk
    from sys import argv
except ModuleNotFoundError as e: input(f"The module was not found {e}. Please resume with return"), exit()

# Variables
Path = argv[1]

# Main
if __name__ == '__main__':
    merger = PdfMerger()
    for root, _, files in walk(Path, topdown=False):
        for file in files:
            if (file.endswith('.pdf')):
                merger.append(join(root, file))
    merger.write(expanduser(r'~/Desktop/result.pdf'))
    merger.close()
