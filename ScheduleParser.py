from bs4 import BeautifulSoup
import datetime
import urllib.request
import re
import utils
from GameInfo import GameInfo


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
    CONST_TIME_INDEX = 3
    CONST_CHANNEL_INDEX = 5

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
        #print(mix[10])
        #print("mid")
        #print(mix[10].contents[self.CONST_GAME_INDEX])
        #print(mix[10].contents[self.CONST_GAME_INDEX])
        #print(mix[10].contents[self.CONST_GAME_INDEX])
        #print("done")
        listOfGames = self.parseListToGamesInBlock(ScheduleParser, mix)
        print("list of games " + str(listOfGames.__sizeof__()))
        for ctr in listOfGames:
            print( ctr.getTeam1() + " " + ctr.getTeam2() + " " + ctr.getTimeStr() + " " + ctr.getChannel() )

        return mix

    # Input: List of raw <tr> webpage chunks
    # BL: Remove non-game <tr> chunks
    # Output: List of game-only <tr> chunks
    def cleanListToRawGameChunks(self, mix):
        cleanedList = []
        return cleanedList


    def parseListToGamesInBlock(self, mix):
        teams_ls = []
        time = ""
        chan = ""
        listOfGames = []

        for item in mix:
            string_comp = str(item)
            string_comp = string_comp.replace(u'\xa0', ' ')
            validGame = 0

            if "Week " in string_comp:
                print("Week")
            elif " vs. " in string_comp:
                teams_ls = re.split(' (vs). ', string_comp)
                #print("VS: " + string_comp)
                #teams_ls[2] = teams_ls[2].split('(')[0]
                #print("t1: " + teams_ls[0] + " t2: " + teams_ls[2])
                validGame = 0
            elif (" at " in string_comp) and (not "Updated" in string_comp):
                tagless_team_line = utils.remove_tags(str(item.contents[self.CONST_GAME_INDEX]))

                teams_ls = re.split(' (at) ', tagless_team_line)
                #print("AT: " )
                #print("AT CONTENTS: " + str(item.contents[1]))
                #print("t0 " + teams_ls[0] + " t1: " + teams_ls[1]+ " t2: " + teams_ls[2])

                # Time
                tagless_time_line = utils.remove_tags(str(item.contents[self.CONST_TIME_INDEX]))
                time = tagless_time_line
                #print("Time: " + time)

                # Channel
                tagless_chan_line = utils.remove_tags(str(item.contents[self.CONST_CHANNEL_INDEX]))
                chan = tagless_chan_line
                #print("Chan: " + chan)

                validGame = 1
            else:
                print("Error?")
                #print("Possible error parsing game: " + string_comp)

            if validGame:
                temp_game_info = GameInfo(teams_ls[0], teams_ls[2], time, chan)
                print("Adding GI: " + teams_ls[0] + " " + teams_ls[2] + " " + time + " " + chan)
                print("Added: " + temp_game_info.getTeam1() + " " + temp_game_info.getTeam2() + " " + temp_game_info.getTimeStr() + " " + temp_game_info.getChannel())
                listOfGames.append(GameInfo(teams_ls[0], teams_ls[2], time, chan))

        return listOfGames

ScheduleParser.parseToList(ScheduleParser)
print("here")