#Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
#стран. Определить какие марки машин были доставлены во все указанные страны, какие в
#некоторые из стран и какие не доставлены ни в одну страну.

n = int(input())
# USA: Toyota, Volvo, Audi
# UK: Toyota, Lada, BMW

# список производимых авто в мире
auto_exp = list(map(str, input().split()))

world_dict = {}
set_auto = set()

# tmp - список авто, импортируемых в указанную страну
tmp = input().split(':')
world_dict[tmp[0]] = set(tmp[1].split(','))

set_all = world_dict[tmp[0]]
for i in range(n - 1):
    tmp = input().split(':')
    world_dict[tmp[0]] = set(tmp[1].split(','))

    # множество всех импортируемых авто
    set_auto |= world_dict[tmp[0]]

    # множество импортируемых авто во все страны
    set_all &= world_dict[tmp[0]]

    # множество импорт. авто в некоторые страны
set_any = set_auto - set_all
set_auto_only = set(auto_exp) - set_auto
print(world_dict)
print('список всех импортируемых авто: ', *set_auto)
print('список авто, импортируемых во все страны: ', *set_all)
print('список авто, импортируемых в некоторые страны: ', *set_any)
print('список неимпортируемых авто: ', set_auto_only)