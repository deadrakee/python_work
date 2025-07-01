### 9-16. Python Module of the Week:

# playground using Regex module(re)
import re

# 1. Matching a substring in a string
print("\n\nPart 1")

text = "All your base are belong to us"
substring = "All"

match = re.search(substring, text)

if match is not None:
    print(f"Found '{match.re.pattern}' in\n{match.string}")
    print(f"from {match.start()} to {match.end()}({text[match.start():match.end()]})")
else:
    print("No match")


# 2. Compile a substring as a regex object to perform operations faster
print("\n\nPart 2")
text_2 = "The random module shouldn’t be used when building security-related applications, but it works well for many fun and interesting projects."
substring_2 = "security"

# compile substring_2 for faster matching
regex_obj_1 = re.compile(substring_2)

print(regex_obj_1.search(text_2))