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