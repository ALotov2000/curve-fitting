from .gene import Gene
from typing import Iterable

class Chromosome():

    def __init__(self, gene_sequence: Iterable[Gene]):
        self._genes = tuple(gene_sequence)

    def __str__(self) -> str:
        return "[" \
            + str.join(str(self.get_gene[i]) + ("," if i != n - 1 else "") for i in range(n)) \
            + "]"

    def get_gene(self, i: int):
        return _genes[i]