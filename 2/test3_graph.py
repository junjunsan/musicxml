#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 12

# sklearn.linear_model.LinearRegression クラスを読み込み
from sklearn import linear_model
clf = linear_model.LinearRegression()
 
# 説明変数に "TS (シュート数)" を利用
#X = wc_data.loc[:, ['TS']].values/wc_data.loc[:, ['MP']].values
#X = (wc_data.loc[:, ['SGP']].values + wc_data.loc[:, ['SGO']].values)/\
#    wc_data.loc[:, ['MP']].values
X1 = [[0],[0],[0],[0],[0],[0],[0],[0]]
X2 = [[0],[0],[0],[0],[0],[0],[0],[0]]
X3 = [[0],[0],[0],[0],[0],[0],[0],[0]]
X4 = [[0],[0],[0],[0],[0],[0],[0],[0]]
X5 = [[0],[0],[0],[0],[0],[1],[0],[0]]
X6 = [[0],[0],[0],[0],[0],[0],[0],[0]]
X7 = [[0],[0],[1],[0],[0],[0],[0],[0]]
X8 = [[0],[0],[0],[0],[0],[0],[0],[0]]
X9 = [[0],[0],[0],[0],[0],[0],[0],[0]]

# 目的変数に "WR (勝率)" を利用
Y =[1,1,1,1,0,0,0,0]

X=X1
# 予測モデルを作成
clf.fit(X, Y)
 
# 回帰係数
print(clf.coef_)

# 切片 (誤差)
print(clf.intercept_)

# 決定係数
print(clf.score(X, Y))

# 散布図
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X, Y)
 
# 回帰直線
ax.plot(X, clf.predict(X), 'C1')
ax.set_xlim(-0.05, 1.05)
ax.set_xlabel('pattern1[0,1]')
ax.set_ylim(-0.05, 1.05)
ax.set_ylabel('textbook[0,1]')

ax.text(0.25, 0.92, r'$Y = {:.4f}\ X {:+.4f}$'.format(
    clf.coef_[0], clf.intercept_),
        ha='center', transform=ax.transAxes)
ax.text(0.25, 0.85, r'$R^2 = {:.4f}$'.format(clf.score(X, Y)),
        ha='center', transform=ax.transAxes)

ax.grid(True)
ax.set_title('regression analysis')
fig.savefig('test3_graph_0.png')
plt.show()
