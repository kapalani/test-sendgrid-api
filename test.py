import sendgrid
import sys
try:
    import rfc822
except Exception as e:
    import email.utils as rfc822

USER_NAME = "kavin"
PASSWORD = "Netapp123"

def testScenarioOne():
    sg = sendgrid.SendGridClient(USER_NAME, PASSWORD)
    message = sendgrid.Mail()
    message.add_to("<kavinkumar_p@yahoo.co.in>")
    message.add_to_name("Kumar, Palani")
    message.set_from("kavinpalni@gmail.com")
    message.set_from_name("Kavin");
    message.set_subject("Test message.,")
    message.set_text("Test text")
    message.set_html("<i><b>Test HTML</b></i>")
    message.add_cc("kavin@netapp.com")
    message.set_replyto("sukanyamani2289@gmail.com")
    message.set_date(rfc822.formatdate())
    status, msg = sg.send(message)
    print msg

if __name__ == '__main__':
    testScenarioOne();


