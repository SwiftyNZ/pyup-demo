@basic
Feature: Basic Date Information Demo

    Scenario: Get days until Christmas day
        Given the date is <date>
        Then the number of days until christmas is <days>

        Examples:
            | date          | days  |
            | 25-12-2021    | 0     |
            | 26-12-2021    | 364   |
            | 12-02-2020    | 317   |
            | 24-12-2020    | 1     |
            | 31-05-2021    | 208   |

    Scenario: Get season
        Given the date is <date> 
        And hemisphere is <hemisphere>
        Then the season is <season>

        Examples:
            | date          | hemisphere | season |
            | 25-12-2021    | north      | Winter |
            | 01-07-2021    | north      | Summer |
            | 01-09-2020    | north      | Autumn |
            | 31-05-2020    | north      | Spring |
            | 01-01-2021    | south      | Summer |
            | 17-03-1990    | south      | Autumn |
            | 02-06-1983    | south      | Winter |
            | 23-10-2001    | south      | Spring |
