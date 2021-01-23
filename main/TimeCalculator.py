class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.valid = True
        try:
            self.hour = int(self.hour)
            self.minute = int(self.minute)
            self.second = int(self.second)
        except ValueError:
            self.valid = False

    def get(self):
        if self.valid:
            return f'{self.hour}:{self.minute}:{self.second}'
        else:
            return 'Erro -\nNúmero digitado inválido!'

    def add(self, hour, minute, second):
        try:
            hour = int(hour)
            minute = int(minute)
            second = int(second)
            self.second += second
            self.minute += minute
            self.hour += hour
            if self.second >= 60:
                self.minute += self.second // 60
                self.second %= 60
            if self.minute >= 60:
                self.hour += self.minute // 60
                self.minute %= 60
        except ValueError:
            self.valid = False

    def sub(self, hour, minute, second):
        try:
            hour = int(hour)
            minute = int(minute)
            second = int(second)
            self.second -= second
            self.minute -= minute
            self.hour -= hour
            if self.second < 0:
                self.minute += self.second // 60
                self.second %= 60
            if self.minute < 0:
                self.hour += self.minute // 60
                self.minute %= 60
            if self.hour < 0:
                raise ValueError
            if self.second >= 60:
                self.minute += self.second // 60
                self.second %= 60
            if self.minute >= 60:
                self.hour += self.minute // 60
                self.minute %= 60
        except ValueError:
            self.valid = False
