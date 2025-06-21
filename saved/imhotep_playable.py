import random
import time

pharoah_pleased: int = 1
pharoah_displeased: int = 2
pharoah_watching: int = 3
tels_out_of_range: int = 4
grain_shortage: int = 5
people_shortage: int = 6
# tels_planted: int = 7
mummied: int = 8
collapsed: int = 9
no_collapse: int = 10
starvation: int = 11
rebellion: int = 12
no_rebellion: int = 13
hyksos_attack: int = 14
achean_attack: int = 15
minoan_tribute: int = 16
bride_dowry: int = 17
workers_escape: int = 18
nothing_happened: int = 19
nubian_tribute: int = 20
military_campaign: int = 21
pestilence: int = 22
storehouse_claimed: int = 23
storehouse_given: int = 24
people_starvation: int = 25
mass_starvation: int = 26
workforce_error: int = 27
worker_storage_error: int = 28
people_storage_error: int = 29
exile: int = 30

overseers: list[str] = [
    "MENE-PTAH",
    "RA-ANX-TETA",
    "ATUM-ATON",
    "SETEP-EN-RE",
    "RAMOSE",
    "MERI-ATUM",
    "KA-RES",
    "MAATUM",
    "MERI-TEHU",
    "TOTHMES",
    "RE-MES-SES",
    "PTAHMES",
    "MERIPASHTU",
]


def titleChange(status: int) -> str:
    if status == pharoah_pleased:
        title = "GREAT LORD IMHOTEP"
    elif status == pharoah_displeased:
        title = "IMHOTEP THE INCOMPETENT"
    elif status == pharoah_watching:
        title = "IMHOTEP-HORUS-WATCHES"
    return title


def jubileeStatus(levels: float, people: float, storage: float, errors: int) -> tuple[int, int, str]:
    if levels == 20 or (
        levels > 10 and people > 300000 and storage * 1000 > people and errors < 2
    ):
        status = pharoah_pleased
    elif levels < 7 and errors > 3 and people < 300000 and storage * 1000 < people + 50:
        status = pharoah_displeased
        errors += 1
    else:
        status = pharoah_watching
    return status, errors, titleChange(status)


def jubileeText(status: int) -> list[str]:
    basic_text = [
        "%sJUBILEE" % (" " * 16),
        "IT IS TIME FOR PHAROAH'S JUBILEE.",
        "YOU HAVE USED HALF OF YOUR TIME.",
    ]
    status_text = []
    if status == pharoah_pleased:
        status_text = [
            "PHAROAH IS PLEASED WITH YOUR",
            "PERFORMANCE SO FAR AND BESTOWS A GREAT",
            "HONOR ON YOU. FROM THIS MOMENT YOU ARE",
            "KNOWN AS 'GREAT LORD IMHOTEP'.",
        ]
    elif status == pharoah_displeased:
        status_text = [
            "PHAROAH IS DISPLEASED WITH YOU AND",
            "DESIRES FOR YOU TO SUFFER THE DISHONOR",
            "OF BEARING THE TITLE 'IMHOTEP THE",
            "INCOMPETENT'.",
        ]
    elif status == pharoah_watching:
        status_text = [
            "PHAROAH FEELS YOU HAVE NOT PUT FORTH A",
            "GOOD EFFORT AND DESIRES TO REMIND YOU",
            "OF YOUR RESPONSIBILITIES WITH THE",
            "TITLE 'IMHOTEP-HORUS-WATCHES'.",
        ]
    basic_text.extend(status_text)
    return basic_text


def getOverseerName(overseer_id: int) -> str:
    index = overseer_id % len(overseers)
    return overseers[index]


def telsToPlantStatus(
    tels_to_plant: int, tels_flooded: int, storage: float, people: int, errors: int, overseer_id: int
) -> tuple[int, int, int]:
    if tels_to_plant > tels_flooded or tels_to_plant < 0:
        errors += 1
        status = tels_out_of_range
        overseer_id += 1
    elif tels_to_plant > storage * 100:
        if storage * 100 < 1:
            status = mummied
        else:
            errors += 1
            status = grain_shortage
    elif tels_to_plant > people * 10:
        errors += 1
        status = people_shortage
    else:
        status = nothing_happened
    return status, errors, overseer_id


def telsToPlantText(status: int, title: str, overseer_id: int, storage: float, people: float) -> list[str]:
    overseer_name = getOverseerName(overseer_id - 1)
    new_overseer_name = getOverseerName(overseer_id)
    if status == tels_out_of_range:
        status_text = [
            "PHAROAH HAS KILLED " + overseer_name,
            "YOUR OVERSEER.",
            "I AM " + new_overseer_name + " YOUR NEW OVERSEER.",
            "NOW...",
        ]
    elif status == grain_shortage:
        status_text = [
            "THERE IS ONLY ENOUGH GRAIN TO PLANT " + str(storage * 100 - 1),
            "TELS.",
        ]
    elif status == people_shortage:
        status_text = [
            "THERE ARE ONLY ENOUGH PEOPLE TO PLANT",
            str(people * 10) + " TELS.",
        ]
    elif status == mummied:
        status_text = ["ZOSER WANTS YOU MUMMIFIED ALIVE IN THE", "HOUSE OF THE DEAD."]
    else:
        status_text = []
    return status_text


def telsToPlantPrompt(tels_flooded: int) -> list[str]:
    text = ["FROM " + str(tels_flooded) + " TELS, HOW MANY DO YOU", "WISH TO PLANT? "]
    return text


def pyramidCollapseStatus(levels: float, workforce: int, workers_fed: int) -> tuple[int, float, int, int, int]:
    chance_of_collapse = random.randint(1, 50)
    if chance_of_collapse <= 9 and levels > 4:
        status = collapsed
        levels_collapsed = random.randint(2, 3)
        levels -= levels_collapsed
        workforce -= workforce // 4
        workers_fed -= workers_fed // 4
    else:
        status = no_collapse
        levels_collapsed = 0
    return status, levels, workforce, levels_collapsed, workers_fed


def pyramidCollapsedText(status: int, levels_collapsed: int) -> list[str]:
    status_text = []
    if status == collapsed:
        status_text = [
            str(levels_collapsed) + " COURSES OF THE PYRAMID HAVE",
            "COLLAPSED AND ONE-FOURTH OF THE WORK",
            "FORCE WAS LOST.",
        ]
    return status_text


def rebellionStatus(workers_fed: int, workforce: int, errors: int, overseer_id: int) -> tuple[int, int, int, int, int, int, int]:
    rebel = random.randint(1, 40)
    status = no_rebellion
    workers_killed = 0
    workers_starved = 0
    if rebel <= 4:
        status = rebellion
        workers_starved = 0
    elif workers_fed < workforce:
        status = starvation
        workers_starved = workforce - workers_fed
        workforce -= workers_starved
        errors += 2
    if (status == rebellion or status == starvation) and workforce > 0:
        workers_killed = random.randint(1, 100)
        overseer_id += 1
        workforce -= workers_killed
        workers_fed -= workers_killed
    return (
        status,
        errors,
        workforce,
        overseer_id,
        workers_killed,
        workers_starved,
        workers_fed,
    )


def rebellionText(
    status: int, workers_fed: int, workforce: int, workers_killed: int, overseer_id: int, workers_starved: int
) -> list[str]:
    overseer_name = getOverseerName(overseer_id - 1)
    new_overseer_name = getOverseerName(overseer_id)
    status_text = []
    if status == starvation:
        status_text = ["YOU HAVE STARVED " + str(workers_starved) + " WORKERS"]
    if (status == rebellion or status == starvation) and workers_killed > 0:
        text = [
            "THE WORKFORCE HAS REBELLED. " + str(workers_killed),
            "WORKERS, AND " + overseer_name + ", THE OVERSEER,",
            "WERE KILLED BY",
            "PHAROAH'S VICTORIOUS ANUBIS SQUADRON.",
            "THE GREAT ZOSER HAS CHOSEN " + new_overseer_name,
            "TO BE YOUR NEW OVERSEER.",
        ]
        status_text.extend(text)
    return status_text


def randomEventStatus(people: int, storage: float, workforce: int, workers_fed: int) -> tuple[int, int, float, int, int, int, int, int]:
    chance = random.randint(1, 300)
    dead = 0
    amount = 0
    escapees = 0
    if chance < 19:
        status = hyksos_attack
        dead = random.randint(1, people)
        people -= dead
    elif chance < 210 and chance > 165:
        status = achean_attack
        dead = random.randint(1, people)
        people -= dead
    elif chance > 75 and chance < 130:
        status = minoan_tribute
        amount = random.randint(20, 70)
        storage += amount
    elif chance > 255 and chance < 260:
        status = bride_dowry
        amount = random.randint(1, 100)
        storage += amount
    elif chance > 282:
        status = workers_escape
        escapees = random.randint(1, workforce)
        workforce -= escapees
        workers_fed -= escapees
    else:
        status = nothing_happened
    return status, people, storage, workforce, dead, amount, escapees, workers_fed


def randomEventText(status: int, dead: int, amount: int, escapees: int) -> list[str]:
    status_text = []
    if status == hyksos_attack:
        status_text = [
            "HYKSOS WITH CHARIOTS AND BLADES OF",
            "BLACK EVIL METAL HAVE ATTACKED KHEM.",
            str(dead) + " PEOPLE HAVE BEEN KILLED.",
        ]
    elif status == achean_attack:
        status_text = [
            "ACHEAN BARBARIANS FROM THE NORTHERN SEA",
            "HAVE RAIDED THE DELTA. " + str(dead),
            "PEOPLE HAVE BEEN KILLED.",
        ]
    elif status == minoan_tribute:
        status_text = [
            "MINOAN MERCHANTS HAVE BROUGHT " + str(amount),
            "STOREHOUSES OF GRAIN TO TRADE FOR",
            "METHODS OF BUILDING AS PRACTICED IN",
            "KHEMI.",
        ]
    elif status == bride_dowry:
        status_text = [
            "THE PHAROAH'S NEW SYRIAN BRIDE BROUGHT",
            "A DOWRY OF " + str(amount) + " STOREHOUSES",
            "OF GRAIN.",
        ]
    elif status == workers_escape:
        status_text = [
            "A FANATICAL REBEL-PRIEST HAS ESCAPED",
            "WITH " + str(escapees) + " WORKERS INTO THE ",
            "WILDERNESS OF THE SINAI.",
        ]
    return status_text


def randomEventStatus2(storage: float, tels_flooded: int, people: int) -> tuple[int, int, float, int, int]:
    chance = random.randint(1, 30)
    amount = 0
    if chance > 22:
        status = nubian_tribute
        amount = random.randint(1, 50)
        storage += amount
    elif chance > 12 and chance < 18:
        status = military_campaign
        amount = random.randint(1, 50)
        tels_flooded += amount
    elif chance < 8:
        status = pestilence
        amount = random.randint(1, people)
        people -= amount
    else:
        status = nothing_happened
    return status, amount, storage, tels_flooded, people


def randomEventText2(status: int, amount: int) -> list[str]:
    status_text = []
    if status == nubian_tribute:
        status_text = [
            "NUBIAN EMISSARIES HAVE BROUGHT TRIBUTE",
            "OF " + str(amount) + " STOREHOUSES OF GRAIN.",
        ]
    elif status == military_campaign:
        status_text = [
            "A MILITARY CAMPAIGN LED BY ZOSER HAS",
            "BROUGHT AN ADDDITIONAL " + str(amount) + " TELS",
            "INTO THE DOUBLE-KINGDOM.",
        ]
    elif status == pestilence:
        status_text = [
            "A PESTILENCE DESCENDED FROM AMEN-RE.",
            str(amount) + " PEOPLE DIED.",
        ]
    return status_text


def harvestStatus(storage: float, tels_to_plant: int, errors: int, levels: int, years: int) -> tuple[int, int, float, int, int, int, float]:
    if levels > years * 2:
        errors -= 1
    years += 1
    storage -= tels_to_plant / 100
    status = nothing_happened
    priest_feed: int = 0
    if errors >= 0 and storage > 0:
        priest_feed = int(((random.random() * storage) + errors * 4) / 2)
        if priest_feed < 2 and priest_feed > 0:
            status = storehouse_claimed
            storage -= priest_feed
            if storage < 0:
                storage: float = 0
        else:
            priest_feed = 0
    elif errors < 0 and storage > 0:
        priest_feed = int(random.randint(1, int(storage)) / 10)
        storage += priest_feed
        status = storehouse_given
    tels_flooded: int = int(random.randint(1, 4000) + priest_feed / 2)
    harvest_rate: float = random.random() * 0.35
    storage += int(tels_to_plant * harvest_rate)
    return status, years, storage, errors, priest_feed, tels_flooded, harvest_rate


def harvestText(status: int, storage: float, harvest_rate: float, priest_feed: int) -> list[str]:
    basic_text = [
        "THE HARVEST THIS YEAR WAS " + "%0.2f" % (harvest_rate),
        "    STOREHOUSES PER TEL.",
    ]
    status_text = []
    if status == storehouse_given:
        status_text = [
            "THE PRIESTS OF AMEN GAVE ZOSER, " + str(priest_feed),
            "    STOREHOUSES OF GRAIN.",
        ]
    elif status == storehouse_claimed:
        status_text = [
            str(priest_feed) + " STOREHOUSES OF GRAIN WERE CLAIMED",
            "    BY THE PRIESTS OF AMEN.",
        ]
    basic_text.extend(status_text)
    return basic_text


def feedStatus(workers_fed: int, workforce: int, people_fed: int, people: int, errors: int) -> tuple[int, int, int, int, int, int, int]:
    status = nothing_happened
    starved_people = 0
    if workers_fed > workforce:
        workers_fed = workforce
    new_people = people_fed - people
    if new_people < 0:
        new_people = 0
    new_people += random.randint(1, 1000)

    if people > people_fed:
        starved_people = people - people_fed
        people -= starved_people
        status = people_starvation
        errors += 1
    elif people_fed > people:
        people_fed = people

    if starved_people > people * 0.45:
        status = mass_starvation

    people += new_people

    return status, workers_fed, new_people, people, starved_people, errors, people_fed


def feedText(status: int, starved_people: int) -> list[str]:
    text = []
    if status == people_starvation or status == mass_starvation:
        text = ["YOU HAVE STARVED " + str(starved_people) + " PEOPLE."]
    if status == mass_starvation:
        text.extend(["ZOSER WANTS YOU MUMMIFIED ALIVE IN THE ", "HOUSE OF THE DEAD."])
    return text


def populationText(new_people: int) -> list[str]:
    text = ["THE POPULATION INCREASED BY " + str(new_people), "    PEOPLE."]
    return text


def yearEndText(levels: int, tels_flooded: int, years: int, errors: int, title: str, line_count: int) -> list[str]:
    text: list[str] = []
    if levels > 0 and levels < 21:
        text.extend(
            ["THE WORK FORCE HAS COMPLETED " + str(levels), "COURSES OF THE PYRAMID."]
        )
    if levels < 21 and tels_flooded < 1000:
        text.extend(["THE VIZIERS PREDICT A POOR FLOOD NEXT", "YEAR."])
        line_count += 2
    if levels < 21 and tels_flooded > 3700:
        text.extend(["THE MELTING SNOW OF ETHIOP WELLS THE", "NILE THIS SPRING."])
        line_count += 2
    if (levels < 10 and years > 6) or (errors > 3 and levels < 20):
        text.extend(["PHAROAH IS BOTHERED BY YOUR", "INEFFICIENCY."])
        line_count += 2
    if errors > 7:
        text.extend(
            [
                "HE HAS DECREED, THAT FOR YOUR MISTAKES,",
                "YOU WILL BE EXILED TO THE RED LAND OF",
                "THE EAST.",
            ]
        )
    else:
        if line_count < 2:
            text.extend([title + ",", "AN UNEVENTFUL YEAR."])
        elif line_count > 8 and line_count < 14:
            text.extend([title + ",", "A VERY EVENTFUL YEAR."])

    return text


def yearEndStatus(people: int, workforce: int, levels: int, workers_fed: int, errors: int) -> tuple[int, int, int]:
    people += workers_fed
    levels += workers_fed // 90000
    status = nothing_happened
    if levels > 20:
        levels = 20
    if errors > 7:
        status = exile
    return status, people, levels


def yearStartText(people: int, storage: float, tels_flooded: int) -> list[str]:
    text = [
        "POPULATION OF KHEMI - " + str(int(people)),
        "PHAROAH OWNS " + str(int(storage)) + " GRAIN STOREHOUSES.",
        "NILE FLOODED " + str(int(tels_flooded)) + " TELS OF LAND.",
    ]
    return text


def workforcePrompt() -> list[str]:
    text = ["# OF PEOPLE YOU WISH ON WORKFORCE "]
    return text


def workforceStatus(workforce: int, people: int, overseer_id: int, errors: int) -> tuple[int, int, int, int]:
    if workforce > people or workforce < 0:
        status = workforce_error
        overseer_id += 1
        errors += 1
    else:
        status = nothing_happened
        people -= workforce
    return status, overseer_id, errors, people


def workforceText(overseer_id: int, title: str, status: int) -> list[str]:
    text = []
    if status == workforce_error:
        overseer_name = getOverseerName(overseer_id - 1)
        new_overseer_name = getOverseerName(overseer_id)
        text = [
            title + ",",
            "ZOSER HEARD YOUR FOOLISHNESS.",
            "HE HAS EXILED " + overseer_name + ".",
            new_overseer_name + " HAS BEEN ASSIGNED AS",
            "OVERSEER.  NOW...",
        ]
    return text


def workerStoragePrompt(storage: float) -> list[str]:
    text = [
        "FROM " + str(int(storage)) + " STOREHOUSES OWNED BY RA,",
        "HOW MANY WILL FEED WORKERS? ",
    ]
    return text


def workerStorageStatus(worker_storage: float, storage: float, errors: int) -> tuple[int, float, float, int]:
    status = nothing_happened
    workers_fed = 0
    if worker_storage > storage or worker_storage < 0:
        status = worker_storage_error
        errors += 1
    else:
        workers_fed = worker_storage * 1000
        storage -= worker_storage
    return status, workers_fed, storage, errors


def workerStorageText(title: str, status: int) -> list[str]:
    text = []
    if status == worker_storage_error:
        text = [title + ",", "DO NOT JEST,", "THE HAWK'S EARS ARE SHARP."]
    return text


def peopleStoragePrompt(storage: float, people: int) -> list[str]:
    text = [
        "FROM " + str(storage) + " REMAINING STOREHOUSES,",
        "HOW MANY WILL FEED " + str(people),
        "REMAINING PEOPLE? ",
    ]
    return text


def peopleStorageStatus(people_storage: float, storage: float, errors: int) -> tuple[int, float, float, int]:
    status = nothing_happened
    people_fed = 0
    if people_storage > storage or people_storage < 0:
        status = people_storage_error
        errors += 1
    else:
        people_fed = people_storage * 1000
        storage -= people_storage
    return status, people_fed, storage, errors


def peopleStorageText(title: str, overseer_id: int, status: int) -> list[str]:
    text = []
    if status == people_storage_error:
        overseer_name = getOverseerName(overseer_id)
        text = [
            title + " I, " + overseer_name + ", WARN YOU NOT",
            "TO MOCK PHAROAH ZOSER.  HIS FLAIL IS",
            "SWIFT.",
        ]
    return text


def outOfTimeText() -> list[str]:
    text = ["YOU HAVE RUN OUT OF TIME, ZOSER WANTS", "YOUR HEAD."]
    return text


def pyramidDoneText() -> list[str]:
    text = [
        "IMHOTEP, YOU HAVE FULFILLED THE WISH",
        "OF PHAROAH.  YOUR REWARD IS THE GREAT",
        "BOON OF BEING ENTOMBED WITH YOUR LORD",
        "AND MASTER, ZOSER, THE GOLDEN HORUS.",
    ]
    return text


def gameStartText1() -> list[str]:
    text = [
        "%sIMHOTEP" % (" " * 17),
        "%sPYRAMID BUILDER" % (" " * 13),
        "",
        "",
        "WRITTEN BY: TERRY CLARK",
        "TRANSLATED TO APPLE BY: M.P. ANTONOVICH",
        "TRANSLATED TO PYTHON BY: C. & C. LARSEN",
        "",
    ]
    return text


def gameStartText2(overseer_id: int) -> list[str]:
    overseer_name = getOverseerName(overseer_id)
    text = [
        "++++A DECREE FROM ZOSER,",
        "    THE GOLDEN HORUS,",
        "    BULL OF KHEM.++++",
        "",
        "TO IMHOTEP, MASTER MASON:",
        "IMHOTEP, THE PHAROAH HAS COMMANDED A",
        "PYRAMID TO BE BUILT.  THE HORUS DESIRES",
        "THIS GLORY TO HIS NAME TO BE FINISHED",
        "WITHIN A PERIOD OF TWELVE YEARS.",
        "YOUR OVERSEER IS " + overseer_name + ".",
        "HE IS TO OBEY YOUR COMMANDS.",
        "",
        "",
    ]
    return text


def pyramidStatusText(years: int) -> list[str]:
    text = ["WORK SITE AFTER " + str(years) + " YEARS"]
    return text


def playAgainPrompt() -> list[str]:
    text = ["IMHOTEP WILL YOU TRY AGAIN? (Y/N) "]
    return text


def drawSamplePyramid():
    x = 20
    s = "*"
    for x in range(20, 15, -1):
        print("%s%s" % (" " * x, s))
        s = "*" + s + "*"
    print("")
    print("")
    return


def drawPyramid(levels: float):
    text = []
    for y in range(int(levels), 0, -1):
        blocks: float = 2 * (21 - y)
        spaces: float = 20 - blocks / 2
        s = "%s%s" % (" " * int(spaces), "*" * int(blocks))
        text.append(s)
    displayText(text)
    return


def clearScreen():
    for i in range(40):
        print("")
    return


def pause(number: float):
    time.sleep(number / 1000.0)
    return


def displayText(text: list[str]):
    for line in text:
        print(line)

    if len(text) > 0 and False:
        print
        time.sleep(1)
    return


def promptUserNumber(prompt: list[str]) -> int:
    number_of_lines = len(prompt)
    for i in range(number_of_lines - 1):
        print(prompt[i])
    value = int(input(prompt[number_of_lines - 1]))
    return value


def promptUserText(prompt: list[str]) -> str:
    number_of_lines = len(prompt)
    for i in range(number_of_lines - 1):
        print(prompt[i])
    value = input(prompt[number_of_lines - 1])
    return value


def pauseForUser():
    _ = input("HIT ENTER KEY TO CONTINUE")
    return


def gameLoop():
    overseer_id: int = random.randrange(len(overseers))
    people: int = 300000
    tels_flooded: int = 2500
    storage: float = 330
    years: int = 0
    workforce: int = 0
    errors: int = 0
    levels: int = 0
    title: str = "IMHOTEP"

    clearScreen()
    drawSamplePyramid()
    text = gameStartText1()
    displayText(text)
    drawSamplePyramid()
    pause(5000)

    clearScreen()
    text = gameStartText2(overseer_id)
    displayText(text)
    pauseForUser()

    clearScreen()

    while years < 12 and levels < 20:
        if years > 0:
            # pyramid status
            text = pyramidStatusText(years)
            displayText(text)
            pause(5000)

        # clear screen
        clearScreen()

        # beginning of year status
        text = yearStartText(people, storage, tels_flooded)
        displayText(text)

        # workforce choice
        ok = False
        while not ok:
            prompt = workforcePrompt()
            workforce = promptUserNumber(prompt)
            status, overseer_id, errors, people = workforceStatus(
                workforce, people, overseer_id, errors
            )
            text = workforceText(overseer_id, title, status)
            displayText(text)
            ok = status == nothing_happened

        # worker_storage choice
        ok = False
        while not ok:
            prompt = workerStoragePrompt(storage)
            worker_storage = promptUserNumber(prompt)
            status, workers_fed, storage, errors = workerStorageStatus(
                worker_storage, storage, errors
            )
            text = workerStorageText(title, status)
            displayText(text)
            ok = status == nothing_happened

        # people_storage choice
        ok = False
        while not ok:
            prompt = peopleStoragePrompt(storage, people)
            people_storage = promptUserNumber(prompt)
            status, people_fed, storage, errors = peopleStorageStatus(
                people_storage, storage, errors
            )
            text = peopleStorageText(title, overseer_id, status)
            displayText(text)
            ok = status == nothing_happened

        # tels to plant
        ok = False
        while not ok:
            prompt = telsToPlantPrompt(tels_flooded)
            tels_to_plant = promptUserNumber(prompt)
            status, errors, overseer_id = telsToPlantStatus(
                tels_to_plant, tels_flooded, storage, people, errors, overseer_id
            )
            text = telsToPlantText(status, title, overseer_id, storage, people)
            displayText(text)
            ok = status == nothing_happened
            if status == mummied:
                # game over man
                break

        if status == mummied:
            # game over man
            break

        # clear screen
        clearScreen()
        line_count = 0
        drawSamplePyramid()

        # feed people
        status, workers_fed, new_people, people, starved_people, errors, people_fed = (
            feedStatus(workers_fed, workforce, people_fed, people, errors)
        )
        text = feedText(status, starved_people)
        displayText(text)
        if status == mass_starvation:
            # game over man
            break

        # handle rebellion
        (
            status,
            errors,
            workforce,
            overseer_id,
            workers_killed,
            workers_starved,
            workers_fed,
        ) = rebellionStatus(workers_fed, workforce, errors, overseer_id)
        text = rebellionText(
            status, workers_fed, workforce, workers_killed, overseer_id, workers_starved
        )
        displayText(text)
        line_count += len(text)

        # handle pyramid collapse
        status, levels, workforce, levels_collapsed, workers_fed = (
            pyramidCollapseStatus(levels, workforce, workers_fed)
        )
        text = pyramidCollapsedText(status, levels_collapsed)
        displayText(text)
        line_count += len(text)

        # handle the harvest - logic only
        (
            harvest_status,
            years,
            storage,
            errors,
            priest_feed,
            tels_flooded,
            harvest_rate,
        ) = harvestStatus(storage, tels_to_plant, errors, levels, years)

        # handle random events
        status, amount, storage, tels_flooded, people = randomEventStatus2(
            storage, tels_flooded, people
        )
        text = randomEventText2(status, amount)
        displayText(text)
        line_count += len(text)

        # handle more random events
        status, people, storage, workforce, dead, amount, escapees, workers_fed = (
            randomEventStatus(people, storage, workforce, workers_fed)
        )
        text = randomEventText(status, dead, amount, escapees)
        displayText(text)
        line_count += len(text)

        # handle the harvest display
        text = harvestText(harvest_status, storage, harvest_rate, priest_feed)
        displayText(text)
        line_count += len(text) - 2

        # handle the people display
        text = populationText(new_people)
        displayText(text)

        # handle end of year stuff
        status, people, levels = yearEndStatus(
            people, workforce, levels, workers_fed, errors
        )
        text = yearEndText(levels, tels_flooded, years, errors, title, line_count)
        displayText(text)
        if status == exile:
            # game over man
            break

        pauseForUser()

        # handle the jubilee
        if years == 6:
            clearScreen()
            drawSamplePyramid()
            status, errors, title = jubileeStatus(levels, people, storage, errors)
            text = jubileeText(status)
            displayText(text)
            pauseForUser()

        clearScreen()
        drawPyramid(levels)

    if levels >= 20:
        text = pyramidDoneText()
        for line in text:
            displayText([line])
            pause(2000)
    elif years >= 12:
        text = outOfTimeText()
        displayText(text)
    else:
        pass

    return


def main():
    done = False
    while not done:
        gameLoop()
        ans = " "
        while ans[0].upper() != "Y" and ans[0].upper() != "N":
            prompt = playAgainPrompt()
            ans = promptUserText(prompt)
            if len(ans) < 1:
                ans = " "

        if ans[0].upper() == "N":
            done = True

    clearScreen()
    return


if __name__ == "__main__":
    main()
