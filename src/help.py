import time


def help():
    print(f"+{80*'-'}+")
    time.sleep(0.2)
    print(f"""|{80*' '}|
| ███    ██{70*' '}|
| ████   ██{70*' '}|
| ██ ██  ██{70*' '}|
| ██  ██ ██{70*' '}|
| ██   ████ Mode:{64*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(f"|      [N] Mode is for make and save password{36*' '}|")
    time.sleep(0.15)
    print(f"|      First you need to enter the password name{33*' '}|")
    time.sleep(0.15)
    print("|          Password name must not be used before, \"-\", Please Do not use \":\" in  |")
    time.sleep(0.15)
    print(f"|{18*' '}password name{49*' '}|")
    time.sleep(0.15)
    print("|      You can choose diffrent methods to make a password",
          "-", "[A]/[N]/[C]/[S]/[M]  |")
    time.sleep(0.15)
    print(
        "|      You need to enter the password length if your are not use [M] method      |")
    time.sleep(0.15)
    print("|          By default it is 8", "-",
          "You can not enter a number less than 4           |")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|      █████{69*' '}|
|     ██   ██{68*' '}|
|     ███████{68*' '}|
|     ██   ██{68*' '}|
|     ██   ██ Method:{60*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print("|          [A] -> (All) Method is for make password near use uppercase           |\n"
          "|                        letters-lowercase letters-numbers-symbols -> (Strong)   |")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|     ███    ██{66*' '}|
|     ████   ██{66*' '}|
|     ██ ██  ██{66*' '}|
|     ██  ██ ██{66*' '}|
|     ██   ████ Method:{58*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(
        "|          [N] -> (Numbers) Method is for make password use numbers -> (Poor)    |")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|      ██████{68*' '}|
|     ██{73*' '}|
|     ██{73*' '}|
|     ██{73*' '}|
|      ██████ Method:{60*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print("|          [C] -> (Characters) Method is for make password use uppercase letters |\n"
          "|                       and lowercase letters -> ((Average)|(better than [N]))   |")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|     ███████{68*' '}|
|     ██{73*' '}|
|     ███████{68*' '}|
|          ██{68*' '}|
|     ███████ Method:{60*' '}|
| 									         |""")
    time.sleep(0.15)
    print("|          [S] -> (Symbols) Method is for make password use symbols              |\n"
          "|                        -> ((Good)|(better than [C]))                           |")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|     ███    ███{65*' '}|
|     ████  ████{65*' '}|
|     ██ ████ ██{65*' '}|
|     ██  ██  ██{65*' '}|
|     ██      ██ Method:                                                         |
|{80*' '}|""")
    time.sleep(0.15)
    print(
        "|          [M] -> (Manually) Method is for make password with user input         |")
    time.sleep(0.15)
    print(
        f"|              If you use manually method please do not use \":\"{18*' '}|")
    time.sleep(0.15)

    print(f"""|{80*' '}|
| ███████{72*' '}|
| ██{77*' '}|
| █████{74*' '}|
| ██{77*' '}|
| ██ Mode:{71*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(f"|      [F] Mode is for find password{45*' '}|")
    time.sleep(0.15)
    print(
        f"|      you can find password values with enter the password name{17*' '}|")
    time.sleep(0.15)

    print(f"""|{80*' '}|
| ██████{73*' '}|
| ██   ██{72*' '}|
| ██████{73*' '}|
| ██{77*' '}|
| ██ Mode:{71*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(
        "|     [P] Mode is for set pasword on this software for make more privacy         |")
    time.sleep(0.15)

    print(f"""|{80*' '}|
| ██{77*' '}|
| ██{77*' '}|
| ██{77*' '}|
| ██{77*' '}|
| ██ Mode:{71*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(f"|      [I] Mode is for show software information{33*' '}|")
    time.sleep(0.15)
    print(f"""|{80*' '}|
| ██████{73*' '}|
| ██   ██{72*' '}|
| ██████{73*' '}|
| ██   ██{72*' '}|
| ██   ██ Mode:{66*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(f"|      [R] Mode is for remove passwords{42*' '}|")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|     ██████{69*' '}|
|     ██   ██{68*' '}|
|     ██████{69*' '}|
|     ██   ██{68*' '}|
|     ██   ██ Method:{60*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(
        f"|          [R] Method is for remove a password with password name{16*' '}|")
    time.sleep(0.15)
    print(f"""|{80*' '}|
|     ██████   █████{61*' '}|
|     ██   ██ ██   ██{60*' '}|
|     ██████  ███████{60*' '}|
|     ██   ██ ██   ██{60*' '}|
|     ██   ██ ██   ██ Method:                                                    |
|{80*' '}|""")

    time.sleep(0.15)
    print(f"|          [RA] Method is for remove all password{32*' '}|")
    time.sleep(0.15)

    print(f"""|{80*' '}|
| ███████{72*' '}|
| ██{77*' '}|
| █████{74*' '}|
| ██{77*' '}|
| ███████ Mode:{66*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(f"|      [E] Mode is for edit password names{39*' '}|")
    time.sleep(0.15)
    print(
        f"|      you can edit the password names with enter that and{23*' '}|\n|{16*' '}new name you want to set{40*' '}|")
    time.sleep(0.15)
    print(
        f"|      Password name must not be used before, \"-\",{31*' '}|\n|{18*' '}Please Do not use \":\" in password name{24*' '}|")
    time.sleep(0.15)

    print(f"""|{80*' '}|
|  ██████{72*' '}|
| ██    ██{71*' '}|
| ██    ██{71*' '}|
| ██ ▄▄ ██{71*' '}|
|  ██████{72*' '}|
|     ▀▀   Mode:{65*' '}|
|{80*' '}|""")
    time.sleep(0.15)
    print(f"|      [Q] Mode is for quit the software{41*' '}|")
    time.sleep(0.15)
    print(f"+{80*'-'}+")
    time.sleep(0.2)


if __name__ == "__main__":
    help()
