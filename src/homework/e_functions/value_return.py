
   
def get_seconds():

    time = int(input("Input time in seconds: "))
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    clock = ("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

    print (seconds)


def get_minutes():

    time = int(input("Input time in seconds: "))
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    clock = ("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

    print (minutes)


def get_hour():

    time = int(input("Input time in seconds: "))
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    clock = ("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

    print (hour)


def get_time():

    time = int(input("Input time in seconds: "))
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    clock = ("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

    print(clock)

