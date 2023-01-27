
def f(a):
    if a < 0:
        return -a
    else:
        return a

def arithmetic_arranger(tab,calculable=False):
    answers1 = ""
    answers2 = ""
    answers4 = ""
    answers5 = ""
    if len(tab) > 5 :
        return "Error: Too many problems."
    else:
        for j,i in enumerate(tab):
            op1,op,op2 = i.split(" ")
            if op not in ('-','+'):
                return "Error: Operator must be '+' or '-'."
            elif op1.isdigit()!=True or op2.isdigit()!=True:
                return "Error: Numbers must only contain digits."
            elif max(len(op1),len(op2)) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                if op == '+':
                    result = str(int(op1) + int(op2))
                else:
                    result = str(int(op1) - int(op2))
                if len(op1) > len(op2):
                    if len(result) > len(op1):
                        if j < len(tab)-1:
                            answers1 += "  {}    ".format(op1)
                            answers2 += "{}{}{}    ".format(op," "*int(f(len(op1)-len(op2))+1),op2)
                            answers4 += "{}    ".format("-"*(len(op1)+2))
                            answers5 += "{}{}   ".format(" ",result)
                        else:
                            answers1 += "  {}".format(op1)
                            answers2 += "{}{}{}".format(op," "*int(f(len(op1)-len(op2))+1),op2)
                            answers4 += "{}".format("-"*(len(op1)+2))
                            answers5 += "{}{}".format(" ",result)
                    else:
                        if j < len(tab)-1:
                            answers1 +="  {}    ".format(op1)
                            answers2 +="{}{}{}    ".format(op," "*int(f(len(op1)-len(op2))+1),op2)
                            answers4 += "{}    ".format("-"*(len(op1)+2))
                            answers5 += "{}{}    ".format("  ",result)
                        else:
                            answers1 +="  {}".format(op1)
                            answers2 +="{}{}{}".format(op," "*int(f(len(op1)-len(op2))+1),op2)
                            answers4 += "{}".format("-"*(len(op1)+2))
                            answers5 += "{}{}".format("  ",result)
                else:
                    if len(result) > len(op2):
                        if j < len(tab)-1:
                            answers1 += "{}{}    ".format(" "*int(f(len(op1)-len(op2))+2),op1)
                            answers2 += "{} {}    ".format(op,op2)
                            answers4 += "{}    ".format("-"*(len(op2)+2))
                            answers5 += "{}{}    ".format(" ",result)
                        else:
                            answers1 += "{}{}".format(" "*int(f(len(op1)-len(op2))+2),op1)
                            answers2 += "{} {}".format(op,op2)
                            answers4 += "{}".format("-"*(len(op2)+2))
                            answers5 += "{}{}".format(" ",result)
                    else:
                        if j < len(tab)-1:
                            answers1 +="{}{}    ".format(" "*int(f(len(op1)-len(op2))+2),op1)
                            answers2 +="{} {}    ".format(op,op2)
                            answers4 += "{}    ".format("-"*(len(op2)+2))
                            answers5 += "{}{}    ".format(" "*int(f(len(result)-len(op2))+2),result)
                        else:
                            answers1 +="{}{}".format(" "*int(f(len(op1)-len(op2))+2),op1)
                            answers2 +="{} {}".format(op,op2)
                            answers4 += "{}".format("-"*(len(op2)+2))
                            answers5 += "{}{}".format(" "*int(f(len(result)-len(op2))+2),result)
        if calculable:
            return "{}\n{}\n{}\n{}".format(answers1,answers2,answers4,answers5)
        else:
            return "{}\n{}\n{}".format(answers1,answers2,answers4)
def calculate(liste):
    try:
        if len(liste) < 9:
            raise ValueError("List must contain nine numbers.")
    except ValueError as e:
        return e
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(calculate([1,2,8,7,9,4,4,5]))


                            