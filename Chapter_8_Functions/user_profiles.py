def build_profile(first, last, **user_param):
    """create a dict from arbitary number of key-values"""
    user_param["first_name"] = first
    user_param["last_name"] = last
    user_param["location"] = "Vt"
    return user_param


user = build_profile("Boyan", last ="Sabchev",
                     location='sofia', 
                     age=28)
print(user) 