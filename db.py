import psycopg

class Database:
    def __init__(self, host, port, dbname, user, password):
        self.conn = psycopg.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
            row_factory=psycopg.rows.dict_row
        )

    def fetch_all(self, query, params=None) -> list[dict]:
        with self.conn.cursor() as cur:
            cur.execute(query, params or ())
            return cur.fetchall()

    def fetch_one(self, query, params=None) -> dict:
        with self.conn.cursor() as cur:
            cur.execute(query, params or ())
            return cur.fetchone()

    def execute(self, query, params=None) -> None:
        with self.conn.cursor() as cur:
            cur.execute(query, params or ())
            self.conn.commit()

    def close(self):
        self.conn.close()
