#!/usr/bin/env bash -e

# the -z switch will test if the expansion of "$1" is a null string or not
if [ -z "$1" ]
then
  echo "Usage: ./generate_migration <migration_name>"
  exit 1
fi


timestamp() {
  date +"%Y%m%d%H%M%S"
}

file_prefix=$(timestamp)
name=$1

touch "sql/V${file_prefix}__$1.sql"
