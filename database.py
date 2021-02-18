import psycopg2
import os

class Database():
    def __init__(self):
        self.con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS data(email VarChar(50) UNIQUE, height INTEGER)")
        self.con.commit()
    def insert(self, email, height):
        self.cur.execute("INSERT INTO data VALUES(%s, %s)", (email,height))
        self.con.commit()
    def extract_heights(self):
        self.cur.execute("SELECT height FROM data")
        heights = [i[0] for i in self.cur.fetchall()]
        return heights
    def extract_emails(self):
        self.cur.execute("SELECT email FROM data")
        emails = [i[0] for i in self.cur.fetchall()]
        return emails
    def __del__(self):
        self.con.close()