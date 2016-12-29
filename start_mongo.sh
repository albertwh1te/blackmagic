#!/usr/bin/env bash
# set -euo pipefail
IFS=$'\n\t'

mongod --fork --logpath ~/mongolog --dbpath=~/db
