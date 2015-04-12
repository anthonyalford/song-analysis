import csv
import subprocess


with open('/Users/anthonya/Downloads/Redline.txt','rb') as tsvin, open('/Users/anthonya/Downloads/new.txt', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    tsvin.next() # read header

    for row in tsvin:
        name = row[0]
        path = row[26]
        path = path.replace(":","/").replace("Macintosh HD","").replace(" ","\\ ").replace("(","\\(").replace(")","\\)").replace("'","\\'").replace("&","\\&")

        cmd = "sox -V1 %s -t raw -r 44100 -e float -c 1 - | bpm" % path
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        res = repr(p.stdout.readlines()).replace("['","").replace("\\n']","")
        retval = p.wait()
        print "File: %s, BPM: %s" % (name, res)
