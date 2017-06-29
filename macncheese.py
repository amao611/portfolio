start = '''
You're desperate for money to continuously feed your mac n' cheese obsession, and you heard on social media that there is treasure at a place located in the middle of nowhere. You pack your things immediately and go hiking.
While hiking, you reach a point where the path diverges into two separate paths.
Which path will you continue on?
'''

print(start)

print("Type 'left' to go left or 'right' to go right.")
while True:
    user_input = input()
    if user_input == "left":#left path ded
        print("You decide to go left, and you casually proceed. However, you accidentally step into a giant hole that you didn't notice, and hit your head as you fall to your death.") # finished the story by writing what happens
        break
    elif user_input == "right":#right path live
        print("You choose to go right and you avoid the spiky vines that were blocking the path. As you keep walking, you encounter 2 tunnels. Which tunnel will lead you to the treasure?") # finished the story writing what happens
        print("Type 'left' to go left or 'right' to go right.")

        user_input = input()
        if user_input == "left":#left cave live
            print("You made it past the stinky bat caves. After several minutes of walking, you reach 2 bridges.")
            print("Type 'left' to go left or 'right' to go right.")

            user_input = input()
            if user_input == "left":#left bridge live
                print("You successfully cross the bridge using your childhood gymnastic skills, and in a few feet after walking, you find the treasure!!! YAYYYY! Now you're a millionaire, and can satisfy your crazy mac n' cheese")
            elif user_input == "right":#right bridge ded
                print("Sadly, your six years of gymnastics wasn't good enough for you to cross this bridge. It collapsed, smushing you under it and killing you instantly as your body floats away in the river.")
                break
            elif user_input != "left" or "right":#response when user doesn't give correct input
                print("You didn't select the options given. You die because you didn't follow the directions.")
                break


        elif user_input == "right":#right cave ded
            print("You enter the tunnel on the right side, but then you get stung by a poisonous bug. When you wake up, you realize there are bats eating you alive. You are now dead.")
            break

        elif user_input != "left" or "right":#response when user doesn't give correct input
            print("You didn't select the options given. You die because you didn't follow the directions.")
            break

    elif user_input != "left" or "right":#response when user doesn't give correct input
        print("You didn't select the options given. You die because you didn't follow the directions.")
        break
