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

                self.passwd = self.passwd_1+self.passwd_2+self.passwd_3+self.passwd_4+self.passwd_5

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

                self.passwd = self.passwd_1+self.passwd_2+self.passwd_3+self.passwd_4+self.passwd_5+self.passwd_6

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
            print("Please enter the password")
            time.sleep(0.15)
            print('Please enter the pasword without using ":" and grater than 3 and less than 61')
            time.sleep(0.3)
            self.passwd = input(">>> ")
            if ":" in self.passwd and len(self.passwd) > 3 and len(self.passwd) < 61:
                self.recommended_passwd = self.passwd.replace(":", f"{all[random.randint(0, len(all))]}")
                while self.recommended_passwd in saved_passwd_value:
                    self.recommended_passwd = self.passwd.replace(":", f"{all[random.randint(0, len(all))]}")
                    if self.recommended_passwd not in saved_passwd_value:
                        break
                print(f'can not save "{self.passwd}" cause ":" is in that')
                time.sleep(0.15)
                print(f'Are you want to use "{self.recommended_passwd}" (it is recommended ) ?[y/N]')
                time.sleep(0.15)
                self.cond_for_use_recommended_passwd = input(">>> ")
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
                print("Please enter a password grater than 3")
                time.sleep(0.15)

            if len(self.passwd) >= 61:
                print("Please enter a number less than 61")
                time.sleep(0.15)

            if self.passwd in saved_passwd_value:
                print(f"This password : {self.passwd} is used before")
                time.sleep(0.15)
                print("Are you sure you want to use this password [y/N]")
                cond_for_save_reuse_passwd = input(">>> ")
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
        print("**************************************************")
        time.sleep(0.15)
        print("**********")
        time.sleep(0.15)
        if len(saved_passwd) == 0:
            print("There is no password found")
            time.sleep(0.15)
            print("**********")
            time.sleep(0.15)
        for passwd in saved_passwd:
            if len(passwd) > 0:
                print(passwd)
                time.sleep(0.15)
                print("**********")
                time.sleep(0.15)

class F_Mode():
    def __init__(self):
        pass

class P_Mode():
    def __init__(self):
        pass

class R_Mode():
    def __init__(self):
        pass

class E_Mode():
    def __init__(self):
        pass
