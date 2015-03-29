import gspread
import sys
#from xml.etree import ElementTree

if len(sys.argv) < 3:
   print("usage \"python bot.py <gmail_username> <gmail_password>\"")
   exit(1)

gmail_username = sys.argv[1]
gmail_password = sys.argv[2]
filename = sys.argv[3]

# Login with your Google account
gc = gspread.login(gmail_username, gmail_password)

# Open a worksheet from spreadsheet with one shot
wks = gc.open(filename).sheet1

print(wks.acell('A1').value)



