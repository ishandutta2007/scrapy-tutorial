import sqlite3


class TutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('MyQuotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                        title text,
                        author text,
                        tag text
                    )""")
    
    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (?, ?, ?)""", (
                            item['title'][0],
                            item['author'][0],
                            item['tag'][0]
                        ))
        
        self.conn.commit()