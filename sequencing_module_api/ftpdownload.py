import getopt
import getpass
import os
import sys
import time 

from ftplib import FTP


interval = 0.05
serveur  = ''
user = ''
password = ''



# if __name__ == "__main__":

#     # Remove 1st argument from the
#     # list of command line arguments
#     argumentList = sys.argv[1:]
    
#     # Options
#     options = "u:h:s:d:"
    
#     # Long options
#     long_options = ["host","user", "source", "dest"]
    
#     try:
#         # Parsing argument
#         arguments, values = getopt.getopt(argumentList, options, long_options)
#         print(arguments)
        
#         # checking each argument
#         for currentArgument, currentValue in arguments:
    
#             if currentArgument in ("-h", "--host"):
#                 serveur = currentValue
                
#             elif currentArgument in ("-u", "--user"):
#                 user = currentValue
                
#             elif currentArgument in ("-s", "--source"):
#                 source = currentValue
            
#             elif currentArgument in ("-d", "--dest"):
#                 destination = currentValue
                
#     except getopt.error as err:
#         # output error, and return with an error code
#         print (str(err))

#     try:
#         password = getpass.getpass()
#     except Exception as error:
#         print('ERROR', error)
    
#     print("printing arguments " )
#     print(serveur)
#     print(user)
#     print(password)
#     print(destination)
    
#     ftp = FTP(serveur)
#     ftp.login(user, password)
#     ftp.encoding = "utf-8"

#     os.chdir(destination)
#     os.system("wget -r  -np -nH ftp://{user}:{password}@{serveur}{source}".format(user=user, password=password, serveur=serveur, source=source))
# #downloadFiles(source,dest)


def sendfile(serveur, user, password, source, destination= ".") :
    ftp = FTP(serveur)
    ftp.login(user, password)
    ftp.encoding = "utf-8"
    
    os.chdir(destination)
    os.system("wget -r  -np -nH ftp://{user}:{password}@{serveur}{source}".format(user=user, password=password, serveur=serveur, source=source))


