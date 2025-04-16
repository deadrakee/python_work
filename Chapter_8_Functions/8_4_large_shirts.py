### 8-4. Large Shirts:

def make_shirt(size='L', stamp='I love Python'):
    """"Tshirt with a printed stamp on it"""
    print(f"\n{size.title()} sized T-shirt with stamp: {stamp}")

make_shirt()
make_shirt('M')
make_shirt('M', "I love C++")
make_shirt(stamp="I love Java")