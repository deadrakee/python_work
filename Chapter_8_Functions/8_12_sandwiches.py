### 8-12. Sandwiches:

def make_sandwich(*products):
    print("\nSandwich with:")
    for prod in products:
        print(f"\t{prod}")

make_sandwich("cheese", "ham", "cheddar")
make_sandwich("tomato", "avocado", "cucumber")
make_sandwich("mozarella", "philadelfia", "peperoni")