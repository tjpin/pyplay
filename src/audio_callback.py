def play_next(play, current: str, playlist):
    for index, song in enumerate(playlist):
        if playlist[index] == current:
            try:
                play(playlist[index + 1])
                break
            except IndexError:
                print("End of list")


def play_previous(play, current: str, playlist):
    for index, song in enumerate(playlist):
        if playlist[index] == current:
            try:
                play(playlist[index - 1])
            except IndexError:
                print("End of list")

