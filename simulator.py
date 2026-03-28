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

#10. Always check if register 0 is being updated. If x0 is the destination register do nothing.


from io import TextIOWrapper

traceList = []

pc = 0 #PC is always updated by +4

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
                
def signExt(immString:str, funcType:str) -> str:
        """
        #Isolate the immediate bits put them in CORRECT ORDER and then pass it as an argument as string.
        
        #try-catch for ValueError and ZeroDivisonError when using signExt()
        
        #Only pass the IMMEDIATE BINARY not THE ENTIRE INSTRUCTION.
"""
        result_imm = ""
        
        if(funcType.upper() == "I" or funcType.upper() == "S"):
                result_imm = (21*immString[0]) + immString[1:]

        
        elif(funcType.upper() == "B"):
                result_imm = (19*immString[0]) + immString[1:] + "0"

        elif(funcType.upper() == "U"):
                result_imm = immString + (12*"0")
        
        elif(funcType.upper() == "J"):
                result_imm = (12*immString[0]) + immString[1:] + "0"

        else:
                raise ZeroDivisionError

        return result_imm

def memory(memInt:int) -> str:        
        mem = "0x" + format((memInt & 0xFFFFFFFF), "08x").upper()
        if mem not in memStates:
                raise ZeroDivisionError
        return mem

def RType(binString:str):
        global pc
        global regStates
        global regStates
        global instructions

        pass

def IType(binString:str):
        global pc
        global regStates
        global memStates
        global instructions

        funct3 = binString[-15:-12]
        opcode = binString[-7:]
        imm = signExt(binString[-32:-20], "I")
        rs1 = binString[-20:-15]
        rd = binString[-12:-7]

        rs1 = int(rs1,2)
        rd = int(rd,2)

        if(rd not in regStates or rs1 not in regStates):
                raise ZeroDivisionError

        if opcode == "0000011" and funct3 == "010":
                operation = "lw"
        elif opcode == "0010011" and funct3 == "000":
                operation = "addi"
        elif opcode == "0010011" and funct3 == "011":
                operation = "sltiu"
        elif opcode == "1100111" and funct3 == "000":
                operation = "jalr"
        else:
                raise ZeroDivisionError
        
        match operation:
                case "addi":
                        if rd == 0:
                                return
                        
                        num1 = int(imm, 2) if (imm[0] == "0") else int(imm, 2) - (2**32)
                        num2 = regStates.get(rs1)
                        sum = num1 + num2
                        sum = format(sum & 0xFFFFFFFF, "032b")
                        valrd = int(sum[-32:], 2) if (sum[-32] == "0") else int(sum[-32:], 2) - (2**32)
                        regStates[rd] = valrd

                case "sltiu":
                        if rd == 0:
                                return
                        
                        num1 = int(imm, 2)
                        num2 = regStates.get(rs1) & 0xFFFFFFFF
                        valrd = 1 if num2 < (num1) else 0
                        regStates[rd] = valrd
                
                case "lw":
                        if rd == 0:
                                return
                        
                        val = regStates.get(rs1)
                        offset = int(imm,2) if (imm[0] == "0") else int(imm, 2) - (2**32)
                        mem_add = memory(val+offset)
                        valrd = memStates.get(mem_add)
                        regStates[rd] = valrd
                
                case "jalr":
                        regStates[rd] = pc + 4 if (rd!=0) else 0
                        val = regStates.get(rs1)
                        offset = int(imm,2) if (imm[0]=="0") else int(imm,2) - (2**32)
                        
                        new_pc = val + offset
                        new_pc = new_pc & 0xFFFFFFFE
                        new_pc= new_pc & 0xFFFFFFFF
                        
                        if(new_pc // 4 >= len(instructions)):
                                raise ZeroDivisionError
                        else:
                                pc = new_pc
                
                case _:
                        raise ZeroDivisionError
                
        return




def SType(binstring:str):

        global pc
        global regStates
        global memStates
        global instructions

        funct3=binstring[-15:-12]
        imm1=binstring[-32:25]
        imm2=binstring[-12:-7]

        imm=imm1+imm2

        rs2=binstring[-25:-20]
        rs1=binstring[-20:-15]

        inst1=int(rs1,2)
        inst2=int(rs2,2)


        if(inst1 not in regStates or inst2 not in regStates):
                raise ZeroDivisionError
        
        if funct3=="010":
                inst_="sw"
        else :
                raise ZeroDivisionError
        
        val1=regStates.get(inst1)
        val2=regStates.get(inst2)

        imm_value=signExt("0b"+imm,"S")

        value= int(imm_value,2)

        if(imm_value[2]=="0"):
                offset=value
        else:
                offset=value-2**32

        memory_=memory(val1+offset)

        if memory_ not in memStates:
                raise ZeroDivisionError
        # else 
        memStates[memory_]=val2
        

def BType(binString:str):
        global pc
        global regStates
        global memStates
        global instructions
        
        pass

def UType(binString:str):
        global pc
        global regStates
        global memStates
        global instructions
        
        if binString[-12:-7] == "00000":
                return
        
        opcode = binString[-7:]
        
        match opcode:
                case "0110111":
                        rd = binString[-12:-7]
                        imm = binString[:-12]
                        temp = int(imm, 2)
                        if temp > 524287:
                                raise ZeroDivisionError

                        imm = signExt(imm, "U")
                        imm = int(imm, 2) if (imm[0] == "0") else int(imm, 2) - (2**32)
                        rd = int(rd, 2)
                        
                        if rd not in regStates:
                                raise ZeroDivisionError

                        regStates[rd] = imm


                case "0010111":
                        pass
                case _:
                        raise ZeroDivisionError
        


def JType(binString:str):
        global pc
        global regStates
        global memStates
        global instructions
        
        pass

def writeRegStates(): #this function will write onto a list
        global regStates
        global pc
        trace = ""
        
        pcValue = format(pc, "032b") + " "
        trace += pcValue

        regValue = ""
        for i in range(32):
                regValue = format(regStates.get(i) & 0xFFFFFFFF, "032b")
                trace += regValue + " "
        traceList.append(trace)

def writeMemStates():
        global memStates
        global traceList

        memValue = ""
        for i in sorted(memStates.keys()):
                memValue = format(memStates.get(i) & 0xFFFFFFFF, "032b")
                traceList.append(i + ":" + memValue)

def main():
        """
        1. Have an index variable which always computes pc//4 in the while loop
            1a. pc increments by 4 every iteration of the while loop.
        2. Check for last instruction to be halt, if not exit with error
            2a. If halt encountered exit loop.
        3. Do things.
        4. Write traceList (and \n) after no errors and halt has been encountered.

        """
        pass

# remove pass after function is created
if __name__ == "__main__":
        main()
