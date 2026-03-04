# 1. Use the following format for Instruction type overall
#       Eg: "I" -> I-Type, etc.

# 2. Call signExt() whenever you get an immediate
#       Eg: imm = signExt(imm)

# 3. All binary values need be read imm[2:]
#       Reason: Binary strings start wtih unneccesary "0b"

# 4. Break instruction into words using .split()

# 5. For errors in any type raise ZeroDivisonError and catch it in main()

# 6. Start all binary strings with "0b" followed by 0s and 1s to keep the format same overall.

#7. Call corr() to remove commas

#8. Call register() to get hexcode of register if not already provided.

pc = 0

instructions = {
    "add":"R",
    "sub":"R",
    "slt":"R",
    "sltu":"R",
    "xor":"R",
    "sll":"R",
    "srl":"R",
    "or":"R",
    "and":"R",
    "lw":"I",
    "addi":"I",
    "sltiu":"I",
    "jalr":"I",
    "sw":"S",
    "beq":"B",
    "bne":"B",
    "bge":"B",
    "bgeu":"B",
    "blt":"B",
    "bltu":"B",
    "auipc":"U",
    "lui":"U",
    "jal":"J"
}

registers = {
    "zero": 0, "ra": 1, "sp": 2, "gp": 3, "tp": 4,
    "t0": 5, "t1": 6, "t2": 7,
    "s0": 8, "fp": 8, "s1": 9,
    "a0": 10, "a1": 11, "a2": 12, "a3": 13,
    "a4": 14, "a5": 15, "a6": 16, "a7": 17,
    "s2": 18, "s3": 19, "s4": 20, "s5": 21,
    "s6": 22, "s7": 23, "s8": 24, "s9": 25,
    "s10": 26, "s11": 27,
    "t3": 28, "t4": 29, "t5": 30, "t6": 31,
    "x0": 0, "x1": 1, "x2": 2, "x3": 3, "x4": 4,
    "x5": 5, "x6": 6, "x7": 7,
    "x8": 8, "x9": 9, "x10": 10, "x11": 11,
    "x12": 12, "x13": 13, "x14": 14, "x15": 15,
    "x16": 16, "x17": 17, "x18": 18, "x19": 19,
    "x20": 20, "x21": 21, "x22": 22, "x23": 23,
    "x24": 24, "x25": 25, "x26": 26, "x27": 27,
    "x28": 28, "x29": 29, "x30": 30, "x31": 31
}

labels = {}

def convert(inst:str, label:bool, index:int) -> str:
        if label:
                if inst.strip()[-1] == ":":
                        labels[inst[:-1]] = index
                        return
                
                else:
                        inst = inst.split()
                        labels[inst[0][:-1]] = index
                        " ".join(inst[1:])

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
        return binInst

def checkType(inst:str)->str:
        inst = inst.split()
        temp = inst[0]
        if temp in instructions:
                return instructions.get(temp)
        
        return "Not Found"       

def rType(inst:str) -> str:
        pass

def iType(inst:str) -> str:
        inst=inst.split()
        match(inst[0]):
                case "addi":
                        opcode="0010011"
                        funct3="000"
                case "lw":
                        opcode="0000011"
                        funct3="010"

                case "sltiu":
                        opcode="0010011"
                        funct3="011"
                case "jalr":
                        opcode="1100111"
                        funct3="000"
                case _:
                        raise ZeroDivisionError
                
        rd = corr(inst[1])
        if rd not in registers:
                raise ZeroDivisionError
        else:
                rd = format(registers.get(rd),"05b")

        if opcode == "0010011" or opcode == "1100111":
                if(len(inst) != 4):
                        raise ZeroDivisionError
                else:
                        rs = corr(inst[2])
                        imm = inst[3]
        else:
                temp = inst[2].split("(")
                if len(temp) != 2:
                        raise ZeroDivisionError
                temp[1] = temp[1].rstrip(")")
                imm = temp[0]
                rs = temp[1]

        if rs not in registers:
                raise ZeroDivisionError
        else:
                rs = format(registers.get(rs),"05b")
        
        if not imm.lstrip("-").isdigit() or int(imm) > 2047 or int(imm) < -2048:
                raise ZeroDivisionError
        else:
                imm = int(imm)
                imm = format(imm & 0xfff,"012b")
                        
        
        binInst = imm + funct3 + rs + rd + opcode
        return binInst

def sType(inst:str) -> str:
        pass

def bType(inst:str) -> str:
        global pc
        pass

def sType(inst:str):
        pass

def uType(inst:str) -> str:
        inst = inst.split()
        
        if len(inst) != 3:
                raise ZeroDivisionError

        binInst = ""
        match(inst[0]):
                case "lui":
                        opcode = "0110111"
                case "auipc":
                        opcode = "0010111"
                case _:
                        raise ZeroDivisionError
        
        rd = corr(inst[1])
        rd = registers.get(rd)
        
        if rd > 31 and rd < 0:
                raise ZeroDivisionError
        else:
                rd = format(rd, "05b")
        
        imm = int(inst[2])
        imm = format(imm & 0xffffffff, "020b")
        
        binInst = imm + rd + opcode
        return binInst

def jType(inst:str) -> str:
        global pc
        pass

def corr(string:str) -> str:
        while(string[-1] == ","):
                string  = string[:-1]
        return string
        
def main():
        
        for i in range(0):
                instruction = instruction.lower() #After input lower all case
                try:
                        isLabel = 0 if(":" not in instruction) else 1
                        binInstruction = convert(instruction, isLabel, i)
                        pc+=1
                        #Write binary string onto file
                
                except ZeroDivisionError:
                        print("You encountered an error on line", i)
                        break


        pass

#Please remove pass after the function has been built
if __name__ == "__main__":
        main()
