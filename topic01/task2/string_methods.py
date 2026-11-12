text = "   hello, wORLD of pyTHON   "
print("Початковий рядок:", repr(text))

clean = text.strip()
print("strip()     :", repr(clean))
print("capitalize():", clean.capitalize())
print("title()     :", clean.title())
print("upper()     :", clean.upper())
print("lower()     :", clean.lower())
