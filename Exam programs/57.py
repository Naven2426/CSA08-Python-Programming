def generate_pythagorean_triples(limit):
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c < limit:
                print(f"{a}, {b}, {int(c)}")
