with open("aircraft.xml", "r") as f:
    lines = f.readlines()

with open("flights_fragment.xml", "r") as f:
    flights = f.read()

# Find the last </data> tag
for i in range(len(lines) - 1, -1, -1):
    if "</data>" in lines[i]:
        lines.insert(i, "\n    <!-- Generated Flight Events -->\n" + flights + "\n")
        break

with open("aircraft.xml", "w") as f:
    f.writelines(lines)

print("Successfully merged flights into aircraft.xml")
