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

def corrInstruction(inst:str) -> str:
        temp = list(inst.partition(" "))
        if "," in temp[2].strip(","):
                temp2 = temp[1:]
                temp2 = ("".join("".join(temp2).split(" "))).split(",")
                temp2 = [i.strip() for i in temp2]

                args = ", ".join(temp2)
                while(len(temp) != 1):
                        temp.pop()
                temp.append(args)
                inst = " ".join(temp)
        return inst.lower()

def convert(inst:str, label:bool, index:int) -> str:

        if label:
                if inst.strip()[-1] == ":":
                        return
                
                else:
                        inst = inst.split(":")
                        inst = " ".join(inst[1:]).strip()

        inst = corrInstruction(inst)
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
        global instructions

        inst = inst.split()
        temp = inst[0]
        if temp in instructions:
                return instructions.get(temp)
        
        raise ZeroDivisionError       

def rType(inst:str) -> str:
        global registers

        inst = inst.split()
        
        if len(inst) != 4:
                raise ZeroDivisionError
        
        match (inst[0].lower()):
                case "add":
                        funct7 = "0000000"
                        funct3 = "000"
                case "sub":
                        funct7 = "0100000"
                        funct3 = "000"
                case "sll":
                        funct7 = "0000000"
                        funct3 = "001"
                case "slt":
                        funct7 = "0000000"
                        funct3 = "010"
                case "sltu":
                        funct7 = "0000000"
                        funct3 = "011"
                case "xor":
                        funct7 = "0000000"
                        funct3 = "100"
                case "srl":
                        funct7 = "0000000"
                        funct3 = "101"
                case "or":
                        funct7 = "0000000"
                        funct3 = "110"
                case "and":
                        funct7 = "0000000"
                        funct3 = "111"
                case _:
                        raise ZeroDivisionError


        rd = corr(inst[1])
        rs1 = corr(inst[2])
        rs2 = corr(inst[3])

        if rd not in registers or rs1 not in registers or rs2 not in registers:
                raise ZeroDivisionError
        
        rd = registers.get(rd)
        rd = format(rd, "05b")
        rs1 = registers.get(rs1)
        rs1 = format(rs1, "05b")
        rs2 = registers.get(rs2)
        rs2 = format(rs2, "05b")

        opcode = "0110011"

        binInst = funct7 + rs2 +rs1 + funct3 + rd + opcode        
        return binInst

def iType(inst:str) -> str:
        global registers

        inst = inst.split()
        
        match(inst[0]):
                case "addi":
                        opcode = "0010011"
                        funct3 = "000"
                case "lw":
                        opcode = "0000011"
                        funct3 = "010"

                case "sltiu":
                        opcode = "0010011"
                        funct3 = "011"
                case "jalr":
                        opcode = "1100111"
                        funct3 = "000"
                case _:
                        raise ZeroDivisionError
                
        rd = corr(inst[1])
        if rd not in registers:
                raise ZeroDivisionError

        rd = format(registers.get(rd),"05b")

        if (opcode == "0010011") or (opcode == "1100111"):
                if(len(inst) != 4):
                        raise ZeroDivisionError
                rs = corr(inst[2])
                imm = corr(inst[3])
        
        else:
                temp = inst[2].split("(")
                if len(temp) != 2:
                        raise ZeroDivisionError
                
                temp[1] = temp[1].rstrip(")")
                imm = corr(temp[0])
                rs = corr(temp[1])

        if rs not in registers:
                raise ZeroDivisionError
        
        rs = format(registers.get(rs),"05b")
        
        if not imm.lstrip("-").isnumeric() or int(imm) > 2047 or int(imm) < -2048:
                raise ZeroDivisionError
        else:
                imm = int(imm)
                imm = format(imm & 0xfff, "012b")
                        
        
        binInst = imm + rs + funct3 + rd + opcode
        return binInst        

def bType(inst:str) -> str:
        global labels
        global registers
        global pc

        opcode = "1100011"
        elements = inst.split()

        if len(elements) != 4:
                raise ZeroDivisionError

        d_funct3 = {
                "beq": "000",
                "bne": "001",
                "blt": "100",
                "bge": "101",
                "bltu": "110",
                "bgeu": "111"
        }

        operation = elements[0]
        if operation not in d_funct3:
                raise ZeroDivisionError

        funct3 = d_funct3[operation]

        rs1 = corr(elements[1])
        rs2 = corr(elements[2])

        if rs1 not in registers or rs2 not in registers:
                raise ZeroDivisionError
        
        rs1 = registers.get(rs1)
        rs2 = registers.get(rs2)
        rs1 = format(rs1, "05b")
        rs2 = format(rs2, "05b")
    
        imm = corr(elements[3])
        if not imm.isnumeric():
                if imm not in labels:
                        raise ZeroDivisionError
                val = int(labels[imm])
                imm = 2*(val - pc)
        else:
                imm=int(imm)
                if imm%4 != 0 or imm > 2047 or imm < -2048:
                        raise ZeroDivisionError
        
        imm_bin = format(imm & 0xfff, '012b')
        imm_12 = imm_bin[0]
        imm_10_5 = imm_bin[2:8]
        imm_4_1 = imm_bin[8:]
        imm_11 = imm_bin[1]

        output = imm_12 + imm_10_5 + rs2 + rs1 + funct3 + imm_4_1 + imm_11 + opcode

        return output
def sType(inst: str) -> str:
	global registers

	inst = inst.lower().split()
	if len(inst) != 3 or inst[0] != "sw":
		raise ZeroDivisionError

	rs2 = corr(inst[1])
	temp = inst[2]
	if "(" not in temp or ")" not in temp:
		raise ZeroDivisionError

	temp = temp.split("(")
	if len(temp) != 2:
		raise ZeroDivisionError

	imm = corr(temp[0])
	rs1 = corr(temp[1].strip(")"))

	if rs1 not in registers or rs2 not in registers:
		raise ZeroDivisionError

	rs1 = format(registers.get(rs1), "05b")
	rs2 = format(registers.get(rs2), "05b")

	imm = int(imm)
	if imm > 2047 or imm < -2048:
		raise ZeroDivisionError

	imm = format(imm & 0xfff, "012b")

	opcode = "0100011"
	funct3 = "010"

	binInst = imm[:7] + rs2 + rs1 + funct3 + imm[7:] + opcode
	return binInst

def uType(inst:str) -> str:
        global registers

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
        if rd not in registers:
                raise ZeroDivisionError
        
        rd = registers.get(rd)        
        rd = format(rd, "05b")
        
        imm = int(corr(inst[2]))
        imm = format(imm & 0xfffff, "020b")
        
        binInst = imm + rd + opcode
        return binInst

def jType(inst:str) -> str:
        global pc
        global labels
        global registers

        inst = inst.split()
        opcode = "1101111"
        rd = corr(inst[1])
        imm = corr(inst[2])

        if rd not in registers:
                raise ZeroDivisionError
        rd=registers.get(rd)
        rd=format(rd,"05b")
        if not imm.strip().strip("-").isnumeric():
                if imm not in labels:
                        raise ZeroDivisionError
                
                offset = 2*(labels.get(imm) - pc)
                imm = format(offset & 0xffffffff, "020b")
        
        else:
                imm = int(imm)
                if imm%4 != 0 or imm > (2**19)-1 or imm < -(2**19):
                        raise ZeroDivisionError
                
                imm = format(imm & 0xfffff, "020b")

        binInst = imm[0] + imm[-10:] + imm[1] + imm[2:-10] + rd + opcode
        return binInst

def corr(string:str) -> str:
        while("," in string):
                ind = string.index(",")
                string = string[0:ind] + string[ind+1:]
        return string
        
def main():

        binInst = []
        global pc
        global labels

        import sys
        input_file = sys.argv[1]
        machine_out = sys.argv[2]
        optional_out = sys.argv[3] if (len(sys.argv) > 3) else None

        fh_read = open(input_file, 'r')
        instructions = fh_read.readlines()
        fh_read.close()
        
        tempIndex = -1
        for instruc in instructions:
                tempIndex += 1
                if ":" not in instruc:
                        continue
                
                label = instruc.split(":")[0]
                labels[label] = tempIndex            
        
        for i in range(len(instructions)):
                binInstruction = ""
                instruction = instructions[i].strip("/r/n").lower()
                instruction = instruction.lower()
                try:
                        isLabel = 0 if(":" not in instruction) else 1
                        binInstruction = convert(instruction, isLabel, pc)
                        binInst.append(binInstruction)
                        pc += 1

                
                except ZeroDivisionError:
                        print("You encountered an error on line", i)
                        break
        
        if ("00000000000000000000000001100011" in binInst):
                with open(machine_out, "w") as fh_write:
                        fh_write.writelines(binInst)
                
        else:
                print("No Virtual Halt Statement found")
                
#Please remove pass after the function has been built
if __name__ == "__main__":
        main()
