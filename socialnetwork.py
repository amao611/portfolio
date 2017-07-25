class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.connections = []

    def add_connection (self, connection):
        self.connections.append(connection)

    def printUser(self):
        print("Name: " + self.name)
        print("Username: " + self.user)
        print("Connections: ")
        print(self.connections)

    def printconnections(self):
        print(self.connections)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        global totalUsers
        self.totalUsers = []

    def add_user (self, user):
        self.totalUsers.append(user)

    def printall(self):
        print(self.totalUsers)

def main():
    # Define the program flow for your user interface here.
    user1 = User("Alice Mao", "alicem")
    user2 = User("Elisa Horta", "elisah")

    user2.add_connection("Jennifer Lawrence")
    user2.add_connection("Donald Trump")
    user2.add_connection("Will Farrow")
    user2.add_connection("Kevin Hart")
    user2.add_connection("Jimmy Fallon")

    user1.add_connection("Elisa Horta")
    user1.add_connection("Baolinh Nguyen")
    user1.add_connection("Ivy Chen")
    user1.add_connection("Janet Watson")
    user1.add_connection("Ginni Rometty")


    network1 = Network()
    network1.add_user(user2.name)
    network1.add_user(user1.name)

    print("Founders of this awesome social media platform: ")
    user1.printUser()
    user2.printUser()

    #user1.add_connection(user2.name)
    #user2.add_connection(user1.name)

    print("Ready to create your own profile?")
    global inputName                            #takes user input for creating new user
    inputName = input("Enter your name: ")
    inputUser = input("Enter your username: ")

    def createUser():                           #function that creates user based on user input
        global objectName
        objectName =inputName
        objectName = User(inputName, inputUser)
        network1.add_user(objectName.name)
        print("You are now in the network")
        print("Network:")
        network1.printall()

    createUser ()                               #calls function
    print("Now type the names of your friends with an enter between each friend to add them to your connections list. Type 'done' when finished.")

    while True:
        friendName = input()
        if friendName != "done":
            objectName.add_connection(friendName)
        elif friendName == "done":
            print("Here are your connections: ")
            objectName.printconnections()
            break

    '''deleteornah =input("See a friend you don't like? Delete them from your connections list by typing 'delete'")

    if deleteornah == "delete":
        notFriend=input("Type their name please.")
#        for i in range(len(connections)):
        if connections[i] == notFriend:
            print("test")


    else:
        print("Looks like you have no enemies...good for you!")
'''


# Runs your program.
if __name__ == '__main__':
    main()
