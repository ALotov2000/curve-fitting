class Gene:
    interval = (0, 0)

    def set_interval(new_interval: (int, int)) -> None:
        Gene.interval = new_interval
    
    def __init__(self, v:float = 0) -> None:
        self.value = v

    def __str__(self) -> str:
        return str(self.value)