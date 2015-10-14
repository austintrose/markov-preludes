import random

# Parse the given files and return a list of the note numbers from each
# Note_on_c line in the file.
def get_notes(filename):
    return [int(l.split(", ")[4])
            for l in open(filename, mode='r').readlines()
            if "Note_on_c" in l]

def replace_note(line, old, new):
    p = line.split(", ")
    return ", ".join([p[0], p[1], p[2], p[3], str(new), p[5]])

def convert(filename, outfile, old_notes, new_notes):
    lines = open(filename, mode='r').readlines()
    out = open(outfile, mode='w')

    needs_off = {}
    added = 0
    for l in lines:
        if "Note_on_c" in l:
            out.write(replace_note(l, old_notes[added], new_notes[added]))
            needs_off[old_notes[added]] = new_notes[added]
            added += 1
        elif "Note_off_c" in l:
            old = int(l.split(", ")[4])
            out.write(replace_note(l, old, needs_off.pop(old)))
        else:
            out.write(l)


def create_markov_dict(notes, depth):
    subs = [notes[i:i+depth+1] for i in range(len(notes)-(depth+1))]
    states = {}
    for s in subs:
        base = tuple(s[:depth])
        end = s[depth]

        if base in states:
            states[base].append(end)

        else:
            states[base] = [end]

    return states

def gen_notes(notes, depth):
    markov_dict = create_markov_dict(notes, depth)
    while True:
        try:
            start = notes[:depth]

            for i in range(depth, len(notes)):
                current = tuple(start[-depth:])
                possible_next = markov_dict[current]
                choice = random.choice(possible_next)
                start.append(choice)

            return start
        except:
            pass
