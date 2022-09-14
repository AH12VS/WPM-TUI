class Data_CED():
    def __init__(self):

        self.normal_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.normal_lwcs_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                                 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.normal_upcs_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                                 "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.normal_sym = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                           ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        self.bin_num = ["0", "00", "000", "0000", "00000", "000000", "0000000", "00000000", "000000000",
                        "0000000000"]

        self.bin_lwcs_char = ["01", "001", "0001", "00001", "000001", "0000001", "00000001",
                              "000000001", "0000000001", "00000000001", "000000000001", "0000000000001", "00000000000001",
                              "000000000000001", "0000000000000001", "00000000000000001", "000000000000000001",
                              "0000000000000000001", "00000000000000000001", "000000000000000000001",
                              "0000000000000000000001", "00000000000000000000001", "000000000000000000000001",
                              "0000000000000000000000001", "00000000000000000000000001", "000000000000000000000000001"]

        self.bin_upcs_char = ["011", "0011", "00011", "000011", "0000011", "00000011", "000000011",
                              "0000000011", "00000000011", "000000000011", "0000000000011", "00000000000011",
                              "000000000000011", "0000000000000011", "00000000000000011", "000000000000000011",
                              "0000000000000000011", "00000000000000000011", "000000000000000000011",
                              "0000000000000000000011", "00000000000000000000011", "000000000000000000000011",
                              "0000000000000000000000011", "00000000000000000000000011", "000000000000000000000000011",
                              "0000000000000000000000000011"]

        self.bin_sym = ["0111", "00111", "000111", "0000111", "00000111", "000000111", "0000000111",
                        "00000000111", "000000000111", "0000000000111", "00000000000111", "000000000000111",
                        "0000000000000111", "00000000000000111", "000000000000000111", "0000000000000000111",
                        "00000000000000000111", "000000000000000000111", "0000000000000000000111",
                        "00000000000000000000111", "000000000000000000000111", "0000000000000000000000111",
                        "00000000000000000000000111", "000000000000000000000000111", "0000000000000000000000000111",
                        "00000000000000000000000000111", "000000000000000000000000000111",
                        "0000000000000000000000000000111", "00000000000000000000000000000111",
                        "000000000000000000000000000000111", "0000000000000000000000000000000111", "00000000000000000000000000000000111"]

        self.split = "1001"

    def normal_to_bin(self, normal_val):
        self.bin_list = list()
        self.val = str(normal_val)
        for index in range(len(self.val)):

            if self.val[index] in self.normal_num:
                self.val_index = self.normal_num.index(self.val[index])
                self.bin_val = self.bin_num[self.val_index]
                self.bin_list.append(self.bin_val+self.split)

            if self.val[index] in self.normal_lwcs_char:
                self.val_index = self.normal_lwcs_char.index(self.val[index])
                self.bin_val = self.bin_lwcs_char[self.val_index]
                self.bin_list.append(self.bin_val+self.split)

            if self.val[index] in self.normal_upcs_char:
                self.val_index = self.normal_upcs_char.index(self.val[index])
                self.bin_val = self.bin_upcs_char[self.val_index]
                self.bin_list.append(self.bin_val+self.split)

            if self.val[index] in self.normal_sym:
                self.val_index = self.normal_sym.index(self.val[index])
                self.bin_val = self.bin_sym[self.val_index]
                self.bin_list.append(self.bin_val+self.split)

        self.joined_bin = "".join(self.bin_list)
        return self.joined_bin

    def bin_to_normal(self, joined_bin):
        self.res_list = list()
        self.b_list = joined_bin.split("1001")

        for b_val in self.b_list:

            if b_val in self.bin_num:
                self.b_val_index = self.bin_num.index(b_val)
                self.normal_val = self.normal_num[self.b_val_index]
                self.res_list.append(self.normal_val)

            if b_val in self.bin_lwcs_char:
                self.b_val_index = self.bin_lwcs_char.index(b_val)
                self.normal_val = self.normal_lwcs_char[self.b_val_index]
                self.res_list.append(self.normal_val)

            if b_val in self.bin_upcs_char:
                self.b_val_index = self.bin_upcs_char.index(b_val)
                self.normal_val = self.normal_upcs_char[self.b_val_index]
                self.res_list.append(self.normal_val)

            if b_val in self.bin_sym:
                self.b_val_index = self.bin_sym.index(b_val)
                self.normal_val = self.normal_sym[self.b_val_index]
                self.res_list.append(self.normal_val)

        self.res = "".join(self.res_list)
        return self.res


if __name__ == "__main__":
    import time
    while True:
        commands_list = ["C", "c", "E", "e", 'Q', 'q']
        inh_obj = Data_CED()
        print(f"+{80*'-'}+")
        time.sleep(0.2)
        print(f"|    select your mode[C/E/Q]{53*' '}|")
        time.sleep(0.15)
        print(f"|    C -> Code | E -> Encode | Q -> Quit{41*' '}|")
        time.sleep(0.15)
        cond_for_select_mode = input("     >>> ")
        time.sleep(0.15)
        if cond_for_select_mode not in commands_list:
            free_space_after_cond_for_select_work = 57 - \
                len(cond_for_select_mode)
            print(
                f"|    The {cond_for_select_mode} is not defiend{free_space_after_cond_for_select_work*' '}|")
            time.sleep(0.15)
        if cond_for_select_mode == "C" or cond_for_select_mode == "c":
            inp_val = input("     >>> ")
            time.sleep(0.15)
            res = inh_obj.normal_to_bin(inp_val)
            len_res = 76-len(res)
            print(f"|    {res}{len_res*' '}|")
            time.sleep(0.15)
        if cond_for_select_mode == "E" or cond_for_select_mode == "e":
            inp_val = input("     >>> ")
            time.sleep(0.15)
            res = inh_obj.bin_to_normal(inp_val)
            len_res = 76-len(res)
            print(f"|    {res}{len_res*' '}|")
            time.sleep(0.15)
        if cond_for_select_mode in ['Q', 'q']:
            print(f"+{80*'-'}+")
            time.sleep(0.2)
            break
