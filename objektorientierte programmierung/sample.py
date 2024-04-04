
# Here is the most minimal class
class Sample:

    def __init__(self, identifier, collector, found_at): # constuctor
        self.identifier = identifier
        self.collector = collector
        self.analysis_done = False
        self.dna_sequence = None
        self.found_at = found_at
        last_sequencer = ""
        rna_triplets = []

    def __str__(self):
        text = "Sample: " + self.identifier + ", collected by " + self.collector
        if self.analysis_done:
            text = text + " (analyzed)"
        return text

    def take_analysis_result(self, dna_sequence):
        self.dna_sequence = dna_sequence
        self.analysis_done = True

    def template_strand(self):
        if self.dna_sequence:
            print(self.dna_sequence)
        else:
            print("your dna Sequence is faulty :(")

    def coding_strand(self):
        if self.dna_sequence:
            dna_sequence_coding = ""
            for element in range(len(self.dna_sequence)):
                if self.dna_sequence[element] == "A" :
                    dna_sequence_coding = dna_sequence_coding + "T"
                elif self.dna_sequence[element] == "T" :
                    dna_sequence_coding = dna_sequence_coding + "A"
                elif self.dna_sequence[element] == "C" :
                    dna_sequence_coding = dna_sequence_coding + "G"
                elif self.dna_sequence[element] == "G" :
                    dna_sequence_coding = dna_sequence_coding + "C"
            print(dna_sequence_coding)
        else:
             print("your dna Sequence is faulty :(")

            
        
