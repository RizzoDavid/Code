#!/bin/bash
#Command Structure ./ip_trace.sh ipaddress
    #ex: ./ip_trace 52.65.23.56

#Add text line to ip_trace.txt | Get info for IP Address |Find the line that has the country | Only keep country code from country line

echo "The country code for IP Address " $1 " is " >> ip_trace.txt | curl -s http://ipinfo.io/$1 | grep country | awk -F: '{print$(2)}' >> ip_trace.txt