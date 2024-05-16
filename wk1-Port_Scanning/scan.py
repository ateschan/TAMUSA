#syncronous scan or something idk

import nmapthon2 as n
import utils
from alive_progress import alive_bar


#-------------------------------SCAN-----------------------------------

def syncScan(ips, ports, version, allPorts, scanTime):

    #translating parsed arguments
    nmapArgs = ""
    nmapArgs += "-sV " if version == True else ""
    nmapArgs += "--scan-delay {}".format(scanTime) if scanTime != None else ""
    ports2Scan = "1-65535 " if allPorts == True else "1-1024"

    if ports != None:
        ports2Scan = []
        file = open(ports, 'r')
        for line in file:
            ports2Scan.append(int(line.replace('\n', '')))

    scanner = n.NmapScanner()
    print("ARGUMENTS GIVEN:  " + nmapArgs)
    
    with alive_bar(len(ips), title='SCANNING', bar='smooth', spinner='wait', enrich_print=False, precision=2) as bar:
        for ip in ips:
            utils.printInfo(scanner.scan(ip, ports=ports2Scan, arguments=nmapArgs))
            bar()
