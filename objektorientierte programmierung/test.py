###### test file
from location import Location, GALAPAGOS
from sample import Sample
from dna_sequencer import Sequencer, DnaSequencer, RnaSequencer
from experiment import Experiment

my_sample = Sample("0123", "Darwin", GALAPAGOS)
my_sequencer = DnaSequencer("C3P0", "Dna_Sequencer", True)
#my_sequencer.clean()
#my_sequencer.analyze_sample(my_sample)

my_rna_sequencer = RnaSequencer("R2D2", "Rna_Sequencer", True)

my_experiment = Experiment(my_sequencer, my_rna_sequencer)

my_experiment.run(my_sample)

#############################################################

#print("last sequencer: ", my_sample.last_sequencer)

#my_sample.template_strand()
#print("#####################################################")
#my_sample.coding_strand()
#print("#####################################################")
##print(my_rna_sequencer.dna_to_rna(my_sample.dna_sequence))
#print(my_rna_sequencer.extract_triplets("GUAGUACC"))

#my_rna_sequencer.extract_triplets("GUAGUACC")

#my_rna_sequencer.analyze_rna(my_sample)

#print(my_sample.dna_sequence)
#print(my_sample.rna_triplets)
#print("last sequencer: ", my_sample.last_sequencer)
#############################################################
