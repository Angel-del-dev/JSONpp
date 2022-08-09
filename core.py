import sys
import json

variables = {}

def setVariables(vars):
    for k, v in vars.items():
        variables[k] = v

def unsetVariables(keys):
    for k in keys:
        variables.pop(k, None)

def p_msg(msg):
    print(msg)

def f_loop(val):
    iterator = val['i']
    do = val['do']
    
    i_start = iterator['$start']
    i_end = iterator['$end']
    i_iterate = iterator['$iterate']

    setVariables({'start': i_start, 'end': i_end, 'iterate': i_iterate})

    for i in range(i_start, i_end, i_iterate):
        variables['count'] = i
        loop(do)
    
    
    unsetVariables(['start', 'end', 'iterate'])

def checkVariable(a):
    a = json.dumps(a)
    for v_k in variables.keys():
        if(type(a) == str and v_k in a):
            a = a.replace('$'+v_k, str(variables[v_k]))
            pass
    return json.loads(a)

def math_doing(f, v):
    if f=='print':
        p_msg(v)


def m_sum(options):
    values = checkVariable(options['v'])

    fn = options['f']
    total = 0
    
    for v in values:
        total += int(v)
    
    math_doing(fn, total)

p_args = {
    'for': f_loop,
    'print' : p_msg,
    'sum': m_sum
}

def lexer(key, args):
    args = checkVariable(args)

    p_args[key](args)

def loop(data):
    for k, v in data.items():
        lexer(k, v)



if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        data = json.load(f)
        loop(data)