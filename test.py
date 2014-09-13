import sendgrid
import sys
try:
    import rfc822
except Exception as e:
    import email.utils as rfc822

USER_NAME = "kavin"
PASSWORD = "Netapp123"

def setup():
    sg = sendgrid.SendGridClient(USER_NAME, PASSWORD)
    return sg

def config_mail():
    message = sendgrid.Mail()
    message.add_to("<kavinkumar_p@yahoo.co.in>")
    message.add_to_name("Kumar, Palani")
    message.set_from("kavinpalni@gmail.com")
    message.set_from_name("Kavin");
    message.set_subject("Test message.,")
    message.set_text("Test text")
    message.set_html("<i><b>Test HTML</b></i>")
    message.set_replyto("sukanyamani2289@gmail.com")
    message.set_date(rfc822.formatdate())
    return message

def testScenarioOne():
    sg = setup()
    message = config_mail()
    status, msg = sg.send(message)

    if status == 200:
        print "Test Scenario 1 passed"
    else:
        print "Test Scenario 1 failed"
        print msg

def testScenariotwo():
    sg = setup()
    message = config_mail()
    message.add_cc("kavin@netapp.com")
    status, msg = sg.send(message)

    if status == 200:
        print "Test Scenario 2 passed"
    else:
        print "Test Scenario 2 failed"
        print msg

def testScenarioThree():
    sg = setup()
    message = config_mail()
    message.add_attachment("abc.txt", "abc.txt")
    message.add_attachment("Pete.mp4", "Pete.mp4")
    status, msg = sg.send(message)

    if status == 200:
        print "Test Scenario 3 passed"
    else:
        print "Test Scenario 3 failed"
        print msg

def testScenarioFour():
    sg = setup();
    message = config_mail()
    message.add_attachment("TaylorSwift.mp4", "TayLorSwift.mp4")

    try:
        status, msg = sg.send(message)
        if status == 200:
            print "Test Scenario 4 passed"
        else:
            print "Test Scenario 4 failed"
            print msg
    except Exception as e:
        print sendgrid.SendGridError(e);

if __name__ == '__main__':
    testScenarioOne()
    testScenariotwo()
    testScenarioThree()
    testScenarioFour()


