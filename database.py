import sqlite3
import os

DB_DIR = os.path.join(os.path.expanduser("~"), "job_data")
DB_PATH = os.path.join(DB_DIR, 'video_data.db')
os.makedirs(DB_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS video(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    标题 TEXT NOT NULL,
    up主 TEXT NOT NULL,
    播放量 TEXT NOT NULL,
    点赞数 TEXT NOT NULL
)''')
conn.commit()
conn.close()

def save_data(data):
    if data is None:
        print("没有数据。")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    count = 0
    for item in data:
        cursor.execute('''
        INSERT INTO video(标题,up主,播放量,点赞数) 
        VALUES (?,?,?,?)''',(
            item.get('标题',''),
            item.get('up主',''),
            item.get('播放量',''),
            item.get('点赞数',''),
        ))
        count += 1
    conn.commit()
    conn.close()
    print(f'存入了{count}条数据。')










