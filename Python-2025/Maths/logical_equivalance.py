# exclusive or
def exclusive_or(a,b):
    return False if a == b else True

# implication
def implication(a,b):
    return not a or b

# bi-conditional
def bi_conditional(a,b):
    return True if a == b else False