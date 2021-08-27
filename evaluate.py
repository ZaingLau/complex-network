from sklearn import metrics
import matplotlib.pyplot as plt
import time
import pandas as pd
import time
import os


def get_the_class_label(test_list):
    sub_list = []
    sub_list.append(test_list[0])
    if len(test_list) == 0:
        sub_list = None
        # num = 0
    else:
        for content in test_list:
            if content not in sub_list:
                sub_list.append(content)
            else:
                continue
        # num = len(sub_list)
        sub_list.sort(reverse=False)
    return sub_list


def acc_evaluate(test_list, predict_list):
    sum_1 = 0
    for i in range(0, len(predict_list)):
        if predict_list[i] != test_list[i]:
            sum_1 += 1
    acc = (len(predict_list) - sum_1) / len(predict_list)
    return acc


def specificity_evaluate():

    pass


def sensitivity_evaluate():
    pass


def f1_score_evaluate():
    pass


def auc_evaluate():
    pass


def cal_confusion_matrix(test_list, predict_list, class_number):
    if class_number == 2:
        classification = "byclass"
    elif class_number > 2:
        classification = "multiclass"
    else:
        raise Exception("Not a classification")
    label_list = get_the_class_label(test_list)
    cm = metrics.confusion_matrix(test_list, predict_list, labels=label_list)
    accuracy = 0
    precision = 0
    sensitive = 0
    specificity = 0
    f1_score = 0
    auc = 0
    if classification == "byclass":
        tp = cm[0][0]
        fp = cm[0][1]
        fn = cm[1][0]
        tn = cm[1][1]
        accuracy = float('{:.2f}'.format((tp + tn) / (tp + fn + fp + tn)))
        precision = float('{:.2f}'.format(tp / (tp + fp)))
        sensitive = float('{:.2f}'.format(tp / (tp + fn)))
        specificity = float('{:.2f}'.format(tn / (fp + tn)))
        f1_score = float('{:.2f}'.format((2 * precision * sensitive) / (precision + sensitive)))
        auc = float('{:.2f}'.format(metrics.roc_auc_score(test_list, predict_list)))
        accuracy = str(accuracy)
        precision = str(precision)
        sensitive = str(sensitive)
        specificity = str(specificity)
        f1_score = str(f1_score)
        auc = str(auc)
    elif classification == "multiclass":
        auc = None
        cm_len = len(cm)
        # accuracy
        all_data = 0
        for first_index in range(0, cm_len):
            for second_index in range(0, cm_len):
                all_data += cm[first_index][second_index]
        predict_right = 0
        get_index = 0
        for first_index in range(0, cm_len):
            predict_right += cm[first_index][get_index]
            get_index += 1
        accuracy = float('{:.2f}'.format(predict_right / all_data))
        accuracy = (str(accuracy) + "      ")
        # precision
        precision_list = []
        precision = ""
        for i in range(0, cm_len):
            predict_true = 0
            for first_index in range(0, cm_len):
                predict_true += cm[first_index][i]
            real_true = cm[i][i]
            if predict_true == 0:
                preci = "None"
                precision_list.append(preci)
                precision += (str(label_list[i]) + ":" + preci + "      ")
            else:
                preci = float('{:.2f}'.format(real_true / predict_true))
                precision_list.append(preci)
                precision += (str(label_list[i]) + ":" + str(preci) + "      ")
        # sensitive
        sensitivity_list = []
        sensitive = ""
        for j in range(0, cm_len):
            ground_truth = 0
            for first_index in range(0, cm_len):
                ground_truth += cm[j][first_index]
            real_true1 = cm[j][j]
            sensi = float('{:.2f}'.format(real_true1 / ground_truth))
            sensitivity_list.append(sensi)
            sensitive += (str(label_list[j]) + ":" + str(sensi) + "      ")
        # specificity
        specificity = ""
        for s in range(0, cm_len):
            specificity += (str(label_list[s]) + ":" + "None" + "      ")
        # F1_score
        f1_score_list = []
        f1_score = ""
        for k in range(0, cm_len):
            prec = precision_list[k]
            sens = sensitivity_list[k]
            if (prec == "None") or (prec + sens == 0):
                score = "None"
                f1_score_list.append(score)
                f1_score += (str(label_list[k]) + ":" + score + "      ")
            else:
                score = float('{:.2f}'.format(((prec * sens) / (prec + sens)) * 2))
                f1_score_list.append(score)
                f1_score += (str(label_list[k]) + ":" + str(score) + "      ")
    return cm, accuracy, precision, sensitive, specificity, f1_score, auc, label_list


def draw_confusion_matrix(cm, label_list, file_time):
    if not os.path.exists("E:/pycharm-program/flex_mnist/result/" + file_time + "/confusion_matrix/"):
        os.makedirs("E:/pycharm-program/flex_mnist/result/" + file_time + "/confusion_matrix/")
    classes = len(cm)
    plt.subplots(figsize=(12,12))
    plt.imshow(cm,cmap=plt.cm.Blues)
    plt.xticks(range(len(cm)), label_list)
    plt.yticks(range(len(cm)), label_list)
    plt.colorbar()
    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('Prediction')
    ax.set_ylabel('Ground Truth')
    # plt.title(str(classes) + '  classes')
    for first_index in range(len(cm)):
        for second_index in range(len(cm[first_index])):
            plt.text(first_index,second_index,cm[second_index][first_index],C='red')
    plt.subplots_adjust(top=0.8,bottom=0.1)
    # plt.show()
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    plt.savefig("E:/pycharm-program/flex_mnist/result/" + file_time + "/confusion_matrix/" + time_now + ".png")


def make_the_result_form(accuracy, precision, sensitive, specificity, f1_score, auc, pair_list, file_time):
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    if not os.path.exists("E:/pycharm-program/flex_mnist/result/" + file_time + "/result/"):
        os.makedirs("E:/pycharm-program/flex_mnist/result/" + file_time + "/result/")
    data = {
        'accuracy':accuracy,
        'precision':precision,
        'sensitivity':sensitive,
        'specificity':specificity,
        'f1_score':f1_score,
        'AUC':auc
    }
    df = pd.DataFrame(data, index = pair_list)
    df.to_excel("E:/pycharm-program/flex_mnist/result/" + file_time + "/result/" + time_now + ".xlsx")

