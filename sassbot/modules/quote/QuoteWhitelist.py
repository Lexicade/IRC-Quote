def Main(strInput2, strInput3, phenny):
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=phenny.config.mysql_username, passwd=phenny.config.mysql_password, db="IRC")
    c = db.cursor(MySQLdb.cursors.DictCursor)

    if strInput2 == 'add':
        c.execute("UPDATE `quote` SET `whitelisted`=1 WHERE `nick` = %s;", (strInput3));db.commit()
        return strInput3 + " has been whitelisted."
    elif strInput2 == 'rem':
        c.execute("UPDATE `quote` SET `whitelisted`=0 WHERE `nick` = %s;", (strInput3));db.commit()
        return strInput3 + " has been blacklisted."