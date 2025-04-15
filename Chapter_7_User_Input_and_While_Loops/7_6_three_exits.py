### 7-6. Three Exits:

# version selector
variant_prompt = "This program has three implementations. Type the number of your choice:\n"
variant_prompt += "\t1 - Four prompts loop.\n"
variant_prompt += "\t2 - Run until all four people tell an appropriate age.\n"
variant_prompt += "\t3 - Type 'quit' to exit.\n"
variant_prompt += "Variant: "

variant = int(input(variant_prompt))


# Run exactly four prompts, regardless of the input.
if variant == 1:

    age_prompt = "\nHow old are you: "

    age = 0
    price = 0
    people_count = 1
    max_count = 4

    while people_count <= max_count:
        age = int(input(f"{age_prompt} number {people_count}? "))

        if age < 3:
            price = 0

        elif age < 13:
            price = 10

        else:
            price = 15

        print(f"Your ticket costs {price}$.")
        people_count += 1


# Run until all four people enter an age between 1 and 100 years.
if variant == 2:

    age_prompt = "\nHow old are you: "

    age = 0
    price = 0
    people_count = 1
    max_count = 4

    while people_count <= max_count:
        age = int(input(f"{age_prompt} number {people_count}? "))

        if age < 1:
            price = -1

        elif age < 3:
            price = 0
        
        elif age < 13:
            price = 10
        
        elif age < 100:
            price = 15

        else:
            price = -1
        
        if price == -1:
            print("Do not lie to me...")
        else:
            print(f"Your ticket costs {price}$.")
            people_count += 1

if variant == 3:

    prompt = "\nEnter how old are you or 'quit': "
    message = ""
    price = 0

    while True:
        message = input(prompt)

        if message == 'quit':
            break

        else:
            age = int(message)

            if age < 3:
                price = 0

            elif age < 13:
                price = 10

            else:
                price = 15

            print(f"Your ticket costs {price}$.")