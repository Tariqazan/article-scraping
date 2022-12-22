import mysql.connector

def save_to_database(name,link, description, image):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="article-data"
)

  mycursor = mydb.cursor()


  sql = "INSERT INTO articles (title, link, description, image) VALUES (%s, %s, %s, %s)"
  val = (name, link, description, image)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")