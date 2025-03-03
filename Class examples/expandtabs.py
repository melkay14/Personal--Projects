# expand tabs can control the number of horizontal tab stops.

print("012345670123456")
print("a\tb\tc")
print("a\tb\tc".expandtabs(5))
print("Nudge, \tnudge, \nwink, \twink. ".expandtabs(11))

#example
print()
print("Class, \nWork.".expandtabs(11))