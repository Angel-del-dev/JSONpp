import lib.memory as me
import lib.lexer as l

def p_msg(msg):
    print(msg)

def f_loop(val):
    iterator = val['i']
    do = val['do']
    
    i_start = iterator['$start']
    i_end = iterator['$end']
    i_iterate = iterator['$iterate']

    me.setVariables({'start': i_start, 'end': i_end, 'iterate': i_iterate})

    for i in range(i_start, i_end, i_iterate):
        me.variables['count'] = i
        l.loop(do)
    
    
    me.unsetVariables(['start', 'end', 'iterate'])
