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
        southern_seasons = {0: "Spring", 1: "Winter", 2: "Autumn", 3: "Summer"}
        northern_seasons = {0: "Autumn", 1: "Summer", 2: "Spring", 3: "Winter"}
        season_modulus = (self.__date.month + 2) % 4

        if hemisphere == "south":
            return southern_seasons.get(season_modulus)
        elif hemisphere == "north":
            return northern_seasons.get(season_modulus)
