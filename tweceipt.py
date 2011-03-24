import serialEscPos,twitter,time
rp = serialEscPos.serialEscPos()
api = twitter.Api()

got = {}
latest=0
searchterm = ""
slipprint = False
starttime = time.time()
stopbeforeprint = True


def printstatus(status):
    global got,rp
    if status.id in got:
        return
    got[status.id] = status.id
    if stopbeforeprint:
        print "In stop before print mode. Won't actually print.\n"
        return
    rp.doubleStrike(1)
    rp.underline(1)
    rp.centre()
    rp.println("@" + unicode(status.user.screen_name).encode('ascii', 'ignore'))
    rp.left()
    rp.doubleStrike(0)
    rp.underline(0)
    rp.println(unicode(status.text).encode('ascii', 'ignore'))
    rp.println("")

def prime(term):
    global api,latest,searchterm
    searchterm = term
    res = api.GetSearch(term=searchterm,per_page=1)
    if(len(res) > 0):
        latest=res[0].id
        printstatus(res[0])

def checkfornew():
    print "running...\n"
    global api,latest,searchterm
    res = api.GetSearch(term=searchterm,per_page=5,since_id=latest)
    for status in res:
        if status.id > latest:
            latest = status.id
        printstatus(status)

def endslip():
    global rp
    if not rp.usingSlip():
        print "Asked to end slip. No slip in use."
        return
    rp.ff()
    #first wait for the slip to need removing:
    while not rp.slipWaiting():
        time.sleep(0.5)
    #now wait for the slip to be removed
    print "Please remove slip.\n"
    while rp.slipWaiting():
        time.sleep(0.5)
    print "Thankyou.\n"

if slipprint:
        rp.useSlip()
    
prime("\"is down\"")

while 1:
    checkfornew()   
    for n in range( 30):
        time.sleep(1)
        if rp.slipAvailable() and not slipprint:
            rp.useSlip()
            rp.centre()
            rp.doubleStrike(1)
            rp.underline(1)
            rp.println("Tweceipt Printer Stats")
            rp.doubleStrike(0)
            rp.underline(0)
            rp.left()
            rp.println("Started at: " + time.asctime(time.localtime(starttime)))
            rp.println("Tweets printed: " + str(len(got)))
            rp.println("That's " + str(len(got)/((time.time()-starttime)/3600)) + " tweets/hour")
            endslip()
    print "Started at: " + time.asctime(time.localtime(starttime))
    print "Tweets printed: " + str(len(got))
    print "That's " + str(len(got)/((time.time()-starttime)/3600)) + " tweets/hour"
