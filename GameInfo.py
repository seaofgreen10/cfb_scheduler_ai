import datetime


class GameInfo:

    team_1 = ""
    team_2 = ""
    time_str = ""
    global time_obj
    channel = ""

    def __init__(self, t1, t2, tstr, chan):
        print("inside!")
        self.team_1 = t1
        print(self.team_1)
        self.team_2 = t2
        self.time_str = tstr
        self.time_obj = datetime.datetime.strptime(self.time_str, "%H:%M %p")
        self.channel = chan

    def getTeam1(self):
        return self.team_1

    def getTeam2(self):
        return self.team_2

    def getTimeStr(self):
        return self.time_str

    def getTimeObj(self):
        return time_obj

    def getChannel(self):
        return self.channel