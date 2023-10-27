from .gene import Gene
from typing import Iterable

class Chromosome():

    def __init__(self, gene_sequence: Iterable[Gene]):
        self._genes = tuple(gene_sequence)

    def __str__(self) -> str:
        return "(" \
            + "".join([(", " if i != 0 else "") + str(gene) for i, gene in enumerate(self._genes)]) \
            + ")"

    def get_gene(self, i: int):
        return self._genes[i]