import numpy as np
import pandas as pd

# 두 개의 시리즈 데이터가 있습니다.
print("Population series data:")
population_dict = {
    'korea': 5180,
    'japan': 12718,
    'china': 141500,
    'usa': 32676
}
population = pd.Series(population_dict)
print(population, "\n")
# {'korea': 5180, 'japan': 12718, 'china': 141500, 'usa': 32676}

print("GDP series data:")
gdp_dict = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000,
}
gdp = pd.Series(gdp_dict)
print(gdp, "\n")
# {'korea': 169320000, 'japan': 516700000, 'china': 1409250000, 'usa': 2041280000}

# 이곳에서 2개의 시리즈 값이 들어간 데이터프레임을 생성합니다.
print("Country DataFrame")
country = pd.DataFrame({
    'population': population,
    'gdp': gdp
})
#        population         gdp
# korea        5180   169320000
# japan       12718   516700000
# china      141500  1409250000
# usa         32676  2041280000


# 데이터 프레임에 1인당 GDP 를 나타내는 새로운 컬럼인 gdp per capita 칼럼을 추가하고 출력합니다.
# 1인당 GDP는 gdp와 population을 나누어 얻을 수 있습니다.
country['gdp per capita'] = country['gdp'] / country['population']
print(country)
#        population         gdp  gdp per capita
# korea        5180   169320000    32687.258687
# japan       12718   516700000    40627.457147
# china      141500  1409250000     9959.363958
# usa         32676  2041280000    62470.314604

# 데이터 프레임을 만들었다면, index와 column도 각각 확인해보세요.
print(country.index)
# Index(['korea', 'japan', 'china', 'usa'], dtype='object')
print(country.columns)
# Index(['population', 'gdp', 'gdp per capita'], dtype='object')
