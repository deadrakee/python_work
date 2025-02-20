#Banned list
banned = ["alice", "bob", "eve"]
user = "bob"

print(f"Is {user} banned? - {user in banned}")

# allowed list
print(f"Is {user} allowed? - {user not in banned}")