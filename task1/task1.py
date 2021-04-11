import re


class Error(Exception):
    """Base exception"""
    pass


class ValueCannotBeConvertedError(Error):
    """Raised when a value cannot be converted to seconds"""
    def __init__(self, message="Cannot convert value to seconds"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class Converter:
    """
    """

    def __init__(self):
        self.t_units = {'s': 1, 'S': 1,
                        'm': 60, 'M': 60,
                        'h': 3600, 'H': 3600,
                        'd': 86400, 'D': 86400}
        self.default_t_unit = "s"
        self.default_unit = self.t_units[self.default_t_unit]

    def to_seconds(self, s):
        num = rf"(?:[\d\.\d]+|\d+)"
        unit = rf"(?:[sSmMhHdD])"
        m = re.match(rf"(?:{num}|{unit}|{num}{unit})$", s)
        if m:
            a = re.match(rf"(?:{num})", s)
            amount = float(a[0]) if a else self.default_unit
            t_unit = self.t_units[s[-1]] if s[-1] in self.t_units else self.default_unit
            return int(amount * t_unit)
        else:
            raise ValueCannotBeConvertedError


if __name__ == "__main__":
    cvt = Converter()
    for i in arr:
        try:
            print(cvt.to_seconds(i))
        except Exception as e:
            print(e)
