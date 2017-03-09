import MySQLdb
import re
import random
import subprocess
import sys
import os
sys.path.insert(0, '/home/bouncer/sassbot/modules/quote/')
import QuoteMain
import QuoteGenerate
import QuoteSave
import QuoteWhitelist
import QuoteDelete
import QuoteFavourite

def q(phenny, input):

    def Botify(strInput):
        c.execute("SELECT `Nick` FROM `LastSeen`;")
        while True:
            row = c.fetchone()
            if row is None:
                break
            strInput = strInput.replace(str(row["Nick"]), str(row["Nick"]) + "bot")
            strInput = strInput.replace(str(row["Nick"]).lower(), str(row["Nick"]).lower() + "bot")
        return strInput

    db = MySQLdb.connect(host="localhost", user=phenny.config.mysql_username, passwd=phenny.config.mysql_password, db="IRC")
    c = db.cursor(MySQLdb.cursors.DictCursor)


    #WIP: Make stat tracker
    #c.execute("UPDATE `stats` SET `uses`=`uses`+1 WHERE `nick` = %s AND `command`='q';", (input.nick))
    #db.commit()

    #WIP: From !q v1, needs re-writing at some point
    db.query("SELECT count(`nick`) as CountOfNick FROM `quote` WHERE `nick` = '" + input.nick + "';")
    r = db.store_result()
    intTotalUsers = str(r.fetch_row())[2:-5]
    if intTotalUsers == '0':
        phenny.say("You have been added to the !q database. Contact JasonFS for whitelisting.")
        c.execute("INSERT INTO `quote` (`nick`, `cooldown`, `whitelisted`, `genlock`) VALUES (%s, %s, %s, %s);",(input.nick, 0, 0, 0))
        db.commit()
    else:
        inCmd = input.group().split(' ')

        c.execute("SELECT `cooldown`,`whitelisted`,`genlock` FROM `quote` WHERE `nick` LIKE '" + input.nick + "';")
        sqlDetails = c.fetchall()
        for row in sqlDetails:
            intCooldown = row["cooldown"]
            intWhitelist = row["whitelisted"]
            intGenlock = row["genlock"]

        if intGenlock == 1:
            #return "Please wait while your logfile is being generated."
            phenny.say("Please wait while your logfile is being generated.")
        elif intCooldown > 0:
            #return "Fucking calm down, son."
            phenny.say("Fucking calm down, son.")
        elif input.sender.lower() == "#fromsteamland" or input.sender.lower() == "#thelewdzone":
            if '-h' in inCmd:
                phenny.say("Available commands are: -w(hitelist), -l(ist favourites), -rm <Number>(Delete favourited quotes), -gen(erate logfile), -s(ave) <Quote>")
            elif '-w' in inCmd:
                strReturn = QuoteWhitelist.Main(inCmd[2], inCmd[3], phenny)
                phenny.write(('NOTICE', input.nick), strReturn)
            elif '-l' in inCmd and intWhitelist == 1:
                strReturn = QuoteFavourite.SaveFavourite(phenny)
                phenny.say(Botify(strReturn))
            elif '-rm' in inCmd and intWhitelist == 1:
                strReturn = QuoteDelete.DeleteFavourite(phenny, inCmd[2])
                phenny.say(strReturn)
            elif '-gen' in inCmd and intWhitelist == 1:
                phenny.say("Creating logfile. Please wait...")
                QuoteGenerate.Gen(phenny, input.nick)
                phenny.say("Your logfile is complete.")
            elif '-s' in inCmd and intWhitelist == 1:
                strID = QuoteSave.Save(phenny, input.nick, input.group())
                phenny.say("Quote saved with ID: "+strID)
            elif input.group() == "!q" and intWhitelist == 1:
                strReturn = QuoteMain.RandomQuote(input.nick)
                strReturn = Botify(strReturn)
                phenny.say(str(strReturn))
        else:
            phenny.write(('NOTICE', input.nick), "!q is restricted to #thelewdzone")
    #else:
        #phenny.say("!q is disabled while it's being rewritten")

q.commands = ['q', 'Q']
q.priority = 'high'
q.example = "whatever..."
