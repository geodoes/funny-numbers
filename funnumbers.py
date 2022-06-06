
words = {
    "numbers": ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"],
    "tens": ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"],
    "hundreds": ['hundred', "thousand", "million", "billion"]
}

class Numbers():
    def __init__(self,number):
        self.number = number
    def __str__(self):

        return words["numbers"][int(self.number)]

class Decimals():
    def __init__(self,tens):
        self.tens = tens
    def __str__(self):
        tens_full = []
        for j in str(self.tens):
            tens_full.append(j)
        if [str(self.tens)][0].startswith("2"):
            return f"{words['tens'][0]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("3"):
            return f"{words['tens'][1]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("4"):
            return f"{words['tens'][2]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("5"):
            return f"{words['tens'][3]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("6"):
            return f"{words['tens'][4]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("7"):
            return f"{words['tens'][5]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("8"):
            return f"{words['tens'][6]}" + " " + f"{words['numbers'][int(tens_full[1])]}"
        if [str(self.tens)][0].startswith("9"):
            return f"{words['tens'][7]}" + " " + f"{words['numbers'][int(tens_full[1])]}"

class Hund():
    def __init__(self, hund_hund):
        self.hund_hund = hund_hund

    def __str__(self):
        hundreds_full = []
        for k in str(self.hund_hund):
            hundreds_full.append(k)

        def two_nums_from_list(a,b):
            return [a,b]
        AA = "".join(two_nums_from_list(hundreds_full[1],hundreds_full[2]))

        if hundreds_full[0].startswith("1"):
            if AA.startswith("0"):
                if AA == "00":
                    return f"{words['numbers'][1]} {words['hundreds'][0]} "
                return f"one hundred and {words['numbers'][int(AA)]}"
            if hundreds_full[1].startswith("1") and hundreds_full[2] != "0":
                return f"{words['numbers'][1]} {words['hundreds'][0]}" + " " + f"{words['numbers'][int(AA)]}"
            else:
                return f"{words['numbers'][1]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"

        if hundreds_full[0].startswith("2"):
            return f"{words['numbers'][2]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("3"):
            return f"{words['numbers'][3]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("4"):
            return f"{words['numbers'][4]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("5"):
            return f"{words['numbers'][5]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("6"):
            return f"{words['numbers'][6]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("7"):
            return f"{words['numbers'][7]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("8"):
            return f"{words['numbers'][8]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"
        if hundreds_full[0].startswith("9"):
            return f"{words['numbers'][9]} {words['hundreds'][0]} " + "and" + " " + f"{Decimals(int(AA))}"

class Thousands():
    def __init__(self,thous):
        self.thous = thous

    def __str__(self):
        thousands_full = []
        for l in str(self.thous):
            thousands_full.append(l)

        def tree_nums_from_list(a,b,c):
            return [a,b,c]
        BB = "".join(tree_nums_from_list(thousands_full[1],thousands_full[2],thousands_full[3]))

        if thousands_full[0].startswith("1"):
            return f"{words['numbers'][1]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("2"):
            return f"{words['numbers'][2]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("3"):
            return f"{words['numbers'][3]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("4"):
            return f"{words['numbers'][4]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("5"):
            return f"{words['numbers'][5]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("6"):
            return f"{words['numbers'][6]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("7"):
            return f"{words['numbers'][7]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("8"):
            return f"{words['numbers'][8]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"
        if thousands_full[0].startswith("9"):
            return f"{words['numbers'][9]} {words['hundreds'][1]} "  + f"{Hund(int(BB))}"

class DecimalThousands():
    def __init__(self, ten_thous):
        self.ten_thous = ten_thous

    def __str__(self):
        ten_thous_full = []
        for m in str(self.ten_thous):
            ten_thous_full.append(m)

        def tree_nums_from_list(a,b,c):
            return [b,c,d]
        CC = "".join(tree_nums_from_list(ten_thous_full[2],ten_thous_full[3],ten_thous_full[4]))

        def two_nums_from_four(aa,bb):
            return [aa,bb]
        CC_Firsts = ''.join(two_nums_from_four(ten_thous_full[0],ten_thous_full[1]))

        def last_two_nums(cc,dd):
            return [cc,dd]
        CC_Lasts = ''.join(last_two_nums(ten_thous_full[3],ten_thous_full[4]))

        if int(self.ten_thous) == 10000:
            return "ten thousand"
        if int(CC) <= 19:
            return f"{Numbers(int(CC_Firsts))} {words['hundreds'][1]} {Hund(int(CC))}"



# class Millions():
#     def __init__(self,million):
#         self.million = million
#
#     def __str__(self):
#         millions_full = []
#         for m in str(self.million):
#             millions_full.append(m)
#
#         def four_nums_from_list(a,b,c,d):
#             return [a,b,c,d]
#         BB = "".join(four_nums_from_list(millions_full[1],millions_full[2],millions_full[3],millions_full[4]))
#
#         if millions_full[0].startswith("1"):
#             return f"{words['numbers'][1]} {words['hundreds'][2]}" + f"{Thousands(int(BB))}"

def main(user_input):
    if int(user_input) <= 19:
        NN = Numbers(int(user_input))
        print(NN.__str__())

    if int(user_input) >= 19 and len(user_input) == 2:
        DD = Decimals(user_input)
        print(DD.__str__())

    if int(user_input) >= 100 and len(user_input) <= 3:
        HH = Hund(user_input)
        print(HH.__str__())
    if int(user_input) >= 1000 and len(str(user_input)) == 4:
        TT = Thousands(user_input)
        print(TT.__str__())
    if int(user_input) >= 10000 and len(str(user_input)) == 5:
        TS = DecimalThousands(user_input)
        print(TS.__str__())
    # if int(user_input) >= 1000000 and len(str(user_input)) == 7:
    #     MM = Millions(user_input)
    #     print(MM.__str__())
if __name__ == '__main__':
    while True:
        main( user_input = input("chislo - "))
