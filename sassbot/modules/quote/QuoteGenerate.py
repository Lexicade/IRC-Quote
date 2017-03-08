def Gen(strInputNick):
    import MySQLdb
    from subprocess import Popen
    import os

    db = MySQLdb.connect(host="localhost", user=phenny.config.mysql_username, passwd=phenny.config.mysql_password, db="IRC")
    c = db.cursor()

    c.execute("UPDATE `quote` SET `genlock`=1 WHERE `nick` = %s;", strInputNick)
    db.commit()
    boolGenerating = True
    Process = Popen('/home/bouncer/test/GenerateUser.sh %s' % strInputNick, shell=True).wait()
    c.execute("UPDATE `quote` SET `genlock`=0 WHERE `nick` = %s;", strInputNick)
    db.commit()
    boolGenerating = False
    f = open('/home/bouncer/test/' + strInputNick + '.txt')
    lines = f.readlines()

    if os.path.exists('/home/bouncer/test/' + strInputNick + '.txt'):
        os.remove('/home/bouncer/test/' + strInputNick + '.txt')

    for line in lines:

        line2 = line[62:]

        if str(line2[:8]) == "#thelewd":
            line3 = line[99:]
        elif line2[:8] == "#jerseye":
            line3 = line[101:]

        with open('/home/bouncer/test/' + strInputNick + '.txt', "a") as myfile:
            myfile.write(line3)

    return