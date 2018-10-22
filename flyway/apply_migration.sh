#!/usr/bin/env bash -e

# the -z switch will test if the expansion of "$1" is a null string or not
if [ -z "$1" ]
then
  echo "Usage: ./apply_migration <environment>"
  exit 1
fi

flyway -configFiles=flyway_${1}.properties migrate
