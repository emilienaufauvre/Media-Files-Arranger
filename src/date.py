from __future__ import annotations

import datetime


class Date:
    """
    A date and time representation of a moment. Can use different
    attribute to describe the moment:
    - year
    - month
    - day
    - hour
    - minute
    - second
    - deci-second
    - centi-second
    - milli-second
    - ten-milli-second
    - hundred-milli-second
    - micro-second.
    """

    def __init__(self,
                 year: int = None,
                 month: int = None,
                 day: int = None,
                 hour: int = None,
                 minute: int = None,
                 second: int = None,
                 decis: int = None,
                 centis: int = None,
                 millis: int = None,
                 ten_millis: int = None,
                 hun_millis: int = None,
                 micros: int = None) -> None:
        Date.__check_args(year,
                          month,
                          day,
                          hour,
                          minute,
                          second,
                          decis,
                          centis,
                          millis,
                          ten_millis,
                          hun_millis,
                          micros)
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__decis = decis
        self.__centis = centis
        self.__millis = millis
        self.__ten_millis = ten_millis
        self.__hun_millis = hun_millis
        self.__micros = micros

    @staticmethod
    def create_from_decimals(year: int = None,
                             month: int = None,
                             day: int = None,
                             hour: int = None,
                             minute: int = None,
                             second: int = None,
                             decimals: int = None) -> Date:
        decimals = "%06d" % decimals
        return Date(year,
                    month,
                    day,
                    hour,
                    minute,
                    second,
                    *[int(d) for d in decimals])

    @staticmethod
    def create_from_datetime(t: datetime.datetime) -> Date:
        return Date.create_from_decimals(year=t.year,
                                         month=t.month,
                                         day=t.day,
                                         hour=t.hour,
                                         minute=t.minute,
                                         decimals=t.microsecond)

    @staticmethod
    def __check_args(year: int | None,
                     month: int | None,
                     day: int | None,
                     hour: int | None,
                     minute: int | None,
                     second: int | None,
                     decis: int | None,
                     centis: int | None,
                     millis: int | None,
                     ten_millis: int | None,
                     hun_millis: int | None,
                     micros: int | None) -> None:

        if not year and \
                not month and \
                not day and \
                not hour and \
                not minute and \
                not second and \
                not decis and \
                not centis and \
                not millis and \
                not ten_millis and \
                not hun_millis and \
                not micros:
            raise ValueError("No value given; can't create empty date.")

        if year and not (1800 <= year <= 2999):
            raise ValueError("Invalid year (must be in [1800, 2999]).")
        if month and not (1 <= month <= 12):
            raise ValueError("Invalid month (must be in [1, 12]).")
        if day and not (1 <= day <= 31):
            raise ValueError("Invalid day (must be in [1, 31]).")
        if hour and not (0 <= hour <= 23):
            raise ValueError("Invalid hour (must be in [0, 23]).")
        if minute and not (0 <= minute <= 59):
            raise ValueError("Invalid minute (must be in [0, 59]).")
        if second and not (0 <= second <= 59):
            raise ValueError("Invalid second (must be in [0, 59]).")
        if decis and not (0 <= decis <= 9):
            raise ValueError("Invalid deci-second (must be in [0, 9]).")
        if centis and not (0 <= decis <= 9):
            raise ValueError("Invalid centi-second (must be in [0, 9]).")
        if millis and not (0 <= decis <= 9):
            raise ValueError("Invalid milli-second (must be in [0, 9]).")
        if ten_millis and not (0 <= decis <= 9):
            raise ValueError("Invalid ten-milli-second (must be in [0, 9]).")
        if hun_millis and not (0 <= decis <= 9):
            raise ValueError("Invalid hundred-milli-second (must be in [0, "
                             "9]).")
        if micros and not (0 <= decis <= 9):
            raise ValueError("Invalid micro-second (must be in [0, "
                             "9]).")

    def to_micros(self) -> float:
        return (self.__year if self.__year else 0)* 3.1536e13 + \
            (self.__month if self.__month else 0) * 2.628288e12 + \
            (self.__day if self.__day else 0) * 8.64e10 + \
            (self.__hour if self.__hour else 0) * 3.6e9 + \
            (self.__minute if self.__minute else 0) * 6e7 + \
            (self.__second if self.__second else 0) * 1e6 + \
            (self.__decis if self.__decis else 0) * 1e5 + \
            (self.__centis if self.__centis else 0) * 1e4 + \
            (self.__millis if self.__millis else 0) * 1e3 + \
            (self.__ten_millis if self.__ten_millis else 0) * 1e2 + \
            (self.__hun_millis if self.__hun_millis else 0) * 1e1 + \
            (self.__micros if self.__micros else 0) * 1e0

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def get_decis(self):
        return self.__decis

    def get_centis(self):
        return self.__centis

    def get_millis(self):
        return self.__millis

    def get_ten_millis(self):
        return self.__ten_millis

    def get_hun_millis(self):
        return self.__hun_millis

    def get_micros(self):
        return self.__micros

    def __str__(self) -> str:
        # Format "YYYYmmdd_HHMMSS_DCITHF".
        return "%04d%02d%02d_%02d%02d%02d_%d%d%d%d%d%d" % (
            self.__year if self.__year else 0,
            self.__month if self.__month else 0,
            self.__day if self.__day else 0,
            self.__hour if self.__hour else 0,
            self.__minute if self.__minute else 0,
            self.__second if self.__second else 0,
            self.__decis if self.__decis else 0,
            self.__centis if self.__centis else 0,
            self.__millis if self.__millis else 0,
            self.__ten_millis if self.__ten_millis else 0,
            self.__hun_millis if self.__hun_millis else 0,
            self.__micros if self.__micros else 0,
        )

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented

        return self.__year == other.get_year() and \
            self.__month == other.get_month() and \
            self.__day == other.get_day() and \
            self.__hour == other.get_hour() and \
            self.__minute == other.get_minute() and \
            self.__second == other.get_second() and \
            self.__decis == other.get_decis() and \
            self.__centis == other.get_centis() and \
            self.__millis == other.get_millis() and \
            self.__ten_millis == other.get_ten_millis() and \
            self.__hun_millis == other.get_hun_millis() and \
            self.__micros == other.get_micros()

    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.to_micros() < other.to_micros()


DATE_MAX = Date.create_from_decimals(year=2999,
                                     month=12,
                                     day=31,
                                     hour=23,
                                     minute=59,
                                     second=59,
                                     decimals=999999)

DATE_MIN = Date.create_from_decimals(year=1800,
                                     month=1,
                                     day=1,
                                     hour=00,
                                     minute=0,
                                     second=0,
                                     decimals=0)
