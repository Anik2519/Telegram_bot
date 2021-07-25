def fun(s):
    tmp = s.split()
    tmp.pop(0)

    if len(tmp)==0:
        return "+technology"

    str = ""
    i=1
    for x in tmp:
        str = str + "+" + x
        if i!= len(tmp):
            str = str + " AND "
        i =i+1
    return str

