### 8-13. User Profile:

def build_profile(first, last, **profile):
    """make a person ID"""
    profile['first'] = first
    profile['last'] = last
    return profile

person = build_profile("Gabriela", "Sabcheva", hair="black", body="sexy", personality="intelligent")
for key, value in person.items():
    print(key,"-", value)