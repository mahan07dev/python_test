def Pythagoras():
    results = []
    numbers = set()
    for a in range(1, 501):
        for b in range(a, 501):  # Start from 'a' to avoid duplicate pairs
            for c in range(b, 501):  # Start from 'b' to avoid duplicate pairs
                if a**2 + b**2 == c**2:
                    results.append((a, b, c))
                    numbers.update([a, b, c])
    return results, sorted(numbers)

pythagorean_triplets, pythagorean_numbers = Pythagoras()
print("Pythagorean Triplets:", pythagorean_triplets)
print("در بالا تمام سگانه ها هستند و در پایین تمام اعداد به ترتیب بصورت جداگانه قرار دارند")
print("Sorted Numbers from Triplets:", pythagorean_numbers)