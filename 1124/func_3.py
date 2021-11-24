def do_anything(*args):
    '''引数の個数によって何かする。int と str で動作'''
    print(f"受け取った値:{args}")
    items_count = len(args)
    if items_count == 0:
        print("やること無いので暇です")
    elif items_count == 1:
        if type(args[0]) == str:
            print(f"{args[0]}{args[0]}")
        elif type(args[0]) == int:
            print(f"{args[0]*2}")
        else:
            print("難しくて無理です")
    elif items_count == 2:
        t = type(args[0])
        t2 = type(args[1])
        if t == t2 and (t == int or t == str):
            print(f"{args[0]+args[1]}")
        elif t != t2:
            print("できません～")
        else:
            print("無茶言わないで！")
    else:
        print("無理です...")


# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1, 2, 3])
do_anything(10, 20)
do_anything(10, 'abc')
do_anything('x', 'yz')
do_anything([1, 2, 3], [4, 5, 6])
do_anything(1, 2, 3)
