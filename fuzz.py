#!/bin/python3

import subprocess
from random import randint

def execute(cmd):
    try:
        subprocess.call(cmd, shell=True, timeout=2)
    except Exception:
        return ;

def mutate(data):
    idx = randint(0, len(data))
    c = chr(randint(0, 0xFF))
    return data[:idx] + c.encode("utf-8") + data[idx:]

def copy_exe():
    with open("gate", "rb") as original, open("gate_fuzz", "wb") as new_file:
        new_file.write(mutate(original.read()))

def compare(fn1, fn2):
    with open(fn1) as f1, open(fn2) as f2:
        return f1.read() == f2.read()

def check_output():
    execute("(./gate ; ./gate gobbledegook ; ./gate hunter2) > tmp/orig_output")
    execute("(./gate_fuzz ; ./gate_fuzz gobbledegook ; ./gate_fuzz hunter2) > tmp/fuzz_output")
    return compare("tmp/orig_output", "tmp/fuzz_output")

def check_gdb():
    execute("echo disassemble main | gdb gate > tmp/orig_gdb")
    execute("echo disassemble main | gdb gate_fuzz > tmp/fuzz_gdb")
    return compare("tmp/orig_gdb", "tmp/fuzz_gdb")

def check_radare():
    execute('echo -e "aaa\ns sym.main\npdf" | radare2 gate > tmp/orig_radare')
    execute('echo -e "aaa\ns sym.main\npdf" | radare2 gate_fuzz > tmp/fuzz_radare')
    return compare("tmp/orig_radare", "tmp/fuzz_radare")

execute("cp gate gate_fuzz")

while True:
    copy_exe()
    if check_output() and not check_gdb() and not check_radare():
        print("FOUND POSSIBLE MUTATION\n\n\n")
        execute("tail tmp/fuzz_gdb")
        execute("tail tmp/fuzz_radare")
        input("\nPress Enter to continue...\n")
