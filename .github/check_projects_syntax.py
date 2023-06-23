#!/usr/bin/env python

import yaml
import sys

sandbox = {}
graduated = {}

with open("projects/templates/sandbox.yml") as f:
    sandbox = yaml.safe_load(f)

with open("projects/templates/graduated.yml") as f:
    graduated = yaml.safe_load(f)

# first try to load as sandbox and check status

def fail(msg):
    print(msg)
    sys.exit(1)

def check(filename, data, template):
    for k in template:
        if k not in data:
            fail(f"{filename}: required key {k} missing!")
        elif isinstance(template[k], dict):
            if not isinstance(data[k], dict):
                fail(f"{filename}: key {k} is expected to be a nested dict!")
            check(filename, data[k], template[k])

for filename in sys.argv[1:]:
    try:
        with open(filename) as f:
            data = yaml.safe_load(f)
    except Exception as e:
        fail(f"Unable to parse {filename} as yml: {e}")

    # it needs to match fields from sandbox
    if "status" not in data:
        fail(f"{filename}: Status field missing")

    # status needs to be either sandbox, graduated or archived
    if data["status"] not in ["sandbox", "graduated", "archived"]:
        fail(f"{filename}: invalid status")



    if data["status"] == "sandbox":
        check(filename, data, sandbox)
    elif data["status"] == "graduated":
        check(filename, data, graduated)
