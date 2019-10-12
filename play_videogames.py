
do_you_want_to = input("Do you want to play videogames? (Yes/No): ").upper()
if do_you_want_to == "YES":
    you_want = True
elif do_you_want_to == "NO":
    you_want = False
else:
    print("I dont know what did you said, you have to answer with Yes and No, I will take this as a No")
    you_want = False

do_you_have_free_time = input("Do you have free time? (Yes/No): ").upper()
if do_you_have_free_time == "YES":
    free_time = True
elif do_you_have_free_time == "NO":
    free_time = False
else:
    print("I dont know what did you said, you have to answer with Yes and No, I will take this as a No")
    free_time = False

singleplayergames = input("Do you like single player games? (Yes/No): ").upper()
if singleplayergames == "YES":
    singleplayer = True
elif singleplayergames == "NO":
    singleplayer = False
else:
    print("I dont know what did you said, you have to answer with Yes and No, I will take this as a No")
    singleplayer = False

multiplayergames = input("Do you like multiplayer games? (Yes/No): ").upper()
if multiplayergames == "YES":
    multiplayer = True
elif multiplayergames == "NO":
    multiplayer = False
else:
    print("I dont know what did you said, you have to answer with Yes and No, I will take this as a No")
    multiplayer = False

do_you_like_games = singleplayergames or multiplayergames

if you_want and free_time and do_you_like_games:
    print("Well then, go and play some videogames")
else:
    print("Well then, dont play videogames")










