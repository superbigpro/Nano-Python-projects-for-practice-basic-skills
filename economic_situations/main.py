from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

# FRED API Key 입력
api_key = 'a2aa6f37d59e8adfcfabfc3dfc16bb9ca2aa6f37d59e8adfcfabfc3dfc16bb9c'

# API 연결
fred = Fred(api_key=api_key)

# GDP 데이터 불러오기
gdp_data = pd.DataFrame(fred.get_series('GDP'), columns=['GDP'])

# 불필요한 데이터 제거
gdp_data = gdp_data.dropna()

# 데이터 출력
print(gdp_data)

# 그래프 그리기
plt.plot(gdp_data)

# 그래프 제목 추가
plt.title('Gross Domestic Product: {:.3f}'.format(gdp_data.iloc[-1][0]))

# 그래프 표시
plt.show()