from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.cmd.disassemble import DisassembleCommand
from ghidra.app.script import GhidraScript
from ghidra.program.model.address import AddressSet

args = getScriptArgs()
code_base_addr = int(args[0])
curr_base_addr = currentProgram.getImageBase().getOffset()
currentProgram.setImageBase(currentAddress.subtract(curr_base_addr-code_base_addr), True)
execMemSet = currentProgram.getMemory()
instIter = currentProgram.getListing().getInstructions(execMemSet, True)
result = ''
while instIter.hasNext():
    inst = instIter.next()
    result += inst.getAddress().toString()
    result += '(' + str(len(inst.getBytes())) + '): '
    result += inst.toString() + '\n'
print('--- instructions ---')
print(result)
print('--- instructions ---')
