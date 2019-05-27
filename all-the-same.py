def all_the_same(elements: List[Any]) -> bool:
    if elements:
        first = elements[0]
        for a in range(1, len(elements)):
            if elements[a] != first:
                return False
    return True
