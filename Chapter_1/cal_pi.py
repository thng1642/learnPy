# number pi = 4/1 - 4/3 + 4/5 - 4/7 + ...
# this is Leibniz formula

def calculate_pi(n: int) -> float:
    demoninator: float = 1.0
    operator: int = 1
    pi:float = 0.0
    for _ in  range(n):
        pi += operator * (4.0 / demoninator)
        demoninator += 2.0
        operator *= -1
    return pi

if __name__ == "__main__":
    print(calculate_pi(100000))