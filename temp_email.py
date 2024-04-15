from mailtm import Email
import time
import os
import colorama
colorama.init()

def listener(message):
    sub=message["subject"]
    text=message["text"]
    sender_email=message['from']['address']
    listener_email=message['to'][0]['address']
    id_m=message['id']
    current_dir = "C:/Users/toart/Documents/Importantly/NET-Porgramming"
    final_dir = os.path.join(current_dir, 'all_mails')

    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    mail_file_path = os.path.join(final_dir, f'{id_m}.txt')

    with open(mail_file_path, 'w', encoding='utf-8') as file:
        file.write(f'Sender: {sender_email}\nTo: {listener_email}\nSubject: {sub}\nContent: {text}')
    
    print("\nSubject: " + sub)
    print("Content: " + text if text else message["html"])

test=Email()
print("\nDomain: " + test.domain)

test.register()
print("\nEmail Address: " + str(test.address))

try:
    test.start(listener, interval=1)
    while True:
        print(f"Waiting for new emails...", end='\r')
        time.sleep(1)
except(KeyboardInterrupt):
    test.stop()
    test.delete()
