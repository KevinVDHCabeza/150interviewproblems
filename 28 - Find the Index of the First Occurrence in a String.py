haystack = "sadbutsad"
needle = "saad"

try:
    value=haystack.index(needle)
except ValueError:
    value=-1



print(value)