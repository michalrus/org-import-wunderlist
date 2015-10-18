#!/usr/bin/python

import json
import sys
from datetime import datetime
from pprint import pprint

def dateconv(d):
    return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %a %H:%M")

def printtask(task, lev):
    print("%s %s %s" % (
        lev,
        ("DONE" if task["completed"] else "TODO"),
        task["title"]
    ))
    print("CREATED: [%s]" % dateconv(task["created_at"]))
    if (task["completed"]):
        print("CLOSED: [%s]" % dateconv(task["completed_at"]))

with open(sys.argv[1]) as data_f:
    data = json.load(data_f)

print("* Wunderlist")
print("EXPORTED: [%s]" % datetime.strptime(data["exported"], "%a %b %d %Y %H:%M:%S GMT%z (%Z)").strftime("%Y-%m-%d %a %H:%M"))

data = data["data"]
for wlist in data["lists"]:
    print("** %s" % wlist["title"])
    print("CREATED: [%s]" % dateconv(wlist["created_at"]))
    for task in (task for task in data["tasks"] if task["list_id"] == wlist["id"]):
        printtask(task, "***")
        for note in (note for note in data["notes"] if note["task_id"] == task["id"] and note["content"]):
            print(note["content"])
        for subtask in (subtask for subtask in data["subtasks"] if subtask["task_id"] == task["id"]):
            printtask(subtask, "****")
