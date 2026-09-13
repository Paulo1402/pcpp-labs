from theclicker.clicker import TheClicker, GameMode

if __name__ == "__main__":
    game_mode = GameMode.time_bound
    options = {
        "MAX_NUMBER": 100,
        "WRONG_CLICK_PENALTY": 10,
        "TIME_BOUND_IN_SECONDS": 100,
    }

    app = TheClicker(game_mode, **options)
    app.run()
