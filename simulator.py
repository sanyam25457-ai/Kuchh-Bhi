#1. For any functions requiring immediate exted the immediate by passing the required parameters in the signExt()
#   function.

#2. As done in assembler extraction of opcode will give the type of the function and the task.

#3. For functions with funct7 and funct3 differentiating between instructions, create an internal dictionary within
#   the function type.

#4. Check for errors and raise ZeroDivisionError, whenever an error is encountered.

#5. Every binary string will go through the execute() function and be called respectively if no general errors
#   are found.

#6. Always update register state using the registerStates dictionary.

#7. For any jump or branch instructions update the pc (after saving the next pc in required jump instructions).

#8. Update corresponding memory by accessing dictionary of memStates.

#9. After getting the memory to update from binary string, use memory() function to get the key of the
#   corresponding memory in the memStates dictionary.

pc = 4 #PC is always updated by +4

instructions=[]

errors = {}

errMSG = {}

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

regStates = {
        0 :  0,
        1 :  0,
        2 :  0,
        3 :  0,
        4 :  0,
        5 :  0,
        6 :  0,
        7 :  0,
        8 :  0,
        9 :  0,
        10 : 0,
        11 : 0,
        12 : 0,
        13 : 0,
        14 : 0,
        15 : 0,
        16 : 0,
        17 : 0,
        18 : 0,
        19 : 0,
        20 : 0,
        21 : 0,
        22 : 0,
        23 : 0,
        24 : 0,
        25 : 0,
        26 : 0,
        27 : 0,
        28 : 0,
        29 : 0,
        30 : 0,
        31 : 0,

}

memStates = {
        "0x00010000" : 0,
        "0x00010004" : 0,
        "0x00010008" : 0,
        "0x0001000C" : 0,
        "0x00010010" : 0,
        "0x00010014" : 0,
        "0x00010018" : 0,
        "0x0001001C" : 0,
        "0x00010020" : 0,
        "0x00010024" : 0,
        "0x00010028" : 0,
        "0x0001002C" : 0,
        "0x00010030" : 0,
        "0x00010034" : 0,
        "0x00010038" : 0,
        "0x0001003C" : 0,
        "0x00010040" : 0,
        "0x00010044" : 0,
        "0x00010048" : 0,
        "0x0001004C" : 0,
        "0x00010050" : 0,
        "0x00010054" : 0,
        "0x00010058" : 0,
        "0x0001005C" : 0,
        "0x00010060" : 0,
        "0x00010064" : 0,
        "0x00010068" : 0,
        "0x0001006C" : 0,
        "0x00010070" : 0,
        "0x00010074" : 0,
        "0x00010078" : 0,
        "0x0001007C" : 0
}

def execute(binString:str):
        if len(binString) > 32:
                raise ZeroDivisionError
        opcode = binString[-7:]
        funcType = opcodes.get(opcode)

        match(funcType):
                case "R":
                        RType(binString)
                case "I":
                        IType(binString)
                case "S":
                        SType(binString)
                case "B":
                        BType(binString)
                case "U":
                        UType(binString)
                case "J":
                        JType(binString)
                case _:
                        raise ZeroDivisionError
                
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

def memory(memInt:int) -> str:        
        mem = "0x" + format((memInt & 0xFFFFFFFF), "08x").upper()
        if mem not in memStates:
                raise ZeroDivisionError
        return mem

def RType():
        global pc
        global regStates
        global regStates

        pass

def IType(binString:str):
        global pc
        global regStates
        global memStates
        global instructions

        funct3=binString[-15:-12]
        opcode=binString[-7:]
        imm=signExt("0b"+binString[-32:-20])
        rs1=binString[-20:-15]
        rd=binString[-12:-7]

        intrs1=int(rs1,2)
        intrd=int(rd,2)

        if(intrd not in regStates or intrs1 not in regStates):
                raise ZeroDivisionError

        if opcode=="0000011"and funct3=="010":
                instn="lw"
        elif opcode=="0010011" and funct3=="000":
                instn="addi"
        elif opcode=="0010011" and funct3=="011":
                instn="sltiu"
        elif opcode=="1100111" and funct3=="000":
                instn="jalr"
        else:
                raise ZeroDivisionError
        
        match instn:
                case "addi":
                        if(intrd==0):
                                return
                        num1=int(imm,2) if imm[2]=="0" else int(imm,2)-2**32
                        num2=regStates.get(intrs1)
                        sum=num1+num2
                        sum=format(sum & 0xFFFFFFFF,"032b")
                        valrd=int(sum[-32:],2) if sum[-32]=="0" else int(sum[-32:],2)-2**32
                        regStates[intrd]=valrd

                case "sltiu":
                        if intrd==0:
                                return
                        num1=int(imm,2)
                        num2=regStates.get(intrs1) & 0xFFFFFFFF
                        valrd=1 if num2<(num1) else 0
                        regStates[intrd]=valrd
                
                case "lw":
                        if intrd==0:
                                return
                        val=regStates.get(intrs1)
                        offset=int(imm,2) if imm[2]=="0" else int(imm,2)-2**32
                        mem_add=memory(val+offset)
                        if mem_add not in memStates:
                                raise ZeroDivisionError
                        valrd=memStates.get(mem_add)
                        regStates[intrd]=valrd
                
                case "jalr":
                        regStates[intrd]=pc+4 if intrd!=0 else 0
                        val=regStates.get(intrs1)
                        offset=int(imm,2) if imm[2]=="0" else int(imm,2)-2**32
                        new_pc=val+offset
                        new_pc=new_pc & 0xFFFFFFFE
                        new_pc= new_pc & 0xFFFFFFFF
                        if(new_pc//4 >= len(instructions)):
                                raise ZeroDivisionError
                        else:
                                pc=new_pc
                
                case _:
                        raise ZeroDivisionError


def SType():
        global pc
        global regStates
        global memStates
        
        pass

def BType():
        global pc
        global regStates
        global memStates
        
        pass

def UType():
        global pc
        global regStates
        global memStates
        
        pass

def JType():
        global pc
        global regStates
        global memStates
        
        pass

def writeRegStates(): #this function will write onto a list and the list will be appended to a list (2D List)
        pass

def main():
        pass

# remove pass after function is created
if __name__ == "__main__":
        main()
