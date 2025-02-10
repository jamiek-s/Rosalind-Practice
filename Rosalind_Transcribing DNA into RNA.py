base_string = "CAATCATGGCCCCAACATAACTAGTAGAACCTGCCTGAGCAACACTAGAGTGGCACGGGGACCTGAAGTTCCGCGGTGATTCTTTATCTTTTGTAAAGTGCGGCAAAACTGATCCTCCTGCAGATGGAATTTTCTTCTGGTTGTAATGCATATTCCCAAGCCGGTGGATCTAAGCTGCTGTCGAGTAAGAAGAAGCTTCTAGCGTGGTTCCTGGCTGACTGATAAATCTTTCAGACTAAAGTCTGTGCCCTCTCCAAACGCGCCTAAATCAGAACTGCCTTAAGTTTGCACGAGTAGGTCACACAGAAGAACCACATTCGCCAAGGCACAGGTGGAAATCGATCTGCTTTACGCCGACACAGTTGGGGTAGAAGCAAAAGGACGGACTAGGGTGCCTGTGGAGCAGCAGCGGGCACACGAATGCTTCTCGCATGTGGCGGCGGAGAGGGATTGTGCTTATCAGGAATGCGGCGTAGGCACACCGTTAGGGCGATCAAAAGCGTACGGACCCGTCTGCATAATCTGCTACAATCCACGCCTGTGGTGGGTGAATTGAGAATCGTCGCGCGGTGTGGGGGCGTACCCTCTTAAACGTATCTCACTCCCCGCTGTGTTCGAGGGCTGGTCCCGTTCTTCCGCCTATGAGTGGAAGAGTTCCCTATGTAGAGGAGCGATGGTGGCATCATACCAACAGGCTACGTCTCCATGAAATCTACGTTGTGAGAGCGTAAGGTGCCGCTCCCCCCTCTTTCCCGAACATTTGAATATCGACTCTTCAAATAGCATCAAGAACGTCTAGGACAATTCCATCCAGAGACCCGCGTATTCGCAGTTGGGGACGCTGTGGAATTTGCGAATTAAGTATCGTGGCTGAACTGTATTCTCCGTATATATTCCAACATCCATGTGACTAGCCGAAACTAACTGGTATCGCTGGGTAGCGGTTG"

def swap_u_and_t (x):
    if (x == "T"):
        return "U"
    else:
        return x


def change_strings (x):
    x_is_list = list(x)
    convert_values = list(map(swap_u_and_t, x_is_list))
    return ''.join(convert_values)
print(change_strings(base_string))

