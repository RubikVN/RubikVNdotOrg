from apps.results.models.wca.event import FORMAT_TIME, FORMAT_MULTI, FORMAT_NUMBER

class ResultFormatter():
    def __init__(self, iterable, key_name, eventid, category="single"):
        self.iterable = iterable
        self.key_name = key_name
        self.eventid = eventid
        self.category = category
        self.actions = [
            (FORMAT_TIME, self.__format_wca_time),
            (FORMAT_MULTI, self.__format_wca_multi),
            (FORMAT_NUMBER, self.__format_wca_number)
        ]

    def __format(self):
        pass

    def format(self):
        try:
            for official_events, action in self.actions:
                if self.eventid in official_events:
                    self.__format = action
                    return self.__format()
        except Error:
            return None

    def __format_wca_time(self):
        for time in self.iterable:
            seconds = time[self.key_name] / 100
            if seconds >= 60:
                time[self.key_name] = f"{int(seconds/60):02d}:{seconds%60:05.2f}"
            else:
                time[self.key_name] = f"{seconds:.2f}"
        return self.iterable

    def __format_wca_multi(self):
        for time in self.iterable:
            # Decoding WCA notations
            res = time[self.key_name]
            DD = res // 10000000
            TTTTT = (res // 100) % 100000
            MM = res % 100

            difference = 99 - DD
            seconds = TTTTT
            solved = difference + MM
            attempted = solved + MM

            if seconds == 3600:
                time[self.key_name] = f"{solved}/{attempted} 1:00:00"
            else:
                time[self.key_name] = f"{solved}/{attempted} {int(seconds/60):02d}:{seconds%60:02d}"
        return self.iterable

    def __format_wca_number(self):
        if self.category == "single":
            return self.iterable
        else:
            for num in self.iterable:
                num[self.key_name] = f"{num[self.key_name]/100:05.2f}"
            return self.iterable
