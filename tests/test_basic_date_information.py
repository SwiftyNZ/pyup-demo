from pytest_bdd import scenarios, given, when, then
from demo.basic import DateInformation
from datetime import datetime

scenarios("./features/basic_date_information.feature", example_converters={"days": int})

DATE_FORMAT = "%d-%m-%Y"

@given("the date is <date>", target_fixture="instantiate_date_class")
def instantiate_date_class(date):
    date_type = datetime.strptime(date, DATE_FORMAT).date()
    return DateInformation(date_type)

@then("the number of days until christmas is <days>")
def valid_christmas_calculation(instantiate_date_class, days):
    assert instantiate_date_class.days_until_christmas() == days

@given("hemisphere is <hemisphere>", target_fixture="get_hemisphere")
def get_hemisphere(hemisphere):
    return hemisphere

@then("the season is <season>")
def validate_season(instantiate_date_class, get_hemisphere, season):
    season_to_validate = instantiate_date_class.get_season(get_hemisphere)
    assert season_to_validate == season