import psycopg2

def load(data):
    conn = psycopg2.connect(
        host="localhost",
        database="data_pipeline",
        user="postgres",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO crypto (time, rate) VALUES (%s, %s)", (data["time"], data["usd_rate"]))
    conn.commit()
    cur.close()
    conn.close()
