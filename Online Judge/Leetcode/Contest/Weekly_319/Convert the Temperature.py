# Accepted using Java during contest.
# Now solved using Python.
# Posted in twitter.

class Solution(object):
    def convertTemperature(self, celsius):
        return [celsius + 273.15, celsius * 1.80 + 32.00]
