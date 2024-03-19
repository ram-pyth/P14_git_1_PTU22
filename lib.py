def sumuok(sk1: int | float, sk2: int | float) -> int | float:
    res = sk1 + sk2  # skaičiuojam naudodami tarpinį kintamąjį res
    return res


def atimk(sk1: float, sk2: float) -> int | float:  # variantas be tarpinio kintamojo
    return sk1 - sk2


def daugink(sk1: int | float, sk2: int | float) -> int | float:
    return sk1 * sk2


def dalink(sk1: int | float, sk2: int | float) -> float:
    return sk1 / sk2
