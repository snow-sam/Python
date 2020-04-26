from instapy_cli import client

username = '_life.motivation' #your username
password = 'samucas5' #your password 

image = '20.jpg' 

text = 'Oi'

with client(username, password) as cli:
    cli.upload(image, text)


