from typing import Iterable, Callable

def custom_sorted(iterable: Iterable[any], order_function: Callable[[any, any], bool]):
    class Item:
        def __init__(self, value):
            self.value = value
        def __lt__(self, other):
            return order_function(self.value, other.value)
    
    items = [Item(x) for x in iterable]
    sorted_items = sorted(items)
    return [item.value for item in sorted_items]
