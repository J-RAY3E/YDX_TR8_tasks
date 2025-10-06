def Figon():
    memory =  dict()
    def managerCommand(command):
            command = command.strip()  
            if command.startswith("List "):
                command = command.removeprefix("List ").split(" = ")
                
                if "subList" in command[-1]:
                    command[-1] = command[-1].split(".subList(")
                    command[-1][-1] =  list(map(int,command[-1][-1].removesuffix(")").split(",") ))
                    if type(memory[command[-1][0]]) is tuple:
                        memory[command[0]] = (memory[command[-1][0]][0],memory[command[-1][0]][1] + command[-1][-1][0]-1,memory[command[-1][0]][1] + command[-1][-1][1])
                    else:
                        memory[command[0]] = (memory[command[-1][0]],command[-1][-1][0]-1,command[-1][-1][1])
                else:
                    nums = command[-1].removeprefix("new List(").removesuffix(")")
                    if nums == "":
                        arr = []
                    else:
                        arr = list(map(int, nums.split(",")))
                    memory[command[0]] = arr

                return "Exito"
            elif ".set(" in command:
                command = command.split(".set(")
                command[-1] = list(map(int, command[-1].removesuffix(")").split(",")))
                if type(memory[command[0]]) is list:
                    memory[command[0]][command[-1][0]-1] = command[-1][1]
                elif type(memory[command[0]]) is tuple:
                    memory[command[0]][0][memory[command[0]][1]+command[-1][0]-1] = command[-1][1]
                return "Exito"
            elif ".get(" in command:
                command = command.split(".get(")
                if type(memory[command[0]]) is list:
                    return memory[command[0]][int(command[-1].removesuffix(")")) -1 ]
                elif type(memory[command[0]]) is tuple:
                    return memory[command[0]][0][memory[command[0]][1] + int(command[-1].removesuffix(")")) -1]
                return "Exito"
            elif ".add(" in command:
                command = command.split(".add(")
                if type(memory[command[0]]) is tuple:
                    return "Exito"
                memory[command[0]].append(int(command[-1].removesuffix(")")))
                return "Exito"
            
    n = int(input())
    commands = [input() for _ in range(n)]
    for command in commands:
        ouput = managerCommand(command)

        print(ouput) if ouput != "Exito" else None

if __name__ == "__main__":
    Figon()