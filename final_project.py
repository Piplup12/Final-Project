#https://www.youtube.com/watch?v=JRCJ6RtE3xU
import smtplib #modul python untuk connect dengan email
import imghdr #modul untuk mengirim gambar
from email.message import EmailMessage #import modul untuk mengirim pesan

msg = EmailMessage()
msg['Subject'] = 'hello'
msg ['From'] = "python.project.bp@gmail.com"
msg ['To'] = 'python.project.bp@gmail.com'
msg.set_content ('how are you')

files = ['Screenshot (28).png', 'Screenshot (29).png']
for file in files: #loop untuk mengirim lebih dari 1 gambar
    with open(file, 'rb') as f: #untuk open file, rb untuk read binary files
        file_data = f.read() #dibaca
        file_type = imghdr.what(f.name) #untuk menentukan tipe file 
        file_name = f.name #untuk nama file yang dikirim
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name) #untuk di add ke emailnya

files2 = ['CV Joshua.pdf']
for file in files2: #loop lebih dari 1 file
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #pakai class smtp_ssl dan smtp.gmail untuk konek dgn gmail, port number=465 untuk SSL
    smtp.login("python.project.bp@gmail.com", "ffzfvyvlmynnvdsv") 
    smtp.send_message(msg)
