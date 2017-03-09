def DeleteFavourite(phenny, inCmd2):
    import MySQLdb
    try:
        strInputID = inCmd2
    except IndexError:
        strInputID = ''

    db = MySQLdb.connect(host='localhost', user=phenny.config.mysql_username, passwd=phenny.config.mysql_password, db='IRC')
    c = db.cursor(MySQLdb.cursors.DictCursor)
    if strInputID.isnumeric():
        c.execute('DELETE FROM `quote-grab` WHERE `ID`=' + str(strInputID))
        db.commit()
        return 'Deleted.'
    else:
        return 'Please enter the ID for the quote you want to delete.'