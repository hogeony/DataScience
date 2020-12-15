# micro, macro, weighted => https://datascience.stackexchange.com/questions/40900/whats-the-difference-between-sklearn-f1-score-micro-and-weighted-for-a-mult

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import metrics

def cf_mat_precision_recall_f1(cf_mat):
    len_mat = len(cf_mat)
    recall = []  # 실제 정확도
    for i in range(len_mat):
        recall.append(cf_mat[i, :] / cf_mat[i, :].sum() * 100)
    recall = np.array(recall)

    precision = []  # 예측 정확도
    cf_mat = cf_mat.transpose()
    for i in range(len_mat):
        precision.append(cf_mat[i, :] / cf_mat[i, :].sum() * 100)
    precision = np.array(precision).transpose()

    f1 = np.zeros((len_mat, len_mat))  # 실제, 얘측 조화 평균
    for i in range(len_mat):
        for j in range(len_mat):
            f1[i, j] = 2 * (precision[i, j] * recall[i, j]) / (precision[i, j] + recall[i, j])

    f1 = np.array(f1)
    return recall, precision, f1

def fig_cf(path_fig, label_unique_list, cf_mat):
    plt.figure(figsize=(15, 13))
    cf_precision, cf_recall, cf_f1 = cf_mat_precision_recall_f1(cf_mat)
    mat_list = [(1, 'Confusion Matrix', 'Blues', '%4d', cf_mat),
                (2, 'F1 Score', 'Purples', '%5.1f', cf_f1),
                (3, 'Precision', 'Greens', '%5.1f', cf_precision),
                (4, 'Recall', 'Oranges', '%5.1f', cf_recall)]
    for i, met_title, cf_cmap, text_format, mat in mat_list:
        plt.subplot(220 + i)
        ax = sns.heatmap(mat, annot=False, linewidths=.5, square=True, cmap=cf_cmap, xticklabels=label_unique_list, yticklabels=label_unique_list, cbar_kws={"shrink": .9})
        ax.axhline(y=0, color='k')
        ax.axhline(y=mat.shape[1])
        ax.axvline(x=0, color='k')
        ax.axvline(x=mat.shape[0])

        plt.title(met_title, fontsize=12, color='r')
        plt.xlabel('Prediction')
        plt.ylabel('Truth')
        for i in range(cf_mat.shape[0]):
            for j in range(cf_mat.shape[1]):
                v = mat[i, j]
                if v > mat[mat > 0].mean():
                    plt.text(j + 0.05, i + 0.6, text_format % v, color='w', fontsize=7)
                elif v > 0:
                    plt.text(j + 0.05, i + 0.6, text_format % v, color='k', fontsize=7)
    plt.tight_layout()
    plt.savefig(path_fig)

label_list = ['Label_%02d'%x for x in range(22)]

y_true = [6, 2, 15, 15, 15, 17, 2, 2, 21, 9, 9, 15, 2, 21, 6, 15, 2, 9, 2, 2, 2, 17, 2, 21, 10, 9, 17, 21, 17, 17, 21, 21, 9, 15, 15, 21, 6, 9, 21, 15, 17, 6, 17, 9, 15, 9, 15, 17, 9, 9, 2, 10, 10, 10, 2, 6, 21, 17, 2, 10, 9, 15, 17, 10, 21, 6, 10, 6, 6, 21, 10, 10, 9, 9, 2, 21, 15, 6, 9, 15, 15, 9, 17, 15, 15, 6, 9, 17, 9, 2, 21, 17, 21, 21, 6, 17, 6, 9, 17, 9, 2, 6, 2, 6, 6, 6, 9, 9]
y_pred = [6, 3, 15, 15, 15, 16, 1, 1, 21, 9, 9, 15, 3, 21, 6, 15, 3, 9, 1, 3, 1, 12, 1, 19, 10, 9, 12, 19, 16, 1, 19, 21, 9, 15, 15, 21, 6, 9, 19, 15, 16, 6, 19, 9, 15, 9, 15, 12, 9, 9, 1, 10, 10, 10, 3, 6, 21, 12, 1, 10, 9, 15, 19, 10, 21, 20, 10, 6, 6, 19, 10, 10, 9, 7, 3, 19, 11, 6, 12, 11, 15, 9, 19, 17, 12, 6, 9, 12, 15, 1, 21, 19, 21, 19, 6, 16, 6, 1, 19, 9, 1, 6, 1, 20, 20, 20, 9, 9]

label_unique_list = [label_list[x] for x in np.unique((y_true, y_pred))]
cf_mat = metrics.confusion_matrix(y_true, y_pred)
fig_cf('cf_mat.png', label_unique_list, cf_mat)

print(metrics.classification_report(y_true, y_pred, target_names=label_unique_list, digits=4))
metrics_report = metrics.classification_report(y_true, y_pred, target_names=label_unique_list, digits=4, output_dict=True)

metrics_keys = label_unique_list + ['accuracy', 'macro avg', 'weighted avg']
for metrics_key in metrics_keys:
    v = metrics_report[metrics_key]
    if isinstance(v, dict):
        v = [*v.values()]
    else:
        v = [v]
    msg = '%s,%s' % (metrics_key, str(v).replace('[', '').replace(']', '').replace(' ', ''))
    print(msg)
    with open('Results.txt', 'a') as f:
        f.write(msg + '\n')
