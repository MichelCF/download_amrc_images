from ftplib import FTP
import os
import os.path

def conect_amrc():
    ftp = FTP('amrc.ssec.wisc.edu') #Acessa o servidor
    ftp.login() #faz o login, mesmo quando não existe usuario
    ftp.cwd('archive') # Entra no diretorio arquivo
    return ftp



def folders(connection_ftp,path = '/work'):
    list_folders = connection_ftp.nlst() #pega o nome de todos os diretorios dentro do arquivo
    if connection_ftp.pwd() == 'archive':
        list_folders =[folder for folder in list_folders if len(folder) == 4] # seleciona apenas as pastas dos anos
    contains_nc = list(filter(lambda x: '.nc' in x, list_folders)) #Faz uma lista com todos os arquivos.nc
    if not(len(contains_nc) == 0):#se existe um arquivo nc, chegamos nas folhas dos diretorios
        if not(os.path.exists(path + connection_ftp.pwd())):
            os.mkdir(path + connection_ftp.pwd())#Cria o diretorio apenas se ele não existir
        return download_all_archives(connection_ftp)
    else:
        for name_folder in list_folders:
            if not(os.path.exists(path + connection_ftp.pwd())):
                os.mkdir(path + connection_ftp.pwd())#Cria o diretorio apenas se ele não existir
            connection_ftp = entry_folders(connection_ftp, name_folder)
            return folders(connection_ftp) #Faz a recursão para percorrer todos os diretorios



def download_all_archives(connection_ftp):
    archives = connection_ftp.nlst() #pega lista com todos os arquivos
    for archive in archives:
        download_archive(connection_ftp, archive)
    return (connection_ftp.cwd('..'))




def download_image(connection_ftp):
    pass




def entry_folders(connection_ftp, name_folder):
    connection_ftp.cwd(name_folder)
    folders(connection_ftp)
    connection_ftp.cwd('..')
    return connection_ftp

#executando
ftp = conect_amrc()
folders(ftp)
