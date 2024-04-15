
all_notes = []
for i in range(1,8):
    octave = str(i)
    next_octave = str(i+1)
    notes = ["C"+octave+" ","C" + octave +"#","D" +octave+" ","D"+octave+"#","E"+octave+" ","F"+octave+" ","F"+octave+"#","G"+octave+" ","G"+octave+"#","A"+octave+" ","A"+octave+"#","B"+octave+" ","C"+next_octave+" "]
    all_notes = all_notes + notes

print(all_notes)

def half_tone_offset():
    try_base_note = True
    while try_base_note:
        base_note = input("please enter a Base note: ")
        if base_note in all_notes:
            index_base_note = all_notes.index(base_note)
            try_base_note = False
