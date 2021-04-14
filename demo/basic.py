from datetime import date, timedelta

class DateInformation:
    def __init__(self, date: date):
        self.__date = date

    def __get_christmas(self, year: int) -> date:
        return date(year, 12, 25)

    def days_until_christmas(self) -> int:
        current_year = self.__date.year
        xmas_day_this_year = self.__get_christmas(current_year)
        
        xmas_day_delta = (xmas_day_this_year - self.__date).days
        if xmas_day_delta >= 0:
            return xmas_day_delta
        else:
            xmas_day_next_year = self.__get_christmas(current_year + 1)
            return (xmas_day_next_year - self.__date).days


    def get_season(self, hemisphere: str="south") -> str:
        northern_seasons = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}
        southern_seasons = {1: "Summer", 2: "Autumn", 3: "Winter", 4: "Spring"}

        month_number = self.__date.month
        season_number = 0
        if month_number == 12 or month_number < 3:
            season_number = 1
        elif month_number >= 3 and month_number < 6:
            season_number = 2
        elif month_number >= 6 and month_number < 9:
            season_number = 3
        else:
            season_number = 4

        if hemisphere == "south":
            return southern_seasons.get(season_number)
        elif hemisphere == "north":
            return northern_seasons.get(season_number)