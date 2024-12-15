midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

final_grades = [max(pair) for pair in zip(midterms, finals)]
final_grades2 = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}

grades = zip(students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)


print(final_grades)
print(final_grades2)
print(dict(grades))