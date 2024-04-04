from dna_sequencer import Sequencer
from sample import Sample

class Experiment:

    def __init__(self,DnaSequencer, RnaSequencer):
        self.DnaSequencer = DnaSequencer
        self.RnaSequencer = RnaSequencer
    
    def run(self, sample):
        continue_run = True

        while continue_run:
            start_again = False
            while not start_again:
                #input sample in dna Sequencer
                DnaSequencer.analyze_sample(sample)

                # check if sample contains dna sequence
                if not sample.dna_sequence:
                    print("an error has accured")
                    continue_run = False

                #input sample in rna sequencer
                RnaSequencer.analyze_rna(sample)

                # check if "UAC" triplet exists
                restart = True
                for element in sample.rna_triplets:
                    if sample.rna_triplets[element] == "UAC":
                        restart = False 

                if restart:
                    start_again = True

                #report sucess and print first 5 triplets
                print("the analysis was sucessful", sample.triplet_list[:5])


                
