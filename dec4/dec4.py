#!/usr/bin/python

# TODO: cleanup this pathetic mess of code

from re import search
from datetime import datetime, timedelta

DATE_FORMAT = "{0.month:02d}-{0.day:02d}"

#with open("sample.txt") as f:
with open("input.txt") as f:
    logLines = f.readlines()

logs = []
schedule = {}
for logLine in logLines:
    timestamp = datetime.strptime(logLine[:18], "[%Y-%m-%d %H:%M]")
    message = logLine[19:].rstrip()

    matchGuard = search("#(\d+)", logLine)
    if matchGuard:
        guard = matchGuard.groups()[0]
        if timestamp.hour != 0:
            timestamp = timestamp + timedelta(days=1)
        schedule[DATE_FORMAT.format(timestamp)] = {"guard": guard, "minutes": []}
    else:
        logs.append({
            "date": timestamp,
            "message": message,
        })
sortedLogs = sorted(logs, key=lambda x: x["date"])

# Calculate minutes per day and add it to the schedule
from itertools import groupby
for key, value in groupby(sortedLogs, lambda x: DATE_FORMAT.format(x["date"])):
    value = list(value)
    minutes = [0] * 60

    index = 0
    while index < len(value):
        for i in range(value[index]["date"].minute, value[index+1]["date"].minute):
            minutes[i] = 1
        index += 2

    schedule[key]["minutes"] = minutes

# Get the amount of sleep minutes per minute per guard
guardTimes = {}
for guard, values in groupby(schedule.values(), lambda x: x["guard"]):
    values = list(values)
    for index, value in enumerate(values):
        if guard not in guardTimes:
            guardTimes[guard] = [0] * 60
        for minindex, minute in enumerate(value["minutes"]):
            guardTimes[guard][minindex] += minute

# PART 1
guardTotalTimes = ([(g, sum(m)) for g, m in guardTimes.items()])
guardMostTimes = sorted(guardTotalTimes, key=lambda x: x[1])[-1][0]
guardMostTimesTopMinute = guardTimes[guardMostTimes]
topMinuteCount = max(guardMostTimesTopMinute)
topMinute = guardMostTimesTopMinute.index(topMinuteCount)
print(int(guardMostTimes) * topMinute)

# PART 2
guardsMaxMinutes = []
for guard, minutes in guardTimes.items():
   maxMinuteValue = max(minutes)
   maxMinuteKey = minutes.index(maxMinuteValue)
   guardsMaxMinutes.append((guard, maxMinuteKey, maxMinuteValue))

mostMinGuard = sorted(guardsMaxMinutes, key=lambda x: x[2])[-1]
print(int(mostMinGuard[0]) * mostMinGuard[1])
