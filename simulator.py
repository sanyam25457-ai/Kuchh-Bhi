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

import sys

jump = False

traceList = []

pc = 0 #PC is always updated by +4

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
        binString = binString.strip()

        if len(binString) > 32:
                raise ZeroDivisionError
        elif len(binString) == 0:
                return
        
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
        if memInt % 4 != 0:
                raise ZeroDivisionError
           
        mem = "0x" + format((memInt & 0xFFFFFFFF), "08x").upper()
        if mem not in memStates:
                raise ZeroDivisionError
        return mem

def RType(binString:str):
        global pc
        global regStates
        global regStates

        #To be made
        pass

def IType(binString:str):
        global pc
        global regStates
        global memStates
        global jump

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
                        
                        if not(valrd < 2**32 and valrd >= -(2**32)):
                                raise ZeroDivisionError
                        regStates[rd] = valrd

                case "sltiu":
                        if rd == 0:
                                return
                        
                        num1 = int(imm, 2)
                        num2 = regStates.get(rs1) & 0xFFFFFFFF
                        valrd = 1 if num2 < (num1) else 0
                        
                        if not(valrd < 2**32 and valrd >= -(2**32)):
                                raise ZeroDivisionError
                        regStates[rd] = valrd
                
                case "lw":
                        if rd == 0:
                                return
                        
                        val = regStates.get(rs1)
                        offset = int(imm,2) if (imm[0] == "0") else int(imm, 2) - (2**32)
                        mem_add = memory(val+offset)
                        valrd = memStates.get(mem_add)
                        
                        if not(valrd < 2**32 and valrd >= -(2**32)):
                                raise ZeroDivisionError
                        regStates[rd] = valrd
                                
                
                case "jalr":
                        regStates[rd] = pc if (rd!=0) else 0
                        val = regStates.get(rs1)
                        offset = int(imm,2) if (imm[0]=="0") else int(imm,2) - (2**32)
                        
                        new_pc = val + offset
                        new_pc = new_pc & 0xFFFFFFFE
                        new_pc= new_pc & 0xFFFFFFFF
                        
                        if new_pc // 4 >= len(instructions) or new_pc < 0 or new_pc % 4 != 0:
                                raise ZeroDivisionError
                        
                        pc = new_pc
                        jump = True
        
def SType(binstring:str):

        global pc
        global regStates
        global memStates

        funct3 = binstring[-15:-12]
        imm = binstring[-32:-25] + binstring[-12:-7]

        rs2 = binstring[-25:-20]
        rs1 = binstring[-20:-15]

        rs1 = int(rs1,2)
        rs2 = int(rs2,2)


        if rs1 not in regStates or rs2 not in regStates:
                raise ZeroDivisionError
        
        if funct3 != "010":
                raise ZeroDivisionError
        
        val1 = regStates.get(rs1)
        val2 = regStates.get(rs2)

        temp = int(imm, 2)
        if temp%4 != 0 or temp > 2048:
                raise ZeroDivisionError
        
        imm = signExt(imm, "S")
        imm = int(imm, 2) if (imm[0] == "0") else int(imm, 2) - (2**32)

        memAdd = memory(val1 + imm)
        
        if not(val2 < 2**32 and val2 >= -(2**32)):
                raise ZeroDivisionError
        memStates[memAdd] = val2
                    
def BType(binString:str):
        global pc
        global regStates
        global memStates
        global jump
        
        funct3 = binString[-15:-12]
        imm_12 = binString[-32]             
        imm_11 = binString[-8]              
        imm_10_5 = binString[-31:-25]       
        imm_4_1 = binString[-12:-8]

        imm = imm_12 + imm_11 + imm_10_5 + imm_4_1
        imm = signExt(imm, "B")

        rs1 = binString[-20:-15]
        rs2 = binString[-25:-20]
        rs1 = int(rs1, 2)
        rs2 = int(rs2, 2)

        if (rs1 not in regStates) or (rs2 not in regStates):
                raise ZeroDivisionError
        
        v1 = regStates.get(rs1)
        v2 = regStates.get(rs2)

        offset = int(imm, 2) if (imm[0] == "0") else int(imm, 2) - (2**32)
        if not(offset < 2*12 and offset >= -(2**12)):
                raise ZeroDivisionError
        
        take_branch = False
        
        match funct3:
                case "000":
                        take_branch = (v1 == v2)
                case "001":
                        take_branch = (v1 != v2)
                case "100":
                        take_branch = (v1 < v2)
                case "101":
                        take_branch = (v1 >= v2)
                case "110":
                        take_branch = (v1 & 0xFFFFFFFF) < (v2 & 0xFFFFFFFF)
                case "111":
                        take_branch = (v1 & 0xFFFFFFFF) >= (v2 & 0xFFFFFFFF)
                case _:
                        raise ZeroDivisionError
                
        if take_branch:
                new_pc = pc + offset
                if (new_pc // 4 >= len(instructions)) or (new_pc < 0):
                        raise ZeroDivisionError
                
                else:
                        pc = new_pc
                        jump = True

def UType(binString:str):
        global pc
        global regStates
        global memStates
        
        rd = binString[-12:-7]
        if rd == "00000":
                return
        
        imm = binString[:-12]
        temp = int(imm, 2)
        if temp > 1048575:
                raise ZeroDivisionError
        
        imm = signExt(imm, "U")
        imm = int(imm, 2) if (imm[0] == "0") else int(imm, 2) - (2**32)
        rd = int(rd, 2)
        
        if rd not in regStates:
                raise ZeroDivisionError

        opcode = binString[-7:]
        
        match opcode:
                case "0110111":
                        if not(imm < 2**32 and imm >= -(2**32)):
                                raise ZeroDivisionError
                        regStates[rd] = imm                                

                case "0010111":
                        val = pc + imm
                        if val > ((2**31) - 1) or val < -(2**31):
                                raise ZeroDivisionError
                        regStates[rd] = val
        
def JType(binString:str):
        global pc
        global regStates
        global memStates
        global jump
        
        imm = binString[-32] + binString[-20:-12] + binString[-21] + binString[-31:-21]

        temp = int(imm, 2)
        if temp > 1048575 or temp < 0:
                raise ZeroDivisionError
        imm = signExt(imm, "J")
        imm = int(imm, 2) if (imm[0] == "0") else int(imm, 2) - (2**32)

        rd = binString[-12:-7]
        rd = int(rd, 2)
        if rd not in regStates:
                raise ZeroDivisionError
        
        new_pc = pc + imm
        new_pc= new_pc & 0xFFFFFFFF
                        
        if new_pc // 4 >= len(instructions) or new_pc < 0 or new_pc % 4 != 0:
                raise ZeroDivisionError
        
        if not(pc < 2**32 and pc >= - (2**32)):
                raise ZeroDivisionError
        
        regStates[rd] = pc + 4 if (rd != 0) else 0
        
        pc = new_pc
        jump = True

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
        global pc 
        global traceList
        global errMSG
        global errors
        global jump

        instructions = [] 
        
        input_file = sys.argv[1]
        machine_out = sys.argv[2]
        optional_out = sys.argv[3] if (len(sys.argv) > 3) else None
        
        fh_read = open(input_file, "r")
        instructions = fh_read.readlines()
        
        ind = pc
        run = True
        
        if "00000000000000000000000001100011" not in instructions:
                run = False
                print("Error Encountered!!\n\
                      Error Message: Virtual Halt not present in the instructions")
        
        elif instructions[-1] != "00000000000000000000000001100011":
                run = False
                print("Error Encountered!!\n\
                      Error Message: Virtual Halt is not present as final Statement")
        
        else:        
                while(instructions[ind] != "00000000000000000000000001100011" and run and ind < len(instructions)):
                        ind = pc//4
                        pc = pc + 4 if (not jump) else pc
                        jump = False

                        try:
                                if instructions[ind].strip() == "":
                                        continue
                                execute(instructions[ind])
                                writeRegStates()
                                
                        
                        except ZeroDivisionError:
                                break
                        
                        pc += 4
                
                else:
                        try:
                                writeMemStates()
                                fh_write = open(machine_out, "w")
                                fh_write.writelines(traceList)
                        
                        except ZeroDivisionError:
                                print("Error Encountered!!\n\
                                      Error Message: Overflow was detected while writing memory")          

# remove pass after function is created
if __name__ == "__main__":
        main()