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
    usr_passwd_file = "w"
if "passwd_user" in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
    usr_passwd_file = "r"

# condition for read the passwd_user file
if usr_passwd_file == "r":
    with open(f"{user_workspace_dir}/Documents/WPM/passwd_user", usr_passwd_file) as p_f:
        for p_l in p_f:
            p_l = p_l.splitlines()
            for p_f_l in p_l:
                if p_f_l not in user_passwd:
                    enc_to_normal = ced_inh_obj.bin_to_normal(p_f_l) # encode the data
                    user_passwd.append(enc_to_normal)

# condition for make passwd_user file
if usr_passwd_file == "w":
    with open(f"{user_workspace_dir}/Documents/WPM//passwd_user", usr_passwd_file) as p_f:
        pass

if len(user_passwd) == 1: # check if length of user_passwd not equal 0 (be any data in that)
    print("Please enter your password")
    time.sleep(0.3)
    user_passwd_for_login = input(">>> ") # get the input of user for open the software
    while user_passwd_for_login != user_passwd[0]: # loop work if user input not equal the real and true password
        print(f'The "{user_passwd_for_login} is incorrect"')
        time.sleep(0.15)
        print("Please enter your password")
        time.sleep(0.3)
        user_passwd_for_login = input(">>> ")

print("")
time.sleep(0.15)
print("WELCOME")
time.sleep(0.15)
print("")


# main loop
while True:

    # variables for save the all data and refresh that every time
    saved_passwd = list()
    saved_passwd_name = list()
    saved_passwd_value = list()

    # condition for make the folder
    if os.path.exists(f"{user_workspace_dir}/Documents") == False:
        os.mkdir(f"{user_workspace_dir}/Documents")
    if os.path.exists(f"{user_workspace_dir}/Documents/WPM/") == False:
        os.mkdir(f"{user_workspace_dir}/Documents/WPM/")

    # condition for make or read passwd_data file
    if "passwd_data" not in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
        file_mode = "w"
    if "passwd_data" in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
        file_mode = "r"

    # condition for make or read passwd_user file
    if "passwd_user" not in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
        usr_passwd_file = "w"
    if "passwd_user" in os.listdir(f"{user_workspace_dir}/Documents/WPM/"):
        usr_passwd_file = "r"

    # condition for read passwd_data file
    if file_mode == "r":
        with open(f"{user_workspace_dir}/Documents/WPM/passwd_data", file_mode) as f:
            for l in f:
                l = l.splitlines()
                for line in l:
                    enc_data = ced_inh_obj.bin_to_normal(line)
                    if enc_data not in saved_passwd:
                        saved_passwd.append(enc_data)

    # condition for make passwd_data file
    if file_mode == "w":
        with open(f"{user_workspace_dir}/Documents/WPM/passwd_data", file_mode) as f:
            pass

    # condition for read passwd_user file
    if usr_passwd_file == "r":
        with open(f"{user_workspace_dir}/Documents/WPM/passwd_user", usr_passwd_file) as p_f:
            for p_l in p_f:
                p_l = p_l.splitlines()
                for p_f_l in p_l:
                    if p_f_l not in user_passwd:
                        user_passwd.append(p_f_l)

    # condition for make passwd_user file
    if usr_passwd_file == "w":
        with open(f"{user_workspace_dir}/Documents/WPM/passwd_user", usr_passwd_file) as p_f:
            pass

    # iterate on saved_passwd variable and split the name of password and add them to saved_passwd_name variable
    for data in saved_passwd:
        if len(data) > 0:
            name = data.split(":")[0]
            if name not in saved_passwd_name:
                saved_passwd_name.append(name)

    # iterate on saved_passwd variable and split the password and add them to saved_passwd_value variable
    for data in saved_passwd:
        if len(data) > 0:
            try:
                val = data.split(":")[1]
                if val not in saved_passwd_value:
                    saved_passwd_value.append(val)
            except:
                pass


    # show the modes
    print("**************************************************")
    time.sleep(0.15)
    print("[N] Input New Password")
    time.sleep(0.15)
    print("[A] Show All Passwords")
    time.sleep(0.15)
    print("[F] Find Password")
    time.sleep(0.15)
    print("[P] Set Password")
    time.sleep(0.15)
    print("[I] Information")
    time.sleep(0.15)
    print("[R] Remove")
    time.sleep(0.15)
    print("[E] Edit")
    time.sleep(0.15)
    print("[H] Help")
    time.sleep(0.15)
    print("[Q] Quit")
    time.sleep(0.15)
    time.sleep(0.3)

    cond_for_work = input(">>> ") # get input for choose a mode

    # if user input a undefined  command
    if cond_for_work not in commands_list:
        print("**********")
        time.sleep(0.15)
        print(f'There is no "{cond_for_work}" command.')
        time.sleep(0.15)
        print("**********")
        time.sleep(0.15)
        print("You can use This commands:")
        time.sleep(0.15)
        print("**********")


    if cond_for_work in ["N", "n"]:
        file_mode = "a"
        print("**************************************************")
        time.sleep(0.15)
        print("Please Enter the Name of Password")
        time.sleep(0.15)
        input_passwd_name = input(">>> ") # get name of password name of user
        time.sleep(0.15)
        print("**************************************************")
        time.sleep(0.15)
        # check if user input name in saved_passwd_name
        while input_passwd_name in saved_passwd_name :
            print("**********")
            time.sleep(0.15)
            print("This name is used before")
            time.sleep(0.15)
            print("**********")
            time.sleep(0.15)
            print("This names are used before : ")
            time.sleep(0.15)
            print("**********")
            time.sleep(0.15)
            # loop to show the all password names
            for n in saved_passwd_name:
                print(n)
                time.sleep(0.15)
                print("**********")
                time.sleep(0.15)
            print("**************************************************")
            time.sleep(0.15)
            print("Please Enter the Name of Password")
            time.sleep(0.15)
            input_passwd_name = input(">>> ") # get the user input for new name for the password
            time.sleep(0.15)
            print("**************************************************")
            time.sleep(0.15)
            # check (for break the loop)
            if input_passwd_name not in saved_passwd_name:
                break

        # check if ":" in user input name of password do not use that
        while ":" in input_passwd_name:
            print('Please enter the password name without ":"')
            time.sleep(0.15)
            input_passwd_name = input(">>> ") # get user input again for name of password
            # check if user input name in saved_passwd_name
            while input_passwd_name in saved_passwd_name :
                print("**********")
                time.sleep(0.15)
                print("This name is used before")
                time.sleep(0.15)
                print("**********")
                time.sleep(0.15)
                print("This names are used before : ")
                time.sleep(0.15)
                print("**********")
                time.sleep(0.15)
                # loop to show the all password names
                for n in saved_passwd_name:
                    print(n)
                    time.sleep(0.15)
                    print("**********")
                    time.sleep(0.15)
                print("**************************************************")
                time.sleep(0.15)
                print("Please Enter the Name of Password")
                time.sleep(0.15)
                input_passwd_name = input(">>> ") # get the user input for new name for the password
                time.sleep(0.15)
                print("**************************************************")
                time.sleep(0.15)
                # check for break the loop
                if input_passwd_name not in saved_passwd_name:
                    break
            # check for break the loop
            if ":" not in input_passwd_name:
                break

        # check if length of user input name be equal 0
        while len(input_passwd_name) == 0:
            print("The password name can not be empty")
            time.sleep(0.15)
            input_passwd_name = input(">>> ") # get passwod again
            # check if ":" in user input name of password do not use that
            while ":" in input_passwd_name:
                print('Please enter the password name without ":"')
                time.sleep(0.15)
                input_passwd_name = input(">>> ") # get user input again for name of password
                # check if user input name in saved_passwd_name
                while input_passwd_name in saved_passwd_name :
                    print("**********")
                    time.sleep(0.15)
                    print("This name is used before")
                    time.sleep(0.15)
                    print("**********")
                    time.sleep(0.15)
                    print("This names are used before : ")
                    time.sleep(0.15)
                    print("**********")
                    time.sleep(0.15)
                    # loop to show the all password names
                    for n in saved_passwd_name:
                        print(n)
                        time.sleep(0.15)
                        print("**********")
                        time.sleep(0.15)
                    print("**************************************************")
                    time.sleep(0.15)
                    print("Please Enter the Name of Password")
                    time.sleep(0.15)
                    input_passwd_name = input(">>> ")  # get the user input for new name for the password
                    time.sleep(0.15)
                    print("**************************************************")
                    time.sleep(0.15)
                    # check (for break the loop)
                    if input_passwd_name not in saved_passwd_name:
                        break
                # check (for break the loop)
                if ":" not in input_passwd_name:
                    break
            # check (for break the loop)
            if len(input_passwd_name) != 0:
                break

        # show the methods of N_Mode
        time.sleep(0.15)
        print("Please select mode (default : A):")
        time.sleep(0.15)
        print("[A]/[N]/[C]/[S]/[M]")
        time.sleep(0.15)
        print('"A" for make password use numbers, charcters and symbols ((Strong)')
        time.sleep(0.15)
        print('"N" for make password only use numbers (Poor)')
        time.sleep(0.15)
        print('"C" for make password only use characters (Average)|(better than "N")')
        time.sleep(0.15)
        print('"S" for make password only use symbols (Good)|(better than "C")')
        time.sleep(0.15)
        print('"M" for make password manually')
        time.sleep(0.3)

        cond_for_select_mk_passwd = input(">>> ") # user input for choose a method

        # check if user input not in methods of N_Mode
        while cond_for_select_mk_passwd not in ["A", "a", "N", "n", "C", "c", "S", "s", "M", "m"]:
            print("Please choose a mode in [A]/[N]/[C]/[S]/[M] modes")
            cond_for_select_mk_passwd = input(">>> ")
            if cond_for_select_mk_passwd in ["A", "a", "N", "n", "C", "c", "S", "s", "M", "m"]:
                break

        # check if user input in ["A", "a", "N", "n", "C", "c", "S", "s"] (and then get length of password)
        if cond_for_select_mk_passwd in ["A", "a", "N", "n", "C", "c", "S", "s"]:
            print("Please Enter the length of Password")
            time.sleep(0.15)
            print("Please Enter an Int number")
            time.sleep(0.15)
            print("Please enter a number grater than 3 and less than 61")
            time.sleep(0.3)
            # loop True for get the length of password
            while True:
                passwd_len = input(">>> ") # get user input for password length
                try:
                    passwd_len = int(passwd_len) # try to convert the passwd_len to integer
                except:
                    print("Please Enter an Int number")
                    time.sleep(0.15)

                if type(passwd_len) == type(0):

                    if passwd_len < 4:
                        print("Please enter a number grater than 3")
                        time.sleep(0.15)

                    if passwd_len >= 61:
                        print("Please enter a number less than 61")
                        time.sleep(0.15)

                    if passwd_len > 3 and passwd_len < 61:
                        break

        if cond_for_select_mk_passwd in ["A", "a"]:
            passwd = n_mode_functions_obj.a_method(all, passwd_len, saved_passwd_value)

        if cond_for_select_mk_passwd in ["N", "n"]:
            passwd = n_mode_functions_obj.n_method(numbers, passwd_len, saved_passwd_value)

        if cond_for_select_mk_passwd in ["C", "c"]:
            passwd = n_mode_functions_obj.c_method(characters, passwd_len, saved_passwd_value)

        if cond_for_select_mk_passwd in ["S", "s"]:
            passwd = n_mode_functions_obj.s_method(symbols, passwd_len, saved_passwd_value)

        if cond_for_select_mk_passwd in ["M", "m"]:
            passwd = n_mode_functions_obj.m_method(all, saved_passwd_value)

        print(f"{input_passwd_name}:{passwd}") # show the name of password and password

        # save the file
        with open(f"{user_workspace_dir}/Documents/WPM/passwd_data", file_mode) as f:
            code_to_bin = ced_inh_obj.normal_to_bin(f"{input_passwd_name}:{passwd}") # code the password name and password value
            f.write(code_to_bin)
            f.write("\n")

    if cond_for_work in ["A", "a"]:
        a_mode_functions_obj.a_method(saved_passwd)

    if cond_for_work in ["F", "f"]:
        f_mode_functions_obj.f_method(saved_passwd_name, saved_passwd_value)

    if cond_for_work in ["P", "p"]:
        cond_for_change_passwd = p_mode_functions_obj.p_method(user_passwd, ced_inh_obj, user_workspace_dir)
        if cond_for_change_passwd in ["N", "n"]:
            pass
        if cond_for_change_passwd in ["Y", "y"]:
            break

    if cond_for_work in ["I", "i"]:
        information.info()

    if cond_for_work in ["R", "r"]:
        print("**************************************************")
        time.sleep(0.15)
        if len(saved_passwd_name) == 0:
                print("There is no password for remove")
        if len(saved_passwd_name) > 0:
            print("Please choose the type: ")
            time.sleep(0.15)
            print('[RA]/[R] ("RA" for remove all passwords | "R" for remove a specific password)')
            cond_for_select_rm_mode = input(">>> ") # get user input for choose a method
        # condition for remove all data
        if cond_for_select_rm_mode in ["RA", "Ra", "rA", "ra"]:
            r_mode_functions_obj.ra_method(user_workspace_dir)
        # condition for remove any password with name of password
        if cond_for_select_rm_mode in ["R", "r"]:
            r_mode_functions_obj.r_method(saved_passwd_name, saved_passwd_value, ced_inh_obj, user_workspace_dir)
