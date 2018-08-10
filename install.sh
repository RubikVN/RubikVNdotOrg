#!/bin/bash

# Install & set up virtualenv and project dependencies
first_time_install ()
{
  echo "Installing and setting up virtualenv..."
  sudo apt install python3.6-dev, libmysqlclient-dev, pv
  sudo python3.6 -m pip install virtualenv
}

initialize ()
{
  virtualenv rbvn-env/ -p python3.6
  source rbvn-env/bin/activate
  pip install -r requirements.txt
}

db_setup ()
{
  echo -n "Your root user password for MySQL: "
  read -s MYSQL_PASSWORD
  echo

  # Create mysql database named wca
  echo "Importing the database export..."
  echo "CREATE DATABASE IF NOT EXISTS wca; CREATE DATABASE IF NOT EXISTS rubikvn;" | mysql -u root --password=$MYSQL_PASSWORD

  # Create the database schema
  echo "Making migrations for Django project"
  python3.6 manage.py makemigrations
  python3.6 manage.py migrate

  # Download & import WCA database
  echo "Downloading WCA database export..."
  cd RubikVNdotOrg/db/
  if [ -e WCA_export.sql ]
  then
    rm WCA_export.sql
  fi
  wget -q --show-progress https://www.worldcubeassociation.org/results/misc/WCA_export.sql.zip
  unzip WCA_export.sql.zip

  # Removing unnecessary files
  rm README.txt
  rm WCA_export.sql.zip

  pv WCA_export.sql | cat | mysql -u root --password=$MYSQL_PASSWORD wca

  # Extract from the database with our needed records
  echo "Reading from database wca and creating new database rubikvn..."
  pv vn_db_export.sql | cat | mysql -u root --password=$MYSQL_PASSWORD

  echo "-------------------------------"
  echo "Done setting up MySQL database."
}

finish ()
{
  # Escape virtualenv
  deactivate
  echo "Finished installation. You can now run the server using 'python3.6 manage.py runserver'."
}

usage ()
{
  echo "USAGE: ./install.sh [-u]"
  echo "    ./install.sh        For first time installation"
  echo "    ./install.sh -u     From second time installation, tell the script to update the database only"
}

# main script
# Parsing arguments using getopts
if [ $# -eq 0 ]
then
  first_time_install
  initialize
  db_setup
  finish
else
  while getopts ":u" opt; do
    case ${opt} in
      u )
        db_setup
        ;;
      \?)
        usage
        ;;
    esac
  done
fi
