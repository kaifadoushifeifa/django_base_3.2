import pymysql
pymysql.version_info = (1, 4, 0, "final", 0)   # 指定版本
pymysql.install_as_MySQLdb()