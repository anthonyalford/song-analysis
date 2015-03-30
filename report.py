import csv

def time_to_secs(time):
    split_time = time.split(":")
    secs = int(split_time[0]) * 3600 + int(split_time[1]) * 60 + int(split_time[2])
    return secs

def to_minutes(t):
    hours = t / 3600
    minutes = (t - (hours * 3600)) / 60
    secs = t - (hours * 3600) - (minutes * 60)
    return "%d-%d-%d" % (hours,minutes, secs)

with open('/Users/anthonya/Downloads/set2.txt','rb') as tsvin, open('/Users/anthonya/Downloads/new.txt', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout)
    tsvin.next()

    increment = 30
    secpoint = 0
    for row in tsvin:
        song = row[0]
        start_time = row[1]
        end_time = row[2]

        start_sec = time_to_secs(start_time)
        end_sec = time_to_secs(end_time)
        print ""
        print "## " + song + " (" + start_time + " - " + end_time + ")"
        while(secpoint<end_sec):
            print "![](img/frame_" + to_minutes(secpoint) + ".jpg)"
            secpoint = secpoint + increment
