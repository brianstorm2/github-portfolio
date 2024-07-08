class LazyList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def lazy_ones():
    return LazyList(1, lazy_ones)

def fib_sequence(a=0, b=1):
    return LazyList(a, lambda: fib_sequence(b, a+b))


def fib(i):
    current_num = fib_sequence()
    count = 0
    while count < i:
        current_num = current_num.next()
        count += 1
    return current_num.value


def combine(l1, l2):
    return LazyList(l1.value, lambda: combine(l2, l1.next()))

def multiplication_row(x):
    def multi_row(y=0):
        return LazyList(lambda: x * y, lambda: multi_row(y + 1))
    return multi_row()

def multiplication_table():
    def multi_table(x=0):
        return LazyList(lambda: multiplication_row(x), lambda: multi_table(x + 1))
    return multi_table()

def square_numbers():
    mult_table = multiplication_table()
    def squares(x=0):
        row = mult_table
        for _ in range(x):
            row = row.next()
        element = row.value()
        for _ in range(x):
            element = element.next()
        return LazyList(lambda: element.value(), lambda: squares(x + 1))
    return squares()

def lazy_squares():
    """ Generate a lazy list of square numbers using the diagonal of the multiplication table. """
    def diagonal(x=0):
        # Accessing the diagonal directly
        return LazyList(lambda: x * x, lambda: diagonal(x + 1))
    return diagonal()

square = lazy_squares()
current = square()
for _ in range(10):  # Print the first 10 square numbers
    print(current.value(), end=' ')
    current = current.next()


def filter(f, l):
    if l is None:
        return None
    elif f(l.value()):
                return LazyList(l.value, lambda: filter(f, l.next()))
    elif f(1.value()) %2 != 0:
        return LazyList(l.value, lambda: filter(f, l.next()))
    else:
        return filter(f, l.next())
