from markov import *

for PRELUDE in ["2", "3"]:
    for PART in ["1", "2"]:
        FILENAME = "Prelude%s-%s.mid.csv" % (PRELUDE, PART)
        original_notes = get_notes(FILENAME)
        for DEPTH in [2, 3, 4]:
            OUTPUT = ("MarkovD%d" % (DEPTH,)) + FILENAME[:FILENAME.index( ".")] + ".csv"
            new_notes = gen_notes(original_notes, DEPTH)
            convert(FILENAME, OUTPUT, original_notes, new_notes)
            print "wrote " + OUTPUT
