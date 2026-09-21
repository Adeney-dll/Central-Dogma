filein = open(r'C:\Users\DELL\Downloads\rosalind_ini5.txt', 'r')
fileout = open(r'C:\Users\DELL\Downloads\out.txt', 'w')

line_number = 1
for line in filein:
    if line_number % 2 == 0:
        fileout.write(line)
    line_number = line_number + 1

filein.close()
fileout.close()
