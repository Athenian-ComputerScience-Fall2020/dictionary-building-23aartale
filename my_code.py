# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
def sports_dict():
    sports_book = {}
    while True:
        team = input("Say a football team- ")
        player = input("Say their best player- ")
        tries = input("if your done type y, if not no: ")
        if tries == 'y':
            break
        sports_book[team] = player
        for x, y in sports_book.items(): 
            print(x,y)


sports_dict()