# Print the multiplication table for a given number up to 10, but skip the forth iteration.


number = 3

for i in range(1, 11):
    if i == 4:
        continue
    print(number,'x', i, '=', number * i)


 