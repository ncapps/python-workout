def reverse_lines(infilename, outfilename):
    with open(infilename, 'r') as infile, open(outfilename, 'w') as outfile:
        for line in infile:
            outfile.write(f'{line.rstrip()[::-1]}\n')


reverse_lines('ch05_files/reversefile.txt', 'ch05_files/reversedfile.txt')
