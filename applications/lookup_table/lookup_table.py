import math
import random
look_up_table = {

}
def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    if (x,y) in look_up_table:
        return look_up_table[(x,y)]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        look_up_table[(x,y)] = v
        return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
