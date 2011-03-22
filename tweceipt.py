import serialEscPos,twitter,time
rp = serialEscPos.serialEscPos()
api = twitter.Api()

while 1:
    rp.useSlip()
    
    #statuses = api.GetPublicTimeline()
    statuses = api.GetUserTimeline("mich181189")
    count = 0
    for status in statuses:
        if(count > 5):
            print "Done 5, so waiting."
            rp.ff()
            time.sleep(30)
            statuses = []
            continue
        count +=1
        
        rp.reallywide()
        rp.println(status.user.name)
        rp.normalwide()
        rp.println(status.text)
        rp.println("")
        rp.println("")
    rp.ff() #form feed
    time.sleep(30)