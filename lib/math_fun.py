import lib.functionalities as fun
import lib.memory as me

def math_doing(f, v):
    if f=='print':
        fun.p_msg(v)


def m_sum(options):
    values = me.checkVariable(options['v'])

    fn = options['f']
    total = 0
    
    for v in values:
        total += int(v)
    math_doing(fn, total)

