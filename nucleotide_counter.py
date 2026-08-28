dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

a_count = dna.count("A")
g_count = dna.count("G")
c_count = dna.count("C")
t_count = dna.count("T")

print(f"{a_count} {c_count} {g_count} {t_count}")
assert f"{a_count} {c_count} {g_count} {t_count}" == "20 12 17 21"

