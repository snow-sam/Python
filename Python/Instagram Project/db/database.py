import sqlite3

conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

def create_table():
    # Create table - Posts
    c.execute('''CREATE TABLE IF NOT EXISTS POSTS ([Media_id] TEXT, [Imagem] TEXT, [Caption] TEXT, [Likes] INTEGER, [Url] TEXT, [Pk] INTEGER)''')


def data_entry(media_id, imagem,caption, likes, url, pk):
    c.execute("INSERT INTO POSTS (media_id, imagem, caption, likes, url, pk ) VALUES (?, ?, ?, ?, ?, ? )"), (media_id, imagem,caption, likes, url, pk)
    conn.commit()
    
def close_con():
    c.close()
    conn.close()


create_table()