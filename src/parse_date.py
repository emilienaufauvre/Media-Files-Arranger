import enum
import re
from itertools import groupby

from src.date import Date


class DateSubPatterns(enum.Enum):
    """
    Sub-patterns to be used to claim a specific :func:`date.Date` information.
    """
    YEAR = "YYYY"
    MONTH = "mm"
    DAY = "dd"
    HOUR = "HH"
    MINUTE = "MM"
    SECOND = "SS"
    DECIS = "D"
    CENTIS = "C"
    MILLIS = "I"
    TEN_MILLIS = "T"
    HUN_MILLIS = "H"
    MICROS = "F"


class DateRegexes(enum.Enum):
    """
    Regexes to be used to find a specific :func:`date.Date` information.
    """
    YEAR = r"(18[0-9]{2}|19[0-9]{2}|2[0-9]{3})"  # 1800 to 2999.
    MONTH = r"(1[0-2]|0[1-9])"
    DAY = r"(3[01]|[12][0-9]|0[1-9])"
    HOUR = r"([01][0-9]|2[0-3])"
    MINUTE = r"([0-5][0-9])"
    SECOND = r"([0-5][0-9]{1})"
    DECIS = r"([0-9])"
    CENTIS = r"(([0-9]))"
    MILLIS = r"([0-9]){1}"
    TEN_MILLIS = r"(([0-9])){1}"
    HUN_MILLIS = r"([0-9]){01}"
    MICROS = r"(([0-9])){01}"


class DateParser:
    """
    Parse a date in a string using a given pattern made of multiple
    :func:`parse_date.DateSubPatterns`.
    """

    # Matches between a Date sub-pattern and it's regex.
    __MATCHES = { p: r for (p, r) in zip(DateSubPatterns, DateRegexes) }
    # Separators that can be found between each Date sub-pattern (e.g
    # "_" in "2023_02_26" of pattern "YYYYmmdd").
    __REGEX_SEP = r"[.,;/\-_|]?"

    @staticmethod
    def parse(pattern: str, string: str) -> Date | None:
        """
        Parse a date in the given string, using the given pattern.
        A date is found is :param:`string` contains a date that matches
        :param:`pattern`.

        :param pattern: A string made of :func:`parse_date.DateSubPatterns`
            values.
        :param string: A string that mays match :param:`pattern`.
        :return: A :func:`date.Date` object if a date is found, otherwise None.
        """
        # Build the regex used to parse using the pattern.
        regex = DateParser.__build_regex(pattern)
        # Search for a match in the string.
        match = re.search(regex, string)
        # If a match is found:
        if match:
            # Filter separator characters in string.
            string = "".join(filter(str.isdigit, match.string))
            # Extract a Date from filtered string.
            return DateParser.__extract_date(pattern, string)
        # No match.
        return None

    @staticmethod
    def __build_regex(pattern: str) -> str:
        regex = ""
        # For each sub-pattern (e.g YYYY, MM, etc.):
        for _, p in groupby(pattern):
            p = "".join(p)
            # Find the regex associated to this sub-pattern.
            regex += DateParser.__MATCHES[DateSubPatterns(p)].value
            # Add a separator between each sub-pattern regex (i.e. -, _, etc.).
            regex += DateParser.__REGEX_SEP
        # Return the full regex.
        return regex

    @staticmethod
    def __extract_date(pattern: str, string: str) -> Date:
        date = { }
        subpattern = ""
        subpattern_value = ""

        # Parse the value of each sub-pattern (i.e YYYY, MM, etc.):
        for i, (p, c) in enumerate(zip(pattern, string)):
            # If we are going to parse a new sub-pattern, save the previously
            # parsed one.
            if subpattern and p != subpattern[-1]:
                date[DateSubPatterns(subpattern)] = int(subpattern_value)
                subpattern = ""
                subpattern_value = ""

            subpattern += p
            subpattern_value += c
            # If we are at the end of the string to parse, save the last parsed
            # sub-pattern.
            if i == len(pattern) - 1:
                date[DateSubPatterns(subpattern)] = int(subpattern_value)

        # Return a Date object.
        return Date(*(date.get(p) for p in DateSubPatterns))


_DATE_FORMATS = [
    # /!\ Be aware that these patterns are tested in the order defined bellow.
    # For example, since pattern "mmYYYY" is included in "ddmmYYYY", it
    # should be defined after in the following list.
    "YYYYmmddHHMMSSDCITHF",
    "FHTICDSSMMHHddmmYYYY",
    "YYYYmmddHHMMSSDCITH",
    "HTICDSSMMHHddmmYYYY",
    "YYYYmmddHHMMSSDCIT",
    "TICDSSMMHHddmmYYYY",
    "YYYYmmddHHMMSSDCI",
    "ICDSSMMHHddmmYYYY",
    "YYYYmmddHHMMSSDC",
    "CDSSMMHHddmmYYYY",
    "YYYYmmddHHMMSSD",
    "DSSMMHHddmmYYYY",
    "SSMMHHddmmYYYY",
    "YYYYmmddHHMMSS",
    "MMHHddmmYYYY",
    "YYYYmmddHHMM",
    "HHddmmYYYY",
    "YYYYmmddHH",
    "ddmmYYYY",
    "YYYYmmdd",
    "mmYYYY",
    "YYYYmm",
    "YYYY",
    "YYYY",
]


def parse_date(string: str) -> Date | None:
    """
    Parse a date in the given string.

    :param string: A string that mays contain a date.
    :return: A :func:`date.Date` object if a date is found, otherwise None.
    """
    for format_ in _DATE_FORMATS:
        match = DateParser.parse(format_, string)
        if match:
            return match
    return None
