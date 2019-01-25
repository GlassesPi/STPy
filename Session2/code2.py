m = int(input())
d = int(input())
days = ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]

if m <= 7:
    s = (m - 1) * 31 + d
else:
    #s = 6 * 31 + (m - 7) * 30 + d
    s = (m - 1) * 30 + d + 6

print(days[s % 7])

