# from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import numpy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendMail(first_name, name, email):
    fromaddr = ""  ########################################################### ENTER YOUR EMAIL HERE
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Certificate of Appreciation"
    body = f"""\
    <html>

<head>
    <meta first_name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <h2>Greetings {first_name}!</h2>
    <p><b>Congratulations on Winning CODEAGER-2021 !!</b></p>
    Kindly find your E-Certificate for the same, attached along with this mail.
    <br>We look forward to seeing you at all our future workshops, seminars and events!
    <br><br>Regards,
    <br>IEEE-VIT Student Branch
    <br>
    <center><br>Connect with us on
        <br>
        <p>
            <a href="https://www.youtube.com/channel/UCO7ECcxG7aSYB0mxh88g_KA">
                <img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/youtube-512.png"
                    height="45" width="45" hspace='20'>
            </a>
            <a href="https://www.instagram.com/ieeevit/">
                <img src="https://www.pinclipart.com/picdir/big/1-13590_instagram-logo-insta-logo-png-transparent-background-clipart.png"
                    height="45" width="45" hspace='20'>
            </a>
            <a href="https://twitter.com/vidyalankarieee?lang=en">
                <img src="http://jetprogramme.org/wp-content/uploads/2017/03/twitter-logo.png" height="45" width="45"
                    hspace='20'>
            </a>
            <a href="https://www.facebook.com/IEEEVIT1/">
                <img src="https://1000logos.net/wp-content/uploads/2016/11/Facebook-logo-768x538.png" height="50"
                    width="70">
            </a>
            <br>
            <br><a href="http://ieee.vit.edu.in/index.html">
                <img src="https://ieee.vit.edu.in/assets/images/ieeevit-blue-1-5017x1103.png" height="50"
                    width="200"></a>
            <br>

            <font size="2">Ask us anything about programming, meet like minded people, build
                projects.<br>

                <center>Join the Coders Republic Group now:
            </font><br><br>
            <a href="https://chat.whatsapp.com/GNjVY5fSZav73fl77vGPj2">
                <img src="http://www.idroexpert.com/wp-content/uploads/soon-873316_960_720.png" height="50" width="50"
                    hspace="20">
            </a><br><br>
        <p>For any errors in certificate<a href="https://goo.gl/forms/8dqLFOmrG3KZs65f2"> click
                here</a></p>
</body>

</html>
    """

    # for certificate
    certificate = open(
        f"D:/_Shubham/shubham/Cert_&_emails_python/workshop_cert/{name}.png", "rb")   ########## Path of certificate
    msg.attach(MIMEText(body, 'html'))
    filename = f"{name}.png"
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((certificate).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    # for zipfile
    # zipfile = open("D:/Shubham/shubham/Cert_&_emails_python/OpenCV_workshop.zip", "rb")
    # filename1 = "OpenCV_workshop.zip"
    # p1 = MIMEBase('application', 'octet-stream')
    # p1.set_payload((zipfile).read())
    # encoders.encode_base64(p1)
    # p1.add_header('Content-Disposition', "attachment; filename= %s" % filename1)
    # msg.attach(p1)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "") ################################################################################ ENTER YOUR PASSWORD HERE
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


df = pd.read_csv("D:\_Shubham\shubham\Cert_&_emails_python\cert1.csv") ################# The path where csv is there ==> | name | email |
for i in range(len(df)):
    name = df.iloc[i, 0]
    email = df.iloc[i, 1]
    first_name = name.split()[0]
    sendMail(first_name, name, email)
    print(f"Sent {name}")
