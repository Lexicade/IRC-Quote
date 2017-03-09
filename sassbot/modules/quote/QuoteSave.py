def Save(phenny, strNick, strInput):
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=phenny.config.mysql_username, passwd=phenny.config.mysql_password,db="IRC")
    c = db.cursor()

    c.execute("INSERT INTO `quote-grab` (`savedby`, `quote`) VALUES (%s, %s);", (strNick, strInput[6:]))
    db.commit()

    db.query("SELECT `ID` FROM `quote-grab` WHERE `quote` = '" + strInput[6:] + "';")
    r = db.store_result()
    strID = str(r.fetch_row(maxrows=1))[2:-5]

    return strID