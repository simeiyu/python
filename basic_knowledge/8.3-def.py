'''
8.3 返回值
----------
函数返回的值被称为返回值。
在函数中，可使用return语句将值返回到调用函数的代码行。
返回值能够让你将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
'''
# 简单返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 让实参变成可选的  使用默认值让实参变成可选的
def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name2('jimi', 'hendrix')
print(musician)

musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)

# 返回字典  函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
def build_person(first_name, last_name, middle_name='', age=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    person = {'name': full_name.title()}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=32)
print(musician)

# 结合使用函数和while循环
while True:
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name2(f_name, l_name)
    print('\nHello, ' + formatted_name + '.')

'''
练一练
'''
def mark_album(name, editor, count=''):
    album = {'name': name, 'editor': editor}
    if count:
        album['count'] = count
    return album

while True:
    print('请输入专辑名称和歌手名字，或键入"q"退出程序')
    name = input('专辑名称：')
    if name == 'q':
        break
    editor = input('歌手：')
    if editor == 'q':
        break
    marked_album = mark_album(name, editor)
    print('\nThis album is ' + str(marked_album))
