#Given a set of ip addresses and ports, enumerate ports & services
#Scans all common ports by default, unless a ports file is given / all ports specified

#TODO: Implement loading bar

#TODO: Implement colored output

import argparse
import scan
import alive_progress

if __name__ == "__main__":

    #init arg parse
    parser = argparse.ArgumentParser(prog="Port Scanner", description="Allows for a number of other port scanning options", epilog="Written by Addison Teschan")
    parser.add_argument('-i','--ip',help='path to file for ip addreses',type=str,required=True)
    parser.add_argument('-p','--port',help='path to file for port numbers',type=str)
    parser.add_argument('-v','--version',help='enumerates service version info',action='store_true')
    parser.add_argument('-a','--all',help='scans all ports',action='store_true')
    parser.add_argument('-t','--time',help='time between each scan',type=int)
    args = parser.parse_args()

    #formatting
    ips=[]
    with open(args.ip) as f:
        for line in f:
            ips.append(line.replace('\n', ''))

    scan.syncScan(ips, args.port, args.version, args.all, args.time) 
   
    print("Success!")
