import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv("iris.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

train_data, test_data, train_label, test_label = \
    train_test_split(data, label)

clf = svm.SVC()
clf.fit(data, label)
results = clf.predict([
    [5.1, 4.4, 3.1, 2.1]
])

print(results)

# clf = svm.SVC()
# clf.fit(train_data, train_label)
# results = clf.predict(test_data)

# score = metrics.accuracy_score(results, test_label)
# print("정답률: ", score)
