import numpy as np
from matplotlib import pyplot as plt

# X - вектор признаков, y - зависимая величина (то, что мы пытаемся восстановить в зависимости от набора признаков

# наша модель, тета (вектор) - параметры модели, тут запись сразу в векторном виде - вектор тет и вектор X
def compute_hypothesis(X, theta):
    return np.matmul(X, theta)

# функция стоимости - критерий апроксимации - чем результат меньше, тем наша функция лучше
# суммирование по всем примерам обучающей выборки (сумма ошибок)
def compute_cost(X, y, theta):
    m = X.shape[0]  # количество примеров в выборке
    # ВАШ КОД ЗДЕСЬ

    return 1 / (2 * m) * sum((compute_hypothesis(X, theta) - y) ** 2)

    # ==============

# общий метод (численный) оптимизации диф. функций
# альфа - скорость обучения
# функция возвращает ф. стоимости для тета и сами теты
def gradient_descend(X, y, theta, alpha, num_iter):
    history = list()

    m = X.shape[0]  # количество примеров в выборке

    for i in range(num_iter):

        # ВАШ КОД ЗДЕСЬ
        # alpha * (compute_hypothesis(X, theta) - y).dot(X[:, 0]) / m - сам градиент
        theta_temp = theta
        theta_temp[0] = theta_temp[0] - alpha * (compute_hypothesis(X, theta) - y).dot(X[:, 0]) / m
        theta_temp[1] = theta_temp[1] - alpha * (compute_hypothesis(X, theta) - y).dot(X[:, 1]) / m
        theta = theta_temp

        # =====================

        history.append(compute_cost(X, y, theta))
    return history, theta


def load_data(data_file_path):
    with open(data_file_path) as input_file:
        X = list()
        y = list()
        for line in input_file:
            *row, label = map(float, line.split(','))
            X.append([1] + row)
            y.append(label)
        return np.array(X, float), np.array(y, float)


X, y = load_data('lab1data1.txt')

# фиктивный вектор + вектор признаков
print(X)
print(y)

plt.title('Исходные данные')
plt.scatter(X[:, 1], y, c='r', marker='x')
plt.show()

print('Значение функции стоимости при theta = [0.7, 0.7]: ', compute_cost(X, y, np.array([0.7, 0.7])))

history, theta = gradient_descend(X, y, np.array([0.7, 0.7], float), 0.009, 1400)

plt.title('График изменения функции стоимости от номера итерации')
plt.plot(range(len(history)), history)
plt.show()

plt.title('Обученая модель')
plt.scatter(X[:, 1], y, c='r', marker='x')
plt.plot(X[:, 1], compute_hypothesis(X, theta))
plt.show()
