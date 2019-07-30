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

def create_tree_list(connection_ftp, folder_list,path = '/'):
    for folder in folder_list:
        browse_directory(connection_ftp,folder)
        create_folder_list(list(map(lambda var: connection_ftp.pwd()+'/' + var, connection_ftp.nlst())), path)
        download_all_archives(connection_ftp, path)
        browse_directory(connection_ftp,'..')

def verify_nc(archive_list):
    contains_nc = list(filter(lambda x: '.nc' in x, folder_list))  # Faz uma lista com todos os arquivos.nc
    if not (len(contains_nc) == 0):  # se existe um arquivo nc, chegamos nas folhas dos diretorios
        return download_all_archives(connection_ftp)

def browse_directory(connection_ftp, path):
    connection_ftp.cwd(path)

def download_all_archives(connection_ftp, path = '/'):
    for folder in connection_ftp.nlst():
        browse_directory(connection_ftp,folder)
        for file in connection_ftp.nlst():
            ftp.retrbinary("RETR " + file ,open(path +connection_ftp.pwd() +'/' + file, "wb").write)
        browse_directory(connection_ftp, '..')


#executando
print('Informe um caminho para a raiz do diretorio')
path = input()
create_folder_list(['archive'],path)
ftp,folder_list = conect_amrc()
create_folder_list(folder_list,path + '/archive')
create_tree_list(ftp,folder_list,path)
