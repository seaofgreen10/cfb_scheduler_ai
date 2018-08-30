from bs4 import BeautifulSoup
import datetime
import urllib.request
import re

print("here")


class GameInfo:

    global team_1
    global team_2
    global time_str
    global time_obj
    global channel

    def __init__(self, t1, t2, tstr, chan):
        team_1 = t1
        team_2 = t2
        time_str = tstr
        time_obj = datetime.datetime.strptime(time_str, "%H:%M%p")
        channel = chan

    def getTeam1(self):
        return team_1


class TimeBlock:

    gameInfoList = []

    def __init__(self, list):
        self.gameInfoList = list

    def __init__(self):
        self.gameInfoList = []

    def addGameInfo(self, gameInfo):
        self.gameInfoList.append(gameInfo)

    def addGameInfo(self, t1, t2, tstr, chan):
        gameInfo = GameInfo(t1, t2, tstr, chan)
        self.gameInfoList.append(gameInfo)


class ScheduleParser:

    CONST_GAME_INDEX = 1
    CONST_TIME_INDEX = 2
    CONST_CHANNEL_INDEX = 3

    # Scrape webpage and find all <tr>
    def parseToList(self):
        print("inside")
        #webpage = "http://www.fbschedules.com/college-football-schedule/"
        webpage = "http://www.lsufootball.net/tvschedule-directv.htm"
        websource = urllib.request.urlopen(webpage)
        soup = BeautifulSoup(websource.read(), "html.parser")

        #print("inside2")
        #span = soup.find_all("td",  "matchup")
        #print(span)
        #week = soup.find_all("div", "bowl-bg")

        #mix = soup.find_all(["tr", "div"], ["matchup", "bowl-bg"])
        mix = soup.find_all("tr")
        print("start")
        #print(mix)
        print(mix[10])
        print("mid")
        print(mix[10].contents[self.CONST_GAME_INDEX])
        print(mix[10].contents[self.CONST_GAME_INDEX])
        print(mix[10].contents[self.CONST_GAME_INDEX])
        print("done")
        return mix

    # Input: List of raw <tr> webpage chunks
    # BL: Remove non-game <tr> chunks
    # Output: List of game-only <tr> chunks
    def cleanListToRawGameChunks(self, mix):
        cleanedList = []
        return cleanedList


    def parseListToGamesInBlock(self, mix):
        teams_ls = []
        stopOnNext = 0
        for item in mix:
            print(type(item))
            string_comp = str(item)
            string_comp = string_comp.replace(u'\xa0', ' ')
            validGame = 0

            if "Week " in string_comp:
                if stopOnNext:
                    print("breaking")
                    break
                print("Setting stopOnNext")
                stopOnNext = 1
            elif " vs. " in string_comp:
                teams_ls = re.split(' (vs). ', string_comp)
                teams_ls[2] = teams_ls[2].split('(')[0]
                print("t1: " + teams_ls[0] + " t2: " + teams_ls[2])
                validGame = 1
            elif " at " in string_comp:
                teams_ls = re.split(' (at) ', string_comp)
                print("t1: " + teams_ls[0] + " t2s: " + teams_ls[2])
                validGame = 1
            else:
                stopOnNext = 0
                print("Possible error parsing game: ")

            time_str = ""
            chan = ""

            if validGame:
                temp_game_info = GameInfo(teams_ls[0], teams_ls[2], time_str, chan)


ScheduleParser.parseToList(ScheduleParser)
print("here")