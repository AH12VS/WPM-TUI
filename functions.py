import time
import random


class N_Mode():

    def __init__(self):
        pass

    def a_method(self, all, passwd_len, saved_passwd_value):
        if passwd_len < 61:
            self.temp = random.sample(all, passwd_len)
            self.passwd = "".join(self.temp)
            while self.passwd in saved_passwd_value:
                self.temp = random.sample(all, passwd_len)
                self.passwd = "".join(self.temp)
                if self.passwd not in saved_passwd_value:
                    self.passwd = self.passwd
                else:
                    self.temp = random.sample(all, passwd_len)
                    self.passwd = "".join(self.temp)
        return self.passwd

    def n_method(self, numbers, passwd_len, saved_passwd_value):
        if passwd_len < 11:
            self.temp = random.sample(numbers, passwd_len)
            self.passwd = "".join(self.temp)
            while self.passwd in saved_passwd_value:
                self.temp = random.sample(numbers, passwd_len)
                self.passwd = "".join(self.temp)
                if self.passwd not in saved_passwd_value:
                    self.passwd = self.passwd
                else:
                    self.temp = random.sample(numbers, passwd_len)
                    self.passwd = "".join(self.temp)

        if passwd_len > 10:

            if passwd_len < 21:
                more_passwd_len = passwd_len-10
                self.temp_1 = random.sample(numbers, 10)
                self.passwd_1 = "".join(self.temp_1)

                self.temp_2 = random.sample(numbers, more_passwd_len)
                self.passwd_2 = "".join(self.temp_2)
                self.passwd = self.passwd_1+self.passwd_2

            if passwd_len > 20 and passwd_len < 31:
                more_passwd_len = passwd_len-20
                self.temp_1 = random.sample(numbers, 10)
                self.passwd_1 = "".join(self.temp_1)

                self.temp_2 = random.sample(numbers, 10)
                self.passwd_2 = "".join(self.temp_2)
                self.temp_3 = random.sample(numbers, more_passwd_len)
                self.passwd_3 = "".join(self.temp_3)

                self.passwd = self.passwd_1+self.passwd_2+self.passwd_3

            if passwd_len > 30 and passwd_len < 41:
                more_passwd_len = passwd_len-30
                self.temp_1 = random.sample(numbers, 10)
                self.passwd_1 = "".join(self.temp_1)

                self.temp_2 = random.sample(numbers, 10)
                self.passwd_2 = "".join(self.temp_2)
                self.temp_3 = random.sample(numbers, 10)
                self.passwd_3 = "".join(self.temp_3)

                self.temp_4 = random.sample(numbers, more_passwd_len)
                self.passwd_4 = "".join(self.temp_4)

                self.passwd = self.passwd_1+self.passwd_2+self.passwd_3+self.passwd_4

            if passwd_len > 40 and passwd_len < 51:
                more_passwd_len = passwd_len-40
                self.temp_1 = random.sample(numbers, 10)
                self.passwd_1 = "".join(self.temp_1)

                self.temp_2 = random.sample(numbers, 10)
                self.passwd_2 = "".join(self.temp_2)
                self.temp_3 = random.sample(numbers, 10)
                self.passwd_3 = "".join(self.temp_3)

                self.temp_4 = random.sample(numbers, 10)
                self.passwd_4 = "".join(self.temp_4)

                self.temp_5 = random.sample(numbers, 10)
                self.passwd_5 = "".join(self.temp_5)

                self.passwd = self.passwd_1+self.passwd_2 + \
                    self.passwd_3+self.passwd_4+self.passwd_5

            if passwd_len > 50 and passwd_len < 61:
                more_passwd_len = passwd_len-50
                self.temp_1 = random.sample(numbers, 10)
                self.passwd_1 = "".join(self.temp_1)

                self.temp_2 = random.sample(numbers, 10)
                self.passwd_2 = "".join(self.temp_2)
                self.temp_3 = random.sample(numbers, 10)
                self.passwd_3 = "".join(self.temp_3)

                self.temp_4 = random.sample(numbers, 10)
                self.passwd_4 = "".join(self.temp_4)

                self.temp_5 = random.sample(numbers, 10)
                self.passwd_5 = "".join(self.temp_5)

                self.temp_6 = random.sample(numbers, more_passwd_len)
                self.passwd_6 = "".join(self.temp_6)

                self.passwd = self.passwd_1+self.passwd_2+self.passwd_3 + \
                    self.passwd_4+self.passwd_5+self.passwd_6

        return self.passwd

    def c_method(self, characters, passwd_len, saved_passwd_value):
        if passwd_len < 53:
            self.temp = random.sample(characters, passwd_len)
            self.passwd = "".join(self.temp)
            while self.passwd in saved_passwd_value:
                self.temp = random.sample(characters, passwd_len)
                self.passwd = "".join(self.temp)
                if self.passwd not in saved_passwd_value:
                    self.passwd = self.passwd
                else:
                    self.temp = random.sample(characters, passwd_len)
                    self.passwd = "".join(self.temp)
        if passwd_len > 52:
            more_passwd_len = passwd_len-50
            self.temp_1 = random.sample(characters, 50)
            self.passwd_1 = "".join(self.temp_1)

            self.temp_2 = random.sample(characters, more_passwd_len)
            self.passwd_2 = "".join(self.temp_2)
            self.passwd = self.passwd_1+self.passwd_2

        return self.passwd

    def s_method(self, symbols, passwd_len, saved_passwd_value):
        if passwd_len < 31:
            self.temp = random.sample(symbols, passwd_len)
            self.passwd = "".join(self.temp)
            while self.passwd in saved_passwd_value:
                self.temp = random.sample(symbols, passwd_len)
                self.passwd = "".join(self.temp)
                if self.passwd not in saved_passwd_value:
                    self.passwd = self.passwd
                else:
                    self.temp = random.sample(symbols, passwd_len)
                    self.passwd = "".join(self.temp)

        if passwd_len > 31:
            more_passwd_len = passwd_len-30
            self.temp_1 = random.sample(symbols, 30)
            self.passwd_1 = "".join(self.temp_1)

            self.temp_2 = random.sample(symbols, more_passwd_len)
            self.passwd_2 = "".join(self.temp_2)
            self.passwd = self.passwd_1+self.passwd_2

        return self.passwd

    def m_method(self, all, saved_passwd_value):
        while True:
            print(f"|    Please enter the password{51*' '}|")
            time.sleep(0.15)
            print(
                f"|    Please enter the pasword without using \":\"{34*' '}|\n|        and grater than 3 and less than 61{38*' '}|")
            time.sleep(0.15)
            self.passwd = input("     >>> ")
            time.sleep(0.15)
            if ":" in self.passwd and len(self.passwd) > 3 and len(self.passwd) < 61:
                self.recommended_passwd = self.passwd.replace(
                    ":", f"{all[random.randint(0, len(all))]}")
                while self.recommended_passwd in saved_passwd_value:
                    self.recommended_passwd = self.passwd.replace(
                        ":", f"{all[random.randint(0, len(all))]}")
                    if self.recommended_passwd not in saved_passwd_value:
                        break
                self.free_space_after_self_passwd_1 = 61-len(self.passwd)
                print(
                    f"|    can not save \"{self.passwd}\"{self.free_space_after_self_passwd_1*' '}|\n|    cause \":\" is in that|{53*' '}")
                time.sleep(0.15)
                self.free_space_after_self_recommended_passwd = 70 - \
                    len(self.recommended_passwd)
                print(
                    f"|    Are you want to use{57*' '}|\n|        \"{self.recommended_passwd}\"{self.free_space_after_self_recommended_passwd*' '}|\n|            (it is recommended ) ?[y/N]{41*' '}|")
                time.sleep(0.15)
                self.cond_for_use_recommended_passwd = input("     >>> ")
                time.sleep(0.15)
                if self.cond_for_use_recommended_passwd in ["Y", "y", "N", "n"]:
                    pass
                else:
                    self.cond_for_use_recommended_passwd = "N"

                if self.cond_for_use_recommended_passwd in ["Y", "y"]:
                    self.passwd = self.recommended_passwd
                    break
                if self.cond_for_use_recommended_passwd in ["N", "n"]:
                    pass

            if len(self.passwd) < 4:
                print(f"|    Please enter a password grater than 3{39*' '}|")
                time.sleep(0.15)

            if len(self.passwd) >= 61:
                print(f"|    Please enter a number less than 61{42*' '}|")
                time.sleep(0.15)

            if self.passwd in saved_passwd_value:
                self.free_space_after_self_passwd_2 = 58-len(self.passwd)
                print(
                    f"|    This password : \"{self.passwd}\"{self.free_space_after_self_passwd_2*' '}|\n|        is used before{58*' '}|")
                time.sleep(0.15)
                print(
                    f"|    Are you sure you want to use this password [y/N]{28*' '}|")
                time.sleep(0.15)
                cond_for_save_reuse_passwd = input("     >>> ")
                time.sleep(0.15)
                if cond_for_save_reuse_passwd in ["Y", "y", "N", "n"]:
                    pass
                else:
                    cond_for_save_reuse_passwd = "N"
                if cond_for_save_reuse_passwd in ["N", "n"]:
                    pass
                if cond_for_save_reuse_passwd in ["Y", "y"]:
                    self.passwd = self.passwd
                    break
            if self.passwd not in saved_passwd_value and len(self.passwd) > 3 and len(self.passwd) < 61 and ":" not in self.passwd:
                break

        return self.passwd


class A_Mode():
    def __init__(self):
        pass

    def a_method(self, saved_passwd):
        print(f"+{80*'-'}+")
        time.sleep(0.2)
        print(f"|{80*'-'}|")
        time.sleep(0.15)
        if len(saved_passwd) == 0:
            print(f"|    There is no password found{50*' '}|")
            time.sleep(0.15)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
        for passwd in saved_passwd:
            if len(passwd) > 0:
                self.free_space_after_passwd_in_a_mode = 76-len(passwd)
                print(
                    f"|    {passwd}{self.free_space_after_passwd_in_a_mode*' '}|")
                time.sleep(0.15)
                print(f"|{80*'-'}|")
                time.sleep(0.15)
        print(f"+{80*'-'}+")
        time.sleep(0.2)


class F_Mode():
    def __init__(self):
        pass

    def f_method(self, saved_passwd_name, saved_passwd_value):
        print(f"|{80*'-'}|")
        time.sleep(0.15)
        print(f"|    Please Enter the Name{55*' '}|")
        time.sleep(0.15)
        print(f"|{80*'-'}|")
        time.sleep(0.15)
        self.find_passwd_name = input("     >>> ")
        time.sleep(0.15)
        if self.find_passwd_name in saved_passwd_name:
            self.name_index = saved_passwd_name.index(self.find_passwd_name)
            time.sleep(0.15)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            print(f"|    Name:Password{63*' '}|")
            time.sleep(0.15)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            self.free_space_after_name_and_passwd_in_f_mode = 75 - \
                (len(self.find_passwd_name) +
                 len(saved_passwd_value[self.name_index]))
            print(
                f"|    {self.find_passwd_name}:{saved_passwd_value[self.name_index]}{self.free_space_after_name_and_passwd_in_f_mode*' '}|")
            time.sleep(0.15)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
        if self.find_passwd_name not in saved_passwd_name:
            self.free_space_after_finded_passwd_for_show_in_f_mode = 56 - \
                len(self.find_passwd_name)
            print(
                f"|    No Item Match for \"{self.find_passwd_name}\"{self.free_space_after_finded_passwd_for_show_in_f_mode*' '}|")
            time.sleep(0.15)


class P_Mode():
    def __init__(self):
        pass

    def p_method(self, user_passwd, ced_inh_obj, user_workspace_dir):
        if len(user_passwd) == 0:
            print(f"|    Please enter your password to set{43*' '}|")
            time.sleep(0.15)
            self.input_user_passwd = input("     >>> ")
            time.sleep(0.15)
            self.free_space_after_self_input_user_passwd_in_p_mode = 56 - \
                len(self.input_user_passwd)
            print(
                f"|    Your password : {self.input_user_passwd} set{self.free_space_after_self_input_user_passwd_in_p_mode*' '}|")
            time.sleep(0.15)
            self.code_to_bin_usr_passwd = ced_inh_obj.normal_to_bin(
                self.input_user_passwd)
            with open(f"{user_workspace_dir}/Documents/WPM/passwd_user", "w") as f:
                f.write(self.code_to_bin_usr_passwd)
                f.write("\n")
            print(f"|    Please start the software again{45*' '}|")
            time.sleep(0.15)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            print(f"|    Have a Nice Day!{60*' '}|")
            time.sleep(0.5)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            self.cond_for_change_passwd = "Y"
        if len(user_passwd) > 1:
            print(f"|    Wanna change your password?[N/y]{44*' '}|")
            time.sleep(0.15)
            try:
                self.cond_for_change_passwd = input("     >>> ")
                time.sleep(0.15)
            except:
                self.cond_for_change_passwd = "N"

            if self.cond_for_change_passwd == "Y" or self.cond_for_change_passwd == "y":
                print(f"|    Please enter your password{50*' '}")
                time.sleep(0.15)
                self.user_passwd_before_change = input("     >>> ")
                time.sleep(0.15)

                if self.user_passwd_before_change == user_passwd[0]:
                    print(
                        f"|    Please enter the new password to set{40*' '}|")
                    time.sleep(0.15)
                    self.new_user_passwd = input("     >>> ")
                    time.sleep(0.15)
                    self.free_space_after_self_new_user_passwd_in_p_mode = 49*' '
                    print(
                        f"|    Your new password \"{self.new_user_passwd}\" is set")
                    time.sleep(0.15)
                    self.code_to_bin_usr_passwd = ced_inh_obj.normal_to_bin(
                        self.new_user_passwd)
                    with open(f"{user_workspace_dir}/Documents/WPM/passwd_user", "w") as f:
                        f.write(self.code_to_bin_usr_passwd)
                        f.write("\n")
                    print(f"|    Please start the software again{45*' '}|")
                    time.sleep(0.15)
                    print(f"|{80*'-'}|")
                    time.sleep(0.15)
                    print(f"|    Have a Nice Day!{60*' '}|")
                    time.sleep(0.5)
                    print(f"|{80*'-'}|")
                    time.sleep(0.15)
                if self.user_passwd_before_change != user_passwd[0]:
                    self.free_space_after_self_user_passwd_before_change_in_p_mode = 57 - \
                        len(self.user_passwd_before_change)
                    print(
                        f"|    The \"{self.user_passwd_before_change}\" is incorrect{self.free_space_after_self_user_passwd_before_change_in_p_mode*' '}|")
                    time.sleep(0.15)
        return self.cond_for_change_passwd


class R_Mode():
    def __init__(self):
        pass

    def ra_method(self, user_workspace_dir):
        print(f"|    Are you sure to remove all the data?[N/y]{35*' '}|")
        time.sleep(0.15)
        self.cond_for_remove_all_data = input("     >>> ")
        time.sleep(0.15)
        if self.cond_for_remove_all_data not in ["Y", "y", "N", "n"]:
            self.cond_for_remove_all_data = "N"
        if self.cond_for_remove_all_data in ["Y", "y"]:
            with open(f"{user_workspace_dir}/Documents/WPM/passwd_data", "w") as f:
                f.write("")
        if self.cond_for_remove_all_data in ["N", "n"]:
            pass

    def r_method(self, saved_passwd_name, saved_passwd_value, ced_inh_obj, user_workspace_dir):
        print(f"|    Please enter the Name for remove{44*' '}|")
        time.sleep(0.15)
        print(f"|{80*'-'}|")
        time.sleep(0.15)
        self.find_passwd_name = input("     >>> ")
        time.sleep(0.15)
        if self.find_passwd_name in saved_passwd_name:
            self.name_index = saved_passwd_name.index(self.find_passwd_name)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            print(
                f"|    Are you want to remove this name and password?[N/y]{25*' '}|")
            time.sleep(0.15)
            self.cond_for_remove = input("     >>> ")
            time.sleep(0.15)
            if self.cond_for_remove not in ["Y", "y", "N", "n"]:
                self.cond_for_remove = "N"
            if self.cond_for_remove in ["Y", "y"]:
                with open(f"{user_workspace_dir}/Documents/WPM/passwd_data", "r+") as f_n:
                    self.new_f = f_n.readlines()
                    f_n.seek(0)
                    for line_n in self.new_f:
                        self.find_bin_passwd = ced_inh_obj.normal_to_bin(
                            f"{self.find_passwd_name}:{saved_passwd_value[self.name_index]}")
                        if self.find_bin_passwd not in line_n:
                            f_n.write(line_n)
                    f_n.truncate()
        if self.find_passwd_name not in saved_passwd_name:
            self.free_space_after_self_find_passwd_name_in_r_mode = 56 - \
                len(self.find_passwd_name)
            print(
                f"|    No Item Match for \"{self.find_passwd_name}\"{self.free_space_after_self_find_passwd_name_in_r_mode*' '}|")
            time.sleep(0.15)


class E_Mode():
    def __init__(self):
        pass

    def e_method(self, saved_passwd_name, saved_passwd_value, ced_inh_obj, user_workspace_dir):
        print(f"|{80*'-'}|")
        time.sleep(0.15)
        print(
            f"|    Please enter the name of password you want edit that{24*' '}|")
        time.sleep(0.15)
        self.passwd_name_for_edit = input("     >>> ")
        time.sleep(0.15)
        if self.passwd_name_for_edit not in saved_passwd_name:
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            self.free_space_after_self_passwd_name_for_edit_in_e_mode = 49 - \
                len(self.passwd_name_for_edit)
            print(
                f"|    \"{self.passwd_name_for_edit}\" is not in password names{self.free_space_after_self_passwd_name_for_edit_in_e_mode*' '}|")
            time.sleep(0.15)
            print(f"|{80*'-'}|")
            time.sleep(0.15)
        if self.passwd_name_for_edit in saved_passwd_name:
            print(f"|{80*'-'}|")
            time.sleep(0.15)
            print(f"|    Please enter the new password name{42*' '}|")
            time.sleep(0.15)
            self.new_passwd_name = input("     >>> ")
            time.sleep(0.15)
            while self.new_passwd_name in saved_passwd_name:
                print(f"|{80*'-'}|")
                time.sleep(0.15)
                print(f"|    This name is used before{52*' '}|")
                time.sleep(0.15)
                print(f"|{80*'-'}|")
                time.sleep(0.15)
                print(f"|    This names are used before : {47*' '}|")
                time.sleep(0.15)
                print(f"|{80*'-'}|")
                time.sleep(0.15)
                for n in saved_passwd_name:
                    self.free_space_after_n_in_e_mode = 76-len(n)
                    print(f"|    {n}{self.free_space_after_n_in_e_mode*' '}|")
                    time.sleep(0.15)
                    print(f"|{80*'-'}|")
                    time.sleep(0.15)
                print(f"|{80*'-'}|")
                time.sleep(0.15)
                print(f"|    Please Enter the Name of Password{43*' '}|")
                time.sleep(0.15)
                self.new_passwd_name = input("     >>> ")
                time.sleep(0.15)
                print(f"|{80*'-'}|")
                time.sleep(0.15)
                if self.new_passwd_name not in saved_passwd_name:
                    break
            self.bin_data_before_change = ced_inh_obj.normal_to_bin(
                f"{self.passwd_name_for_edit}:{saved_passwd_value[saved_passwd_name.index(self.passwd_name_for_edit)]}")
            self.bin_data_to_edit = ced_inh_obj.normal_to_bin(
                f"{self.new_passwd_name}:{saved_passwd_value[saved_passwd_name.index(self.passwd_name_for_edit)]}")
            self.free_space_after_self_passwd_name_for_edit_in_e_mode = 44 - \
                len(self.passwd_name_for_edit)
            self.free_space_after_self_new_passwd_name_in_e_mode = 61 - \
                len(self.new_passwd_name)
            print(
                f"|    are you sure you want to change {self.passwd_name_for_edit}{self.free_space_after_self_passwd_name_for_edit_in_e_mode*' '}|\n|        to{70*' '}|\n|            {self.new_passwd_name}? [N/y]{self.free_space_after_self_new_passwd_name_in_e_mode*' '}|")
            time.sleep(0.15)
            self.cond_for_change_passwd_name = input("     >>> ")
            time.sleep(0.15)
            if self.cond_for_change_passwd_name in ["Y", "y", "N", "n"]:
                pass
            else:
                self.cond_for_change_passwd_name = "N"

            if self.cond_for_change_passwd_name in ["Y", "y"]:
                fin = open(
                    f"{user_workspace_dir}/Documents/WPM/passwd_data", "rt")
                self.data = fin.read()
                fin.close()
                self.data = self.data.replace(
                    self.bin_data_before_change, self.bin_data_to_edit)
                fin = open(
                    f"{user_workspace_dir}/Documents/WPM/passwd_data", "wt")
                fin.write(self.data)
                fin.close()
                self.free_space_after_self_bin_data_to_edit_in_e_mode = 62 - \
                    len(ced_inh_obj.bin_to_normal(self.bin_data_to_edit))
                print(
                    f"|    New password: {ced_inh_obj.bin_to_normal(self.bin_data_to_edit)}{self.free_space_after_self_bin_data_to_edit_in_e_mode*' '}|")
                time.sleep(0.15)
            if self.cond_for_change_passwd_name in ["N", "n"]:
                pass
