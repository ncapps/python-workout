import csv


def passwd_to_csv(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        infile = csv.reader(input_file, delimiter=':')
        outfile = csv.writer(output_file, delimiter='\t')

        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


passwd_to_csv('ch05_files/fakefile.txt', 'ch05_files/fakeoutput.txt')
