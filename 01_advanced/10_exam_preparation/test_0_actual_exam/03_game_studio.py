# We create our function and give her its parameters
def sort_games(*args, **kwargs):
    console_games = {}
    pc_games = {}

    # We sort the games in two dicts by the games platform
    for platform, game in args:
        if platform == "console":
            console_games[game] = None
        else:
            pc_games[game] = None

    for release_date, name in kwargs.items():
        if name in console_games:
            console_games[name] = release_date
        if name in pc_games:
            pc_games[name] = release_date

    # We sort by release date
    sorted_console_games = sorted(console_games.items(), key=lambda x: x[1])
    sorted_pc_games = sorted(pc_games.items(), key=lambda x: x[1], reverse=True)

    # Writing the final result
    result = ""
    if console_games:
        result += "Console Games:\n"
        for name, release_date in sorted_console_games:
            result += f">>>{release_date[:-4]}: {name}\n"

    if pc_games:
        result += "PC Games:\n"
        for name, release_date in sorted_pc_games:
            result += f"<<<{release_date[:-4]}: {name}\n"

    return result


print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))
print("===========================")
print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))

print("===========================")
print(sort_games(
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("console", "Blade Echo"),
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
))

print("===========================")
print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))

print("===========================")