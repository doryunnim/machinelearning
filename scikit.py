from sklearn import svm, metrics

datas = [[1*1], [1*2], [1*3], [1*4], [1*5], [2*2], [2*3], [2*4], [2*5], [3*3], [3*4], [3*5], [3*6], [4*8], [5*7]]
lables = [1, 2, 3, 4, 5, 4, 6, 8, 10, 9, 12 ,15, 18, 32, 35]
examples = [[5*5], [9*2], [12*12]]
examples_label = [25, 18, 144]

clf = svm.SVC()
clf.fit(datas, lables)
result = clf.predict(examples)
print(result)

score = metrics.accuracy_score(examples_label, result)
print("정답률 : ", score)