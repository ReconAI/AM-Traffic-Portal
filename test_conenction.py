import psycopg2

conn=psycopg2.connect(
  database="recondb",
  user="py_server",
  host="localhost",
  password="5432"
)