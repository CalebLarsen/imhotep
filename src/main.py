from imhotep_game import game_core, State, Input  # noqa: F401

def main():
    state = State()
    input = 0, 0, 300, 2500
    while not state.finished:
        state = game_core(state, input)
    state.print()

if __name__ == "__main__":
    main()
