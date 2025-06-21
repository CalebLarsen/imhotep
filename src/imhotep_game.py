import random
# Workforce, Workforce_Storehouses, People_Storehouses, Tels_To_Plant
type Input = tuple[int, int, int, int]

class State:
    def __init__(self):
        self.people: int = 300000
        self.tels_flooded: int = 2500
        self.storage: float = 330
        self.years: int = 0
        self.errors: int = 0
        self.levels: int = 0
        self.finished: bool = False

    def print(self):
        print("==============")
        print("People:", self.people)
        print("Tels:", self.tels_flooded)
        print("Storage:", self.storage)
        print("Years:", self.years)
        print("Errors:", self.errors)
        print("Levels:", self.levels)
        print("Finished:", self.finished)
        print("==============")

def jubileeStatus(state: State) -> State:
    if state.levels < 7 and state.errors > 3 and state.people < 300000 and state.storage * 1000 < state.people + 50:
        state.errors += 1
    return state


def telsToPlantStatus(
    state:State, tels_to_plant: int) -> State:
    if tels_to_plant > state.tels_flooded or tels_to_plant < 0:
        state.errors += 1
        state.finished = True
    elif tels_to_plant > state.storage * 100:
        if state.storage * 100 < 1:
            state.finished = True
        else:
            state.errors += 1
            state.finished = True
    elif tels_to_plant > state.people * 10:
        state.errors += 1
        state.finished = True
    return state

def pyramidCollapseStatus(state: State, workforce: int, workers_fed: int) -> tuple[State, int, int, int]:
    chance_of_collapse = random.randint(1, 50)
    if chance_of_collapse <= 9 and state.levels > 4:
        levels_collapsed = random.randint(2, 3)
        state.levels -= levels_collapsed
        workforce -= workforce // 4
        workers_fed -= workers_fed // 4
    else:
        levels_collapsed = 0
    return state, workforce, levels_collapsed, workers_fed

def rebellionStatus(state: State, workers_fed: int, workforce: int) -> tuple[State, int, int, int, int]:
    rebel = random.randint(1, 40)
    bad_happened = False
    workers_killed = 0
    workers_starved = 0
    if rebel <= 4:
        bad_happened = True
        workers_starved = 0
    elif workers_fed < workforce:
        bad_happened = True
        workers_starved = workforce - workers_fed
        workforce -= workers_starved
        state.errors += 2
    if (bad_happened) and workforce > 0:
        workers_killed = random.randint(1, 100)
        workforce -= workers_killed
        workers_fed -= workers_killed
    return (
        state,
        workforce,
        workers_killed,
        workers_starved,
        workers_fed,
    )

def randomEventStatus(state: State, workforce: int, workers_fed: int) -> tuple[State, int, int]:
    chance = random.randint(1, 300)
    dead = 0
    amount = 0
    escapees = 0
    if chance < 19:
        dead = int(state.people * random.random())
        state.people -= dead
    elif chance < 210 and chance > 165:
        dead = int(state.people * random.random())
        state.people -= dead
    elif chance > 75 and chance < 130:
        amount = random.randint(20, 70)
        state.storage += amount
    elif chance > 255 and chance < 260:
        amount = random.randint(1, 100)
        state.storage += amount
    elif chance > 282:
        escapees = int(workforce * random.random())
        workforce -= escapees
        workers_fed -= escapees
    return state, workforce, workers_fed

def randomEventStatus2(state: State) -> State:
    chance = random.randint(1, 30)
    amount = 0
    if chance > 22:
        amount = random.randint(1, 50)
        state.storage += amount
    elif chance > 12 and chance < 18:
        amount = random.randint(1, 50)
        state.tels_flooded += amount
    elif chance < 8:
        amount = state.people * random.random()
        state.people -= amount
    return state

def harvestStatus(state: State, tels_to_plant: int) -> State:
    if state.levels > state.years * 2:
        state.errors -= 1
    state.years += 1
    state.storage -= tels_to_plant / 100
    priest_feed: int = 0
    if state.errors >= 0 and state.storage > 0:
        priest_feed = int(((random.random() * state.storage) + state.errors * 4) / 2)
        if priest_feed < 2 and priest_feed > 0:
            state.storage -= priest_feed
            if state.storage < 0:
                state.storage = 0
        else:
            priest_feed = 0
    elif state.errors < 0 and state.storage > 0:
        priest_feed = int(state.storage * random.random() / 10)
        state.storage += priest_feed
    state.tels_flooded = int(random.randint(1, 4000) + priest_feed / 2)
    harvest_rate: float = random.random() * 0.35
    state.storage += int(tels_to_plant * harvest_rate)
    return state

def feedStatus(state:State, workers_fed: int, workforce: int, people_fed: int) -> tuple[State, int, int]:
    starved_people = 0
    if workers_fed > workforce:
        workers_fed = workforce
    new_people = people_fed - state.people
    if new_people < 0:
        new_people = 0
    new_people += random.randint(1, 1000)

    if state.people > people_fed:
        starved_people = state.people - people_fed
        state.people -= starved_people
        state.errors += 1
    elif people_fed > state.people:
        people_fed = state.people


    if starved_people > state.people * 0.45:
        state.finished = True

    state.people += new_people
    return state, workers_fed, people_fed

def yearEndStatus(state: State, workforce: int, workers_fed: int) -> State:
    state.people += workers_fed
    state.levels += workers_fed // 90000
    if state.levels > 20:
        state.levels = 20
    if state.errors > 7:
        state.finished = True
    return state

def workforceStatus(state: State, workforce: int) -> State:
    if workforce > state.people or workforce < 0:
        state.errors += 1
        state.finished = True
    else:
        state.people -= workforce
    return state

def workerStorageStatus(state: State, worker_storage: int) -> tuple[State, int]:
    workers_fed = 0
    if worker_storage > state.storage or worker_storage < 0:
        state.errors += 1
        state.finished = True
    else:
        workers_fed = worker_storage * 1000
        state.storage -= worker_storage
    return state, workers_fed

def peopleStorageStatus(state: State, people_storage: float) -> tuple[State, int]:
    people_fed = 0
    if people_storage > state.storage or people_storage < 0:
        state.errors += 1
        state.finished = True
    else:
        people_fed = int(people_storage * 1000)
        state.storage -= people_storage
    return state, people_fed

def clearScreen():
    for i in range(40):
        print("")
    return


def get_input() -> Input:
    workforce = int(input("Workforce: "))
    work_store = int(input("Workforce storehouses: "))
    people_store = int(input("People storehouses: "))
    tels_planted = int(input("Tels to plant: "))
    return workforce, work_store, people_store, tels_planted

def game_core(state: State, input: Input) -> State:
    if not (state.years < 12 and state.levels < 20):
        state.finished = True
        return state

    workforce, worker_storage, people_storage, tels_to_plant = input

    # workforce choice
    state = workforceStatus(state, workforce)
    if state.finished:
        return state
    # worker_storage choice
    state, workers_fed = workerStorageStatus(state, worker_storage)
    if state.finished:
        return state

    # people_storage choice
    state, people_fed = peopleStorageStatus(state, people_storage)
    if state.finished:
        return state

    # tels to plant
    state = telsToPlantStatus(state, tels_to_plant)
    if state.finished:
        # game over man
        return state

    # feed people
    state, workers_fed, people_fed = feedStatus(state, workers_fed, workforce, people_fed)
    if state.finished:
        # game over man
        return state

    # handle rebellion
    (
        state,
        workforce,
        workers_killed,
        workers_starved,
        workers_fed,
    ) = rebellionStatus(state, workers_fed, workforce)

    # handle pyramid collapse
    state, workforce, levels_collapsed, workers_fed = (
        pyramidCollapseStatus(state, workforce, workers_fed)
    )

    # handle the harvest - logic only
    state = harvestStatus(state, tels_to_plant)

    # handle random events
    state = randomEventStatus2(state)

    # handle more random events
    state, workforce, workers_fed = (
        randomEventStatus(state, workforce, workers_fed)
    )

    # handle end of year stuff
    state = yearEndStatus(
        state, workforce, workers_fed
    )
    if state.finished:
        # game over man
        return state

    # handle the jubilee
    if state.years == 6:
        state = jubileeStatus(state)

    return state

def gameLoop():
    state: State = State()  
    clearScreen()

    while not state.finished:
        input = get_input()
        state = game_core(state, input)
        state.print()
    return


def main():
    gameLoop()
    return


if __name__ == "__main__":
    main()
