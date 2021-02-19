import sqlite3

db_path = r'C:\Users\Michael\AppData\Local\Google\Chrome\User Data\Default\History'
conn = sqlite3.connect(db_path)
sql = "select * from urls"
c = conn.cursor()
urls = c.execute(sql).fetchall()
for url in urls:
  print(url[0], url[1])
c.close()