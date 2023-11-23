import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 랜덤 데이터 생성
np.random.seed(0)
data = np.random.randn(100, 2)
a, b = data[:, 0], data[:, 1]

# 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 기술 통계: 평균과 중앙값
for i, var in enumerate([a, b]):
    axes[0, 0].bar(['평균', '중앙값'], [np.mean(var), np.median(var)], alpha=0.7, label=f'변수 {i+1}')

axes[0, 0].legend()
axes[0, 0].set_title('기술 통계: 평균과 중앙값')

# 상관 분석
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('상관 분석')

# 변수의 히스토그램
axes[1, 0].hist([a, b], bins=15, alpha=0.7, label=['변수 1', '변수 2'])
axes[1, 0].legend()
axes[1, 0].set_title('변수의 히스토그램')

# 변수 1 대 변수 2의 산점도
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('변수 1')
axes[1, 1].set_ylabel('변수 2')
axes[1, 1].set_title('변수 1 대 변수 2의 산점도')

# 레이아웃 조정 및 표시
plt.tight_layout()
plt.show()
