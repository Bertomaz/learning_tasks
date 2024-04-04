from random import choices
from sample import Sample
from location import GALAPAGOS

class Sequencer:
    
    def __init__(self, serial_number, model, is_clean):
        self.serial_number = serial_number
        self.model = model
        self.is_clean = is_clean

    def analyze_sample(self, sample):
        if not self.is_clean:
            print("Sequencer", self.serial_number, "is still dirty - abort")
            return

        dna_sequence = "".join(
            choices(
                self.BASES,  # Note how it is accessed
                k=self.SEQUENCE_LENGTH
            )
        )
        sample.take_analysis_result(dna_sequence)

        # Analysis done, device got dirty
        self.is_clean = False
        sample.last_sequencer = self.serial_number

class RnaSequencer(Sequencer):

    BASES = ["A", "C", "G", "T"]
    SEQUENCE_LENGTH = 2000

    def analyze_rna(self, sample):
        if not sample.dna_sequence:
            self.analyze_sample(sample)
        template_dna_sequence = sample.dna_sequence
        template_rna_sequence = ""

        for elementz in range(len(template_dna_sequence)):
            if template_dna_sequence[elementz] == "A" :
                template_rna_sequence = template_rna_sequence + "U"
            elif template_dna_sequence[elementz] == "T" :
                template_rna_sequence = template_rna_sequence + "A"
            elif template_dna_sequence[elementz] == "C" :
                template_rna_sequence = template_rna_sequence + "G"
            elif template_dna_sequence[elementz] == "G" :
                template_rna_sequence = template_rna_sequence + "C"
        
        triplet_list = [template_rna_sequence[i:i+3] for i in range(0, len(template_rna_sequence),3)]
        if len(triplet_list[len(triplet_list)-1]) < 3:
            triplet_list.pop()
        print(triplet_list)

        sample.rna_triplets = triplet_list


######################## little helpers ##############################################
#    def dna_to_rna(self, template_dna_sequence):
#        template_rna_sequence = ""
#
#        for elementz in range(len(template_dna_sequence)):
#            if template_dna_sequence[elementz] == "A" :
#                template_rna_sequence = template_rna_sequence + "U"
#            elif template_dna_sequence[elementz] == "T" :
#                template_rna_sequence = template_rna_sequence + "A"
#            elif template_dna_sequence[elementz] == "C" :
#                template_rna_sequence = template_rna_sequence + "G"
#            elif template_dna_sequence[elementz] == "G" :
#                template_rna_sequence = template_rna_sequence + "C"
#        return template_rna_sequence

#    def extract_triplets(self, template_rna_sequence):
#        triplet_list = [template_rna_sequence[i:i+3] for i in range(0, len(template_rna_sequence),3)]
#        if len(triplet_list[len(triplet_list)-1]) < 3:
#            triplet_list.pop()
#        print(triplet_list)
#        return triplet_list
#####################################################################################        

class DnaSequencer(Sequencer):
    

    BASES = ["A", "C", "G", "T"]
    SEQUENCE_LENGTH = 2000
    # If it is written at the indentation level
    # directly below the class header, it is a class attribute
    # This time in upper case because we want this to be treated
    # as a constant, which are written this way by convention

    #Class Method
    @classmethod #decorater
    def verify_dna_sequence(cls, dna_sequence):
        if len(dna_sequence) != cls.SEQUENCE_LENGTH:
            return False
        for base in dna_sequence:
            if base not in cls.BASES:
                return False
        return True

    def __init__(self, serial_number, model, is_clean=False):
        super().__init__(serial_number,model, is_clean)
        

    def clean(self):
        self.is_clean = True
        print("DNA sequencer", self.serial_number, "has been cleaned")

    def analyze_sample(self, sample):
        super().analyze_sample(sample)

######### Sub classes #################

class DnaMaster2000(DnaSequencer):
    MODEL = "DNA MASTER 2000"

    def __init__(self, serial_number):
        super().__init__(serial_number, is_clean=True)

# with the super() you can use methods from the superclass

    def analyze_sample(self, sample):
        print(self.MODEL, "serial number" , self.serial_number)
        super().analyze_sample(sample)
        print("analyzed", len(sample.dna_sequence), "bases")
        
class DnaMaster3000(DnaSequencer):
    MODEL = "DNA MASTER 3000"
    SEQUENCE_LENGTH = 3000

    def analyze_sample(self,sample):
        print(self.MODEL, "serial number" , self.serial_number)
        print("Sample: " , sample)
        super().analyze_sample(sample)
        if sample.dna_sequence:
            print("Preview:" , sample.dna_sequence[:20])
        else:
            print("No preview available")
        
    
    def run_demonstation(self, sample):
        print(self.MODEL, "serial number" , self.serial_number)
        print("Sample: " , sample)
        print("Preview:", "ACGT" * 5)













    
    
