from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential, load_model, model_from_json
from keras import optimizers
import keras as K
import numpy as np

from sklearn.preprocessing import LabelBinarizer


model_file = "./cp/多分类4.h5"

# 训练数据
x_train1 = np.random.randint(0, 99, (100, 1))
x_train2 = np.random.randint(100, 999, (100, 1))
x_train3 = np.random.randint(1000, 9999, (100, 1))
x_train4 = np.random.randint(10000, 99999, (100, 1))

xs = np.concatenate((x_train1, x_train2, x_train3, x_train4))
y_train = np.array([[1, 0, 0, 0]*100 + [0, 1, 0, 0]*100 + [0, 0, 1, 0]*100 + [0, 0, 0, 1]*100])
labels = y_train.reshape((400, 4))

x_train = xs.astype(float)
y_train = labels.astype(float)

# 打乱数据
# 学习效率高
arr = np.arange(x_train.shape[0])
np.random.shuffle(arr)
x_train = x_train[arr, :]
y_train = labels[arr, :]

# print(x_train)
# print(y_train)



model = load_model(model_file)



score = model.evaluate(x_train, y_train, batch_size=128)
print('loss:', score[0], '\t\taccuracy:', score[1])



#测试结果
res = model.predict(np.array([[50],[564],[8975],[55555],[54687]]))

#四舍五入显示结果
print("res:\n", np.round(res))

print("res:\n", res)
