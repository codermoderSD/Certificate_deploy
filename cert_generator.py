# from PIL import Image, ImageFont, ImageDraw
import pandas as pd
# import numpy
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# def createCertificate(name):
#     FONT_COLOR = "#000000"
#     WIDTH, HEIGHT = 3627, 1253
#     image_source = Image.open(r'dummy.jpg')
#     draw = ImageDraw.Draw(image_source)
#     font = ImageFont.truetype("arial.ttf", 150)
#     w, h= draw.textsize(name, font=font)
#     draw.text(((WIDTH-w)/2,1200), name, fill=FONT_COLOR, font=font)
#     image_source.save("\shubham\Cert_&_emails_python\\" + "Participation_cert"+".jpg")
#     print('printing certificate of: '+name)
    
def sendMail(name,email):
    fromaddr = "sdisilva13@gmail.com"
    #"*Add your email*"
    toaddr = email
    msg = MIMEMultipart()  
    msg['From'] = fromaddr 
    msg['To'] = toaddr  
    msg['Subject'] = "Certificate of Participation"
    body = """\
    <html>
    <body>
        <p><b>Thanks for attending workshop on Gesture Controlled Gaming using OpenCV</b></p>
        <p><b>Kindly find your E-certificate for the same, attached along with this mail.<br>We look forward seeing you at all our future workshops, seminars and events!</b><p>
        <p><b>Regards<br>IEEE-VIT Student Branch</b></p>
        <div style="text-align:center">
            <p><b>Connect with us on</b></p>
            
            <a href="https://www.facebook.com/IEEEVIT1"><img src="https://www.bworldonline.com/wp-content/uploads/2020/08/f_logo_RGB-Hex-Blue_512.png" height="45" width="45"></img></a>
            
            <a href="https://www.instagram.com/ieeevit/?hl=en"><img src="https://static01.nyt.com/images/2016/05/11/us/12xp-instagram/12xp-instagram-facebookJumbo-v2.jpg" height="55" width="100"></img></a>
            
            <a href="https://ieee.vit.edu.in/"><img src="https://ieee.vit.edu.in/assets/images/ieeevit-blue-1-5017x1103.png" height="55" width="100"></img></a>
            <p><b>Ask us anything about programming, meet like minded people, build projects.</b></p>
            <p><b>Join the coders Republic Group now:</b></p>
            <a href="https://chat.whatsapp.com/GNjVY5fSZav73fl77vGPj2"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/WhatsApp_logo-color-vertical.svg/600px-WhatsApp_logo-color-vertical.svg.png" height="50" width="50"></img></a>
            <p><b>For any error in certificate <a>click here</a></b></p>
        </div>
        <img src="cid:{image_cid}">
    </body>
    </html>
    """ 
    msg.attach(MIMEText(body, 'html'))  
    filename = name
    #add your path
    attachment = open(f'D:\Shubham\shubham\Cert_&_emails_python\workshop1\{filename}', "rb")
    # attachment1 = open(f"D:\Shubham\shubham\Python_udemy\workshop\Workshop_Codes", "rb")
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read())
    # p.set_payload((attachment1).read())
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # p.add_header('Content-Disposition', "attachment1; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "saviosavio") 
# *Your Email password*
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 

df = pd.read_csv("cert1.csv")
for i in range(len(df)):
    name = df.iloc[i,0]
    email = df.iloc[i,1]
    # createCertificate(name)
    sendMail(name, email)