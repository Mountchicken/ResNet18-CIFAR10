import Mydataset
import torch
import torchvision
import torchvision.transforms as transforms
from ResNet18 import ResNet18
from Mydataset import get_test_data_loader
import matplotlib.pyplot as plt
from PIL import Image
PATH="E:\LearningStuff\DLcode\Pytorch\CIFAR10\Models"
def predict(image):
    if not torch.is_tensor(image):
        image=image.resize((32,32))  
        '''将图像转为tensor'''
        loader=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))])
        image=loader(image).unsqueeze(dim=0)
    ''' 预测 '''
    network=ResNet18()
    network.eval()
    state=torch.load(PATH+"\BestModel.pkl")
    param=state['network']
    network.load_state_dict(param)
    pred=network(image).argmax(dim=1)
    return pred

