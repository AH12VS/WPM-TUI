# import libraries
import string
import time
import os
import banner
import CED as ced
import functions
import information
import help

# show the intro of software
banner.banner()

# make inheritance of each class
ced_inh_obj =  ced.Data_CED()
n_mode_functions_obj = functions.N_Mode()
a_mode_functions_obj = functions.A_Mode()
f_mode_functions_obj = functions.F_Mode()
p_mode_functions_obj = functions.P_Mode()
r_mode_functions_obj = functions.R_Mode()
e_mode_functions_obj = functions.E_Mode()

# list of commands
commands_list = ["N", "n", "A", "a", "F", "f", "P", "p", "I", "i", "R", "r", "E", "e", "H", "h", "Q", "q"]

numbers = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
symbols = string.punctuation
symbols = symbols.replace(":", "")
characters = lowercase_letters+uppercase_letters
all = numbers+lowercase_letters+uppercase_letters+symbols


user_workspace_dir = os.path.expanduser("~") # get user workspace directory

user_passwd = list() # save all password with name

# condition for make the folder
if os.path.exists(f"{user_workspace_dir}/Documents") == False:
    os.mkdir(f"{user_workspace_dir}/Documents")
if os.path.exists(f"{user_workspace_dir}/Documents/WPM/") == False:
    os.mkdir(f"{user_workspace_dir}/Documents/WPM/")

# condition for make or read passwd_user file
if "passwd_user" not in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
    usr_passwd_file = "w" # for make file
if "passwd_user" in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
    usr_passwd_file = "r" # for read file
