def RandomQuote(strInputNick):
    import os
    import random

    if os.path.exists('/home/bouncer/test/' + strInputNick + '.txt'):
        strQuoteLength = 0
        while strQuoteLength <= len("] <" + strInputNick + "> 123456789012345") - 2:
            strQuote = random.choice(open('/home/bouncer/test/' + strInputNick + '.txt').readlines())
            strQuoteLength = len(strQuote)

        return strQuote