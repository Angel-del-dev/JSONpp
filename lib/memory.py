import json

variables = {}

def setVariables(vars):
    for k, v in vars.items():
        variables[k] = v

def unsetVariables(keys):
    for k in keys:
        variables.pop(k, None)

def checkVariable(a):
    a = json.dumps(a)
    for v_k in variables.keys():
        if(type(a) == str and v_k in a):
            a = a.replace('$'+v_k, str(variables[v_k]))

    return json.loads(a)
    