# Write any script to generate TeX code.

def line_break():
    print()


def base_structure():
    document_class = input('Document class (article, report, book, beamer, powerdot): ')
    font_size = input('Font size (8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 16pt): ')
    packages = input('Packages (space separated): ')
    author = input('Author: ')
    date = input('Date: ')

    '''
    Varies on document class.
    '''

    print(r'\documentclass[' + font_size + ']' + '{' + document_class + '}')
    line_break()
    print(r'% Packages')
    print(r'\usepackage' + '\n' + '{\n\t' + packages + '\n}')
    line_break()
    print(r'% Author affiliations')
    print(r'\author{' + author + '}')
    print(r'\date{' + date + '}')
    line_break()
    print(r'\begin{document}' + '\n' + r'\end{document}')


base_structure()
