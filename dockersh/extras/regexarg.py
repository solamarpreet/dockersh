# My script to organise command arguments for dockershell
import re

with open('/home/sol/work/dockershell/env/input.txt') as f:
    fc = f.read()
    singlelist = re.findall(r"(-\w),", fc)
    for i in range(len(singlelist)):
        singlelist[i]+=' : None,'
    s = '\n'.join(singlelist)
    s+='\n'
    s = re.sub(r"(-\w)", r"'\1'", s)
    fc = re.sub(r"-\w,", r"", fc)
    fc = re.sub(r"(--.+?)\s", r"'\1'", fc)
    fc = re.sub(r"('--.+?)'\w", r"\1='", fc)
    fc = re.sub(r"\s*[A-Z].*", r" : None,", fc)
    fc = re.sub(r"'\w.*?\s", r"' ", fc)
    fc = re.sub(r"\n.*?'", r"\n'", fc)
    fc = re.sub(r"^\s.*?'", r"'", fc)
    with open('/home/sol/work/dockershell/env/output.txt', 'w') as f2:
        f2.write(s)
        f2.write(fc)
