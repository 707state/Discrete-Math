import sqlite3
import time as tm
class Restore:
    con=sqlite3.connect("RestorePrimaryWFF.db")
    def __int__(self,targetText:str,outcome:list):
        with self.con:
            try:
                self.con.execute("""
                    CREATE TABLE WFF(
                        id text ,
                        WFF text,
                        outcome text
                    );
                """)
            except:
                pass
        insideData='\n'.join(outcome)
        sql = "INSERT INTO WFF (id, WFF, outcome) VALUES(?, ?, ?)"
        t=tm.localtime(tm.time())
        with self.con:
            data=[
                str(tm.asctime(t)),
                targetText,
                insideData
            ]
            self.con.execute(sql,data)
    def PrintHistory(self)->list:
        History=[]
        with self.con:
            try:
                data=self.con.execute("SELECT * FROM WFF")
                if data is not None:
                    for row in data:
                       History.append(str(row))
                else:
                    History.append("尚未添加数据")
            except:
                History.append("请输入数据")
        return History
    def DeleteData(self):
        cmdDelete='DROP TABLE WFF'
        self.con.execute(cmdDelete)
        self.con.commit()