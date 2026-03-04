# 1. Use the following format for Instruction type overall
#       Eg: "I" -> I-Type, etc.

# 2. Call signExt() whenever you get an immediate
#       Eg: imm = signExt(imm)

# 3. All binary values need be read imm[2:]
#       Reason: Binary strings start wtih unneccesary "0b"

# 4. Break instruction into words using .split()

# 5. For errors in any type raise ZeroDivisonError and catch it in main()

# 6. Start all binary strings with "0b" followed by 0s and 1s to keep the format same overall.

#7. call corr() to remove commas

def convert(inst:str) -> str:
        instType = checkType(inst)

        match(instType.upper()):
                case "R":
                        binInst = rType(inst)
                case "I":
                        binInst = iType(inst)
                case "S":
                        binInst = sType(inst)
                case "B":
                        binInst = bType(inst)
                case "U":
                        binInst = uType(inst)
                case "J":
                        binInst = jType(inst)
                case _:
                        raise ZeroDivisionError

def checkType(inst:str):
        pass

def signExt(binString:str, funcType:str) -> str:
        """
        Isolate the immediate bits put them in CORRECT ORDER and then pass it as an argument as string.
        
        try-catch for ValueError and ZeroDivisonError when using signExt()
        
        Only pass the IMMEDIATE BINARY not THE ENTIRE INSTRUCTION.
        """
        result_imm = ""
        
        
        if(funcType.upper() == "R"):
                raise ValueError
        
        elif(funcType.upper() == "I" or funcType.upper() == "S"):
                result_imm = "0b" + (20*binString[2]) + binString[2:]

        
        elif(funcType.upper() == "B"):
                result_imm = "0b" + (19*binString[2]) + binString[2:] + "0"

        elif(funcType.upper() == "U"):
                result_imm = binString + (12*"0")
        
        elif(funcType.upper() == "J"):
                result_imm = "0b" + (12*binString[2]) + binString[3:] + "0"

        else:
                raise ZeroDivisionError

        return result_imm

def rType(inst:str) -> str:
        pass

def iType(inst:str) -> str:
        pass

def sTypr(inst:str) -> str:
        pass

def bType(inst:str) -> str:
        pass

def sType(inst:str):
        pass

def uType(inst:str) -> str:
        inst = inst.split()
        binInst = ""
        match(inst[0]):
                case "lui":
                        opcode = "0110111"
                case "auipc":
                        opcode = "0010111"
                case _:
                        raise ZeroDivisionError
        
        rd = corr(inst[1])
        rd = int(rd[2:])
        
        if rd > 31 and rd < 0:
                raise ZeroDivisionError
        else:
                rd = bin(rd)
        
        imm = inst[2]
        imm = signExt(imm, "J")

        return binInst

def jType(inst:str) -> str:
        pass

def corr(string:str) -> str:
        while(string[-1] == ","):
                string  = string[:-1]
        return string
        
def main():

        for i in range(0):
                instruction = instruction.lower() #After input lower all case
                try:
                        binInstruction = convert(instruction)
                        
                        #Write binary string onto file
                
                except ZeroDivisionError:
                        print("You encountered an error on line", i)


        pass   

#Please remove pass after the function has been built
if __name__ == "__main__":
        main()
