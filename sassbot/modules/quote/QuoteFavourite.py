def SaveFavourite(phenny):
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=phenny.config.mysql_username, passwd=phenny.config.mysql_password, db='IRC')
    c = db.cursor(MySQLdb.cursors.DictCursor)

    strQuote = intQuoteID = ""
    c.execute("SELECT `ID`, `quote` FROM `quote-grab` ORDER BY RAND() LIMIT 1;")
    sqlRandomQuote = c.fetchall()
    for row in sqlRandomQuote:
        strQuoteID = "[ID:" + str(row["ID"]) + "]"
        strQuoteString = row["quote"]
    return strQuoteID+strQuoteString