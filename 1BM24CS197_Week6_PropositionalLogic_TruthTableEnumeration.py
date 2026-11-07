from itertools import product

def evaluate(sentence, model):
    if sentence == "P":
        return model["P"]
    elif sentence == "Q":
        return model["Q"]
    elif sentence == "R":
        return model["R"]


def model_check(KB, query):
    symbols = ["P", "Q", "R"]

    print("P Q R | KB | Query")
    print("--------------------")

    entailment = True

    for values in product([True, False], repeat=3):
        model = dict(zip(symbols, values))

        P = model["P"]
        Q = model["Q"]
        R = model["R"]

        kb = ((not Q or P) and
              (not P or not Q) and
              (Q or R))

        if query == "R":
            result = R
        elif query == "R->P":
            result = (not R or P)
        elif query == "Q->R":
            result = (not Q or R)

        print(P, Q, R, "|", kb, "|", result)

        if kb and not result:
            entailment = False

    return entailment


KB = ["Q->P", "P->~Q", "Q|R"]

print("\nChecking KB entails R:")
print("Result:", model_check(KB, "R"))
