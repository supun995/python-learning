#Generator expressions are a concise way to create generators.
# They are similar to list comprehensions but use parentheses instead of square brackets and are more memory efficient.
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)