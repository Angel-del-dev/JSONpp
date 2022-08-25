import lib.functionalities as fun
import lib.math_fun as ma
import lib.memory as me


p_args = {
    'for': fun.f_loop,
    'print' : fun.p_msg,
    'sum': ma.m_sum
}

def lexer(key, args):
    args = me.checkVariable(args)

    p_args[key](args)

def loop(data):
    for k, v in data.items():
        lexer(k, v)


