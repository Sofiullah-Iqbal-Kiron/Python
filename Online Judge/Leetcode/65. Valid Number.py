# Accepted after
#               928 days or
#               2 years, 6 months, 14 days
#               30 months, 14 days.
#               80,179,200 seconds.

# First submit: 15 May, 2020. 4:36 PM.
# Last submit: 28 Nov, 2022. 9:15 PM.

# Time duration result extracted from: https://www.timeanddate.com/date/durationresult.html?d1=15&m1=5&y1=2020&d2=28&m2=11&y2=2022&ti=on

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        numRex = re.compile(r"[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?")
        return numRex.fullmatch(s)
