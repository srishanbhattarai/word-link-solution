import sys
import enchant
import itertools

def main():
    d = enchant.Dict("en_US")

    if len(sys.argv) < 2:
        msg = '''
Usage:
    python main.py <letters>
Example:
    python main.py deia
        '''.strip()
        print(msg)
        sys.exit(1)
    
    # Input
    letters = sys.argv[1]
    letters_size = len(letters)

    for size in range(2, letters_size + 1):
        print("Length", size)

        permutations = [''.join(p) for p in list(itertools.permutations(letters, size))]
        matches = [word for word in permutations if d.check(word) == True]

        print("\t", dedupe(matches))

def dedupe(seq):
    seen = set()
    seen_add = seen.add

    return [x for x in seq if not (x in seen or seen_add(x))]

if __name__ == '__main__':
    main()
