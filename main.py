def timer(minute, second):
    """
    """

    timer_set = (minute * 60) + second

    tick_tock = [
        "Timer started.",
        "Time's up."
    ]

    for i in range(2):
        print(tick_tock[i])
        time.sleep(int(timer_set))
