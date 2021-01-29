#+----------------------------------------------------------------------+
#Imports
import os
import time
from termcolor import colored
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#+----------------------------------------------------------------------+
#loading+banner
def loading():
	part1=(colored("   .~~.   .~~.", "green"))
	part2=(colored("  '. \ ' ' / .'", "green"))
	part3=(colored("   .~ .~~~..~.", "red"))
	part4=(colored("  : .~.'~'.~. :", "red"))
	part5=(colored(" ~ (   ) (   ) ~", "red"))
	part6=(colored("( : '~'.~.'~' : )", "red"))
	part7=(colored(" ~ .~ (   ) ~. ~", "red"))
	part8=(colored("  (  : '~' :  ) ", "red"))
	part9=(colored("   '~ .~~~. ~'  ", "red"))
	part10=(colored("       '~'", "red"))
	tool=(colored("Raspy Mail", "blue"))
	credit=(colored("CREDIT:Mr. Pascal", "blue"))
	version=(colored("VERSION:1.0", "blue"))
	print(part1)
	time.sleep(0.5)
	print(part2)
	time.sleep(0.5)
	print(part3)
	time.sleep(0.5)
	print(part4)
	time.sleep(0.5)
	print(part5)
	time.sleep(0.5)
	print(part6)
	time.sleep(0.5)
	print(part7+tool)
	time.sleep(0.5)
	print(part8+version)
	time.sleep(0.5)
	print(part9+credit)
	time.sleep(0.5)
	print(part10)
	time.sleep(2)
	os.system("clear")


#Banner
def banner():
	banner=open("./banner/banner.txt", "r").read()
	print(colored(banner, "red"))
	print(colored("https://www.github.com/cryp70m4n/Raspy-Mail", "red"))
	print(colored("----------------------------------------------------------", "red"))
loading()
banner()
#+----------------------------------------------------------------------+
#smtp server
server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


def manual_inputs():
	mail=[]
	#sender email(sending mails from this email address)
	sender = input(colored("Enter sender:", "red"))

	#sender email account passowrd
	password=input(colored("Enter password:", "red"))

	#receiver email(receiving emails on this email address)
	reciever=input(colored("Enter reciever:", "red"))

	mail.append(sender)
	mail.append(password)
	mail.append(reciever)
	return mail

def automatic_inputs():
	mail=[]
	sender=open("./auto_inputs/sender.txt", "r").read()
	reciever=open("./auto_inputs/reciever.txt", "r").read()
	password=open("./auto_inputs/password.txt", "r").read()
	mail.append(sender)
	mail.append(password)
	mail.append(reciever)
	return mail


while True:
	print(colored("[1]-Manual input", "red"))
	print(colored("[2]-Automatic input", "red"))
	print(colored("[.]-Quit", "red"))
	choice=input(colored("Enter your choice:", "red"))
	if choice=="1":
		mail=manual_inputs()
		break
	if choice=="2":

		mail=automatic_inputs()
		break
	if choice==".":
		os.system("clear")
		quit()
	else:
		print(colored("Wrong input, try again please!", "red"))
		continue


#Smtp login to sender email
server.login(mail[0], mail[1])

print(colored(f"Logged in as:{mail[0]}", "red"))
#+----------------------------------------------------------------------+
#def message
def message():
	#message
	message=input(colored("Enter message to send:", "red"))
	#mail subject
	subject="Raspy Mail"
	#Smtp send email
	server.sendmail(mail[0], mail[2], message)
	print(colored(f"Email sent to:{mail[2]}  message:{message}", "red"))

#def attachment
def attachment():
	file_input=input(colored("Please enter the file you would like to send:", "red"))

	subject = "Raspy Mail"

	msg = MIMEMultipart()
	msg['From'] = mail[0]
	msg['To'] = mail[2]
	msg['Subject'] = subject

	body = 'Raspy Mail'
	msg.attach(MIMEText(body, 'plain'))
	attachment = open(file_input, 'rb')

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= " + file_input)	
	msg.attach(part)
	text = msg.as_string()
	server.sendmail(mail[0], mail[2], text)
	print(colored(f"attachment:{file_input} sent to:{mail[2]}", "red"))

#+----------------------------------------------------------------------+
while True:
	print(colored("[1]-send message", "red"))
	print(colored("[2]-send attachment", "red"))
	print(colored("[.]-Quit", "red"))
	email=input(colored("Enter your choice:", "red"))
	if email == "1":
		message()
		time.sleep(5)
		os.system("clear")
	if email == "2":
		attachment()
		time.sleep(5)
		os.system("clear")
	if email == ".":
		os.system("clear")
		quit()
	else:
		print(colored("Wrong input try again", "red"))
#+----------------------------------------------------------------------+
