from ftplib import *
ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario = ''
senha = ''
ftp.login(usuario, senha)
print('Diretorio atual de trabalho: ',ftp.pwd())
ftp.quit