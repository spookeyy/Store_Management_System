from lib.config import DATABASE, CURSOR

class Admin:
    @classmethod
    def login(cls, username, password):
        sql = "SELECT * FROM admin WHERE username = ? AND password = ?"
        CURSOR.execute(sql, (username, password))
        return CURSOR.fetchone()

    @classmethod
    def create_admin(cls, username, password):
        sql = "INSERT INTO admin (username, password) VALUES (?, ?)"
        CURSOR.execute(sql, (username, password))
        DATABASE.commit()
        admin_id = CURSOR.lastrowid
        CURSOR.execute("SELECT * FROM admin WHERE id = ?", (admin_id,))
        return CURSOR.fetchone()
    

admin = Admin()
# admin.create_admin("admin", "admin")