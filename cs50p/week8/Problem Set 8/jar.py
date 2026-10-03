class Jar:
    def __init__(self, capacity=12):
        if type(capacity) is not int or capacity < 0:
            raise ValueError("Invalid capacity.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{"🍪" * self._size }"

    def deposit(self, n):
        if self._size+n > self._capacity:
            raise ValueError("Too many cookies to fit!!")
        self._size += n

    def withdraw(self, n):
        if self._size -n < 0:
            raise ValueError("Not enough cookie's in the jar!")
        self._size -= n

    @property # Max cookie
    def capacity(self):
         return self._capacity

    @property # Current cookie count
    def size(self):
        return self._size

def main():
    my_jar = Jar(12)
    print(f"Jar Capacity: {my_jar.capacity}")

    my_jar.deposit(5)
    print(my_jar)
    print(f"Current Cookies: {my_jar.size}")

    my_jar.withdraw(1)
    print(my_jar)
    
    my_jar.withdraw(5)

if __name__ == "__main__":
    main()