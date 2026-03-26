#1. For any functions requiring immediate exted the immediate by passing the required parameters in the signExt()
#   function.

#2. As done in assembler extraction of opcode will give the type of the function and the task.

#3. For functions with funct7 and funct3 differentiating between instructions, create an internal dictionary within
#   the function type.

#4. Check for errors and raise ZeroDivisionError, whenever an error is encountered.


opcodes = {
        "0110011" : "R",
        "0000011" : "I",
        "0010011" : "I",
        "1100111" : "I",
        "0100011" : "S",
        "1100011" : "B",
        "0110111" : "U",
        "0010111" : "U",
        "1101111" : "J"
}



def signExt(binString:str, funcType:str) -> str:
        """
        #Isolate the immediate bits put them in CORRECT ORDER and then pass it as an argument as string.
        
        #try-catch for ValueError and ZeroDivisonError when using signExt()
        
        #Only pass the IMMEDIATE BINARY not THE ENTIRE INSTRUCTION.
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

def Rtype():
        pass

def Itype():
        pass

def Stype():
        pass

def Btype():
        pass

def Utype():
        pass

def Jtype():
        pass

def main():
        return

# remove pass after function is created
if __name__ == "__main__":
        main()
