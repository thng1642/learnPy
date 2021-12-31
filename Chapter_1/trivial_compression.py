
# Code converts a str composed of As, Cs, Gs and Ts into a string of bits and back again.
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    # underscore is used as a convention to indicate that implemention fo a method should not be relied on by actors outside of the class. (private for method or variable)
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<=2 #shift left two bits
            if nucleotide == 'A': #change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == 'C': #change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == 'G': #change last two bits to 1o
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else: 
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))