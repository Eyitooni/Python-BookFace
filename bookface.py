# Dictionary that will hold user as key and friend in a set 
datacenter = {}

# Opening and reading the file 
with open("facebook_data.txt", "r") as database:
    # The number of users that are in the data set to iterate over
    data = int(database.readline())
    # The rest of the lines present in the database
    lines = database.readlines()
    # Loops through by the number of users 
    for user in range(data):   
        # creates a dictionary key value of each user iterated on and sets their value to an empty set  
        datacenter[user] = set()
        # Nested loop to read the lines of each data in the data set 
        for users in lines:  
            # Seperates each friend into their individual id and then adds to the set if the user being iterated over is present looking both ways then adding to the set
            id = users.split()
            if (user == int(id[0])):
                datacenter[user].add(id[1])
            if(user == int(id[1])):
                datacenter[user].add(id[0])


def suggestion(user):
    #sets the most common to the length of the users 
    mostcommon = len(datacenter)   
    #loops through the lines in the keys 
    for data in range(len(datacenter)): 
        #Assures the user needing friends doesnt get recommended to themselves
        if data != user:       
            #Finds the difference in adding the dict value set togather 
            templen = len(datacenter[data])
            newlen = len(datacenter[user].union(datacenter[data]))
            similarity = newlen - templen
            #Based on how much duplicates were removed we know most common
            if (similarity < mostcommon): 
                mostcommon = similarity
                friendSuggestion = data
    return friendSuggestion

while True:
    #Catches error of invalid inputs
    findFriend = int(input("Enter the User by their ID 0 - 1000: "))
    try:
        suggestion(findFriend)
    except:
        break 
    print(f"Your Recommended Friend Suggestion is: {suggestion(findFriend)}")
