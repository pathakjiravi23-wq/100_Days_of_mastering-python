# Special / Magic Methods
# Learn these after the fundamentals:
# __str__()
# __repr__()
# __len__()
# __eq__()
# __lt__()
# __add__()


class Book:
    def __init__(self, name, price: float | None = None) -> None:
        self.name = name
        self.price = price

    def __str__(self):  # it shows how originally print fucnt works under the hood
        return self.name

    def __repr__(self):  # developer friendly both used to print object's data
        return f"Book(name='{self.name}', age={self.price})"

    # If __str__() doesn't exist, Python can fall back to __repr__().
    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(
        self, other
    ):  # cannot be compared if price ==none due to its nonetype and int nature of price
        return self.price < other.price

    def __add__(
        self, other
    ):  # cannot be added if price ==none due to its nonetype and int nature of price
        return self.price + other.price


objref = Book("Alice", 21222)
print(objref)  # uses __str__()
print(repr(objref))  # uses repr fucnt
objref = Book(["alice", "lalit", "laluyara"], 21222)
print(len(objref))
print(repr(objref))
objref2 = Book("Ballu", 21223)
print(objref == objref2)
print(objref2 > objref)
print(objref + objref2)


class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    # Makes the object iterable
    # Used by: for x in obj
    def __iter__(self):
        return iter(self.numbers)

    # Makes the object an iterator
    # Used by: next(obj)
    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value

        raise StopIteration

    # Used by: obj[index]
    def __getitem__(self, index):
        return self.numbers[index]

    # Used by: obj[index] = value
    def __setitem__(self, index, value):
        self.numbers[index] = value

    # Used by: value in obj
    def __contains__(self, value):
        return value in self.numbers

    # Used by: obj()
    def __call__(self):
        return sum(self.numbers)


# ==================================================
# TESTING
# ==================================================

# Creating an object
numbers = Numbers([10, 20, 30, 40, 50])

print("Original object:")
print(numbers.numbers)


# --------------------------------------------------
# 1. __iter__()
# --------------------------------------------------

print("\n1. Testing __iter__()")

for number in numbers:
    print(number)


# --------------------------------------------------
# 2. __next__()
# --------------------------------------------------

print("\n2. Testing __next__()")

print(next(numbers))
print(next(numbers))
print(next(numbers))


# --------------------------------------------------
# 3. __getitem__()
# --------------------------------------------------

print("\n3. Testing __getitem__()")

print(numbers[0])
print(numbers[2])
print(numbers[4])


# --------------------------------------------------
# 4. __setitem__()
# --------------------------------------------------

print("\n4. Testing __setitem__()")

numbers[1] = 200

print(numbers.numbers)
print(numbers[1])


# --------------------------------------------------
# 5. __contains__()
# --------------------------------------------------

print("\n5. Testing __contains__()")

print(30 in numbers)
print(100 in numbers)


# --------------------------------------------------
# 6. __call__()
# --------------------------------------------------

print("\n6. Testing __call__()")

print(numbers())


# --------------------------------------------------
# 7. Normal object attributes
# --------------------------------------------------

print("\n7. Accessing object attributes")

print(numbers.numbers)
print(numbers.index)
