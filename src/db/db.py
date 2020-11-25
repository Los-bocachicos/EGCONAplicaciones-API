import mysql.connector as mysql


class ConexionDB:

    @staticmethod
    def conexion():
        cnx = mysql.MySQLConnection(
            host="34.121.18.138",
            port=3306,
            user="elias",
            password="elias",
            database="evergreen_con",
            auth_plugin="mysql_native_password"
        )
        return cnx
