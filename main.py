# 1. Use the following format for Instruction type overall
#       Eg: "I" -> I-Type, etc.

# 2. Call signExt() whenever you get an immediate
#       Eg: imm = signExt(imm)

# 3. All binary values need be read imm[2:]
#       Reason: Binary strings start wtih unneccesary "0b"

# 4. Break instruction into words using .split()

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
                        pass

def checkType(inst:str):
        pass

def signExt(funcType:str, binString:str) -> str:
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
                case "":
                        pass
        
        return binInst

def jType(inst:str) -> str:
        pass

def main():

        instruction = instruction.lower() #After input lower all case
        binInstruction = convert(instruction)
        pass   

#Please remove pass after the function has been built
if __name__ == "__main__":
        main()
