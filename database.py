import sqlite3
from pathlib import Path

class Database:
    def __init__(self,path="data/output/sentinel.db"):
        Path(path).parent.mkdir(parents=True,exist_ok=True)
        self.db=sqlite3.connect(path)
        self.db.execute("""CREATE TABLE IF NOT EXISTS iocs(
        id INTEGER PRIMARY KEY,value TEXT,type TEXT,source TEXT,risk INTEGER,
        severity TEXT,confidence REAL,technique TEXT,tactic TEXT,context TEXT)""")
        self.db.commit()

    def save(self,iocs):
        self.db.executemany("""INSERT INTO iocs
        (value,type,source,risk,severity,confidence,technique,tactic,context)
        VALUES(?,?,?,?,?,?,?,?,?)""",
        [(x.value,x.ioc_type,x.source,x.risk,x.severity,x.confidence,
          x.technique,x.tactic,x.context) for x in iocs])
        self.db.commit()

    def close(self):
        self.db.close()
