#!/bin/sh
echo "Content-type: text/html"
echo
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` 
id=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/instance-id)
az=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/placement/availability-zone)
pridns=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/local-hostname)
priip=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/local-ipv4)
pubdns=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/public-hostname)
pubip=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/public-ipv4)
time=$(TZ=UTC-9 date '+%Y/%m/%d %H:%M:%S JST')
echo "<!DOCTYPE html>"
echo "<html>"
echo "<head>"
echo "<title>Apache Web Server</title>"
echo "</head>"
echo "<body>"
echo $time
echo "<h2>Target information</h2>"
echo "<table border=\"1\">"
echo "<tr>"
echo "<th>Key</th>"
echo "<th>Value</th>"
echo "</tr>"
echo "<tr>"
echo "<td>Instance ID</td>"
echo "<td>"
echo $id
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>Availability Zone</td>"
echo "<td>"
echo $az
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>Public IPv4 DNS</td>"
echo "<td>"
echo $pubdns
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>Public IPv4 Address</td>"
echo "<td>"
echo $pubip
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>Private IPv4 DNS</td>"
echo "<td>"
echo $pridns
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>Private IPv4 Address</td>"
echo "<td>"
echo $priip
echo "</td>"
echo "</tr>"
echo "</table>"
echo
echo "<br>"
echo "<h2>Environmental variation</h2>"
echo "<table border=\"1\">"
echo "<tr>"
echo "<th>Key</th>"
echo "<th>Value</th>"
echo "</tr>"
echo "<tr>"
echo "<td>REMOTE_ADDR</td>"
echo "<td>"
echo $REMOTE_ADDR
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_USER_AGENT</td>"
echo "<td>"
echo $HTTP_USER_AGENT
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_ACCEPT_LANGUAGE</td>"
echo "<td>"
echo $HTTP_ACCEPT_LANGUAGE
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_COOKIE</td>"
echo "<td>"
echo $HTTP_COOKIE
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_REFERER</td>"
echo "<td>"
echo $HTTP_REFERER
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_FORWARDED</td>"
echo "<td>"
echo $HTTP_FORWARDED
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_X_FORWARDED_FOR</td>"
echo "<td>"
echo $HTTP_X_FORWARDED_FOR
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>REMOTE_PORT</td>"
echo "<td>"
echo $REMOTE_PORT
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>SERVER_SOFTWARE</td>"
echo "<td>"
echo $SERVER_SOFTWARE
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>SERVER_PROTOCOL</td>"
echo "<td>"
echo $SERVER_PROTOCOL
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>SERVER_PORT</td>"
echo "<td>"
echo $SERVER_PORT
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>SERVER_NAME</td>"
echo "<td>"
echo $SERVER_NAME
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>SERVER_ADDR</td>"
echo "<td>"
echo $SERVER_ADDR
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>HTTP_HOST</td>"
echo "<td>"
echo $HTTP_HOST
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>PATH</td>"
echo "<td>"
echo $PATH
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>SCRIPT_NAME</td>"
echo "<td>"
echo $SCRIPT_NAME
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>CONTENT_LENGTH</td>"
echo "<td>"
echo $CONTENT_LENGTH
echo "</td>"
echo "</tr>"
echo "<tr>"
echo "<td>QUERY_STRING</td>"
echo "<td>"
echo $QUERY_STRING
echo "</td>"
echo "</tr>"
echo "</table>"
echo
echo "<br>"
echo "</body>"
echo "</html>"