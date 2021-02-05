import itertools
import numpy as numpy
import matplotlib.pyplot as plt
import torch
from Mydataset import get_test_data_loader
from ResNet18 import ResNet18

CLASSES=['飞机','汽车','鸟','猫','鹿','狗','青蛙','马','船','卡车']
CATEGORY_Num=10

def plot_confusion_matrix(cm,classes,normalize=False,title='Confusion matrix',cmp=plt.cm.Blues):
    if normalize:
        cm=cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
    print(cm)
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks=np.arange(len(classes))
    plt.xticks(tick_marks,classes,rotation=45)
    plt.yticks(tick_marks,classes)

    fmt='.2f' if normalize else 'd'
    thresh=cm.max()/2.
    for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,format(cm[i,j],fmt),
        horizontalalignment="center",
        color="white" if cm[i,j]>thresh else "black"
        )
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

def ConfusionMatrix(network,loader):
    all_preds=torch.tensor([])
    all_labels=torch.tensor([])
    network.eval()
    for batch in loader:
        images,labels=batch
        preds=network(images)
        all_preds=torch.cat((all_preds,preds),dim=0)
        all_labels=torch.cat((all_labels,labels),dim=0)
    stacked=torch.stack((all_labels,all_preds.argmax(dim=1)),dim=1)
    cm=torch.zeros(CATEGORY_Num,CATEGORY_Num,dtype=torch.int64)
    for p in stacked:
        j,k=p.tolist()
        cm[j,k]=cm[j,k]+1
    plot_confusion_matrix(cm,CLASSES,normalize=False,title='Confusion matrix',cmp=plt.cm.Blues)

if __name__=='__main__':
    loader=get_test_data_loader(256)
    network=ResNet18()
    state=torch.load('E:\LearningStuff\DLcode\Pytorch\CIFAR10\Models\BestModel.pkl')
    param=state['network']
    network.load_state_dict(param)
    ConfusionMatrix(network,loader)