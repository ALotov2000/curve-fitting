from .gene import Gene
from typing import List

class Chromosome():

    def __init__(self, n):
        self.genes = []
        self.length = n

    def autofill(self):
        # todo: autofill randomly
        pass

    def __str__(self) -> str:
        return "[" \
            + str.join(str(i) + ("," if i != n - 1 else "") for i in range(n)) \
            + "]"
