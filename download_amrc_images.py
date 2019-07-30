from ftplib import FTP
import os
import os.path

def conect_amrc():
    ftp = FTP('amrc.ssec.wisc.edu') #Acessa o servidor
    ftp.login() #faz o login, mesmo quando não existe usuario
    ftp.cwd('archive') # Entra no diretorio arquivo
    folder_list = [folder for folder in ftp.nlst() if len(folder) == 4]  # seleciona apenas as pastas dos anos
    return ftp, folder_list

def create_folder_list(folder_list, path = '/'):
    for folder in folder_list:
        if not( os.path.exists(path + '/'+folder)):
            os.mkdir(path + '/'+folder)

def verify_nc(archive_list):
    contains_nc = list(filter(lambda x: '.nc' in x, folder_list))  # Faz uma lista com todos os arquivos.nc
    if not (len(contains_nc) == 0):  # se existe um arquivo nc, chegamos nas folhas dos diretorios
        return download_all_archives(connection_ftp)

def download_all_archives(connection_ftp):
    archives = connection_ftp.nlst() #pega lista com todos os arquivos
    for archive in archives:
        download_archive(connection_ftp, archive)
    return (connection_ftp.cwd('..'))

def browse_directory(connection_ftp, path):
    connection_ftp.cwd(path)



def download_image(connection_ftp):
    pass


#executando
print('Informe um caminho para a raiz do diretorio')
path = input()
ftp,folder_list = conect_amrc()
create_folder_list(folder_list,path + '/archive')
for folder in folder_list:
    print((folder))
    browse_directory(ftp,folder)
    print((ftp))
    create_folder_list(ftp.nlst(), path)

