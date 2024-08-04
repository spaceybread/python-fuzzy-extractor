from fuzzy_extractor import FuzzyExtractor

INPUT_LENGTH = 16 # bytes of input accepted
EPSILON = 4 # bits of similarity
extractor = FuzzyExtractor(INPUT_LENGTH, EPSILON)

test_string = "SPACEY_WAS_HERE1"
print(len(test_string),":",test_string)

key, helper = extractor.generate(test_string)

attempts = ["SPACEY_WAS_HERE1", "SPACEY_WAS_HERE2", "AABBCCDDEEFFGGHH", "SPACEY_WAS_SLEEP"]

for at in attempts:
    r = extractor.reproduce(at, helper)
    if r == key:
        print("Similar:", at)
    else:
        print("Not Similar:", at)
        # if it is not similar, at least according to this implementation
        # the reproduced key is None
