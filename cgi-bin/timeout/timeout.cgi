#!/bin/sh
echo "Content-type: text/html"
echo
echo "<!DOCTYPE html>"
echo "<html>"
echo "<head>"
echo "<title>Apache Web Server</title>"
echo "</head>"
echo "<body>"
period=$(pwd | awk -F "/" '{ print $NF }')
echo "Sleep for "
echo $period
echo "sec"
echo "<br>"
echo "<br>"
echo
echo "Time Before Sleep Statement:"
time_b=$(TZ=UTC-9 date '+%Y/%m/%d %H:%M:%S JST')
echo $time_b
echo
echo "<br>"
echo "Waiting..."
echo "<br>"
echo "<br>"
sleep $period
echo
echo "Time After Sleep Statement:"
time_a=$(TZ=UTC-9 date '+%Y/%m/%d %H:%M:%S JST')
echo $time_a
echo
echo "<br>"
echo "Completed!!"
echo "<br>"
echo "<br>"
echo "</body>"
echo "</html>"