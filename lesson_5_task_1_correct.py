from collections import namedtuple
from collections import defaultdict
"""
Задание 1.
Замечания к заданию - "реализовали через namedtuple, как мы и обсуждали на уроке" - т.е. это не очень хорошо? 
Эта коллекция вроде лучше всего подходит для решения и быстрота и меньше памяти, говорили на 5 вебинаре.
Добавил реализацию через defaultdict.
"""
# Вариант 2 defaultdict
avg_all_companies = 0
print(f'Введите количество предприятий для расчета прибыли ')
n = int(input())
company_dct = defaultdict(int)
for i in range(n):
    i += 1
    print(f'Введите название преприятия ')
    name_comp = input()
    try:
        input_list = input("Через пробел введите прибыль предприятия за каждый квартал(Всего 4 квартала) ").split()
        num_list = list(map(int, input_list))
        if len(num_list) <= 4:
            profit = sum(num_list)
            company_dct[name_comp] = profit
            avg_all_companies = (avg_all_companies + profit) / len(company_dct.keys())
        else:
            raise ValueError
    except ValueError:
        print('Ошибка ввода.В году 4 квартала')
        exit(1)
print(f'Средняя годовая прибыль всех предприятий {avg_all_companies}')
lower_profit = [key for key in company_dct if company_dct[key] < avg_all_companies]
higher_profit = [key for key in company_dct if company_dct[key] > avg_all_companies]
print('Предприятия, с прибылью выше среднего значения:')
print(*higher_profit, sep='\n')
print('Предприятия, с прибылью ниже среднего значения:')
print(*lower_profit, sep='\n')

# 1 Вариант Namedtuple
# Company = namedtuple('Company', 'name profit')
# companies = []
# avg_all_companies = 0
# print(f'Введите количество предприятий для расчета прибыли ')
# n = int(input())
# for i in range(n):
#     i += 1
#     print(f'Введите название преприятия ')
#     name_comp = input()
#
#     try:
#         input_list = input("Через пробел введите прибыль предприятия за каждый квартал(Всего 4 квартала) ").split()
#         num_list = list(map(int, input_list))
#         if len(num_list) <= 4:
#             profit: int = sum(num_list)
#             companies.append(Company(name_comp, profit))
#             avg_all_companies = (avg_all_companies + profit) / len(companies)
#         else:
#             raise ValueError
#     except ValueError:
#         print('Ошибка ввода.В году 4 квартала')
#         exit(1)
# print(f'Средняя годовая прибыль всех предприятий {avg_all_companies}')
# lower_profit = [company.name for company in companies if company.profit < avg_all_companies]
# higher_profit = [company.name for company in companies if company.profit > avg_all_companies]
# print('Предприятия, с прибылью выше среднего значения:')
# print(*higher_profit, sep='\n')
# print('Предприятия, с прибылью ниже среднего значения:')
# print(*lower_profit, sep='\n')
