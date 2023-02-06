# Full Stack - Django
## Stacks :
[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org/)


### Steps to configure ubuntu server
- `#psycopg2 error fix`
````
sudo apt-get install libpq-dev
````
- Then run :
````
pip install psycopg2
````
### Setup Postgres on Ubuntu :

`cd /etc/postgresql/<psql_version>/main`

`sudo vim postgresql.conf`

Go to CONNECTIONS AND AUTHENTICATION and uncomment `#listen_addresses = 'localhost'` edit it to `listen_addresses = '*'` , save the file & done!

Now, `sudo vim pg_hba.conf` & edit:

Add above the all host settings: `host<TAB>all<TAB>all<TAB>0.0.0.0/0<TAB>md5` (Use TAB Key for intendation)

Last CMD: `sudo service postgresql restart`

---

### Useful Postgres Commands :
- Open postgres terminal in ubuntu, linux using:
- `sudo su postgres`
- `psql`

`ALTER USER postgres password 'hsjga(*hdjkjs829';`
- https://generate-secret.vercel.app/32 `Generate secret key via this.`
`CREATE USER pld WITH PASSWORD 'hikjh4fgh';` 

`DROP USER pld;`

`CREATE DATABASE database_name;` 

`DROP DATABASE database_name;`

If you wish to delete the database if it exists and otherwise do nothing, include the optional IF EXISTS option:

`DROP DATABASE IF EXISTS some_database;`

`GRANT ALL PRIVILEGES ON DATABASE database_name to pld;` 

`REVOKE ALL PRIVILEGES ON DATABASE database_name FROM pld;`

- `# Quit using the following command:`
`\q `

- `# Connect to a database, lets say database_name using:`
`\c database_name `

- `# List all databases using:`
`\l`

- `# List all database tables:`
`\dt`

- `Create Tables using: `
- 
CREATE TABLE supplies (
    id INT PRIMARY KEY,
    name VARCHAR,
    description VARCHAR,
    manufacturer VARCHAR,
    color VARCHAR,
    inventory int CHECK (inventory > 0)
);

- `#Delete Table using:`
- `DROP TABLE table_name;`
- `DROP TABLE IF EXISTS table_name;`

INSERT Data into the tables using:

`INSERT INTO supplies(id, name, description, manufacturer, color, inventory) VALUES (1, 'grain', 'grain supply from vietnam', 'ITC Vietnam', 'brown', 1000);`

How to log table data using:

`SELECT * FROM supplies;`

Update table data using:

`UPDATE supplies SET color = 'green', inventory = 5000;`

Introduction:
PostgreSQL and other relational database management systems use databases and tables to structure and organize their data. We can review the definition of those two terms quickly:

databases: separate different sets of structures and data from one another
tables: define the data structure and store the actual data values within databases
In PostgreSQL, there is also an intermediary object between databases and tables called schema:

schema: a namespace within a database that contains tables, indexes, views, and other items.
Relationship between PostgreSQL databases, schemas, and tables.

![Database_flow-chart](https://www.prisma.io/dataguide/content/postgresql/creating-and-deleting-databases-and-tables/object-hierarchy.png)
