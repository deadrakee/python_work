# We have a dictionary with three key-value pairs. Each value is of type dictionary. This dictionary has two key-value pairs.
# The second pairs contain place and simple string. The first pair(name-value), has a value of type dictionary. 
# This dictionary has two key-value pairs first_name & last_name. The values are simple strings.

users = {
    #key_1  : val_1
    'thardy': {
        #key_2: val_2 
        'name': {
                # key_3     : val_3
                'first_name': 'Tom', 
                'last_name' : 'Hardy',
        },
        'place': 'usa'
    },

    'bcumberbatch': {
        'name': {
                'first_name': 'benedict',
                'last_name': 'Cumberbatch',
        },
        'place': 'England'
    },

    'mbilalov' : {
        'name': {
                'first_name': 'mihail',   
                'last_name': 'bilalov',
        },
        'place': 'bulgaria'    
    }
}


for key_1, val_1 in users.items():
    for key_2, val_2 in val_1.items():
        if key_2 == 'name':
            print("\nActor is:")
            for key_3, val_3 in val_2.items():
                print( f"\t{val_3.title()}" )
        elif key_2 == 'place':
            print(f"from:\t{val_2.title()}")