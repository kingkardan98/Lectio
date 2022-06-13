# LECTIO - Manage Lessons, Payments and more!

Lectio is a Python program that manages a database (using PostgreSQL) to create, manage and extrapolate information about your private lessons.

## Necessary tools

[PostgreSQL](https://www.postgresql.org/download/): the relational database used in this project, needed for use.

[Python](https://www.python.org/downloads/): written using Python 3.10.4

## First steps

If you wish to use this program, be sure to create a file named 'database.ini' and put it in the same folder as all the other files. A template is given in this repo. The file should look like this:

		[postgresql]
		host = hostName
		database = databaseName
		user = postgresUser
		password = postgresPassword

If you use a local installation of PostgreSQL, set *hostName* to *localhost*.

*postgresUser* and *postgresPassword* are the credentials PostgreSQL made you create on installation. Default username is *postgres*.