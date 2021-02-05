import torch 
import torch.nn as nn
'''构建VGG11，VGG13，VGG16，VGG19'''

cfg={
    'VGG11': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'VGG13': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'VGG16': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],
    'VGG19': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M'],

}

class VGG(nn.Module):
    '''初始化网络参数'''
    def __init__(self,vgg_name):
        super(VGG,self).__init__()
        self.features=self._make_layers(cfg[vgg_name])
        '''对于CIFAR10，输入图片为32x32，经过5次maxpool后，大小变为1x1。且
        不在VGG中不用使用全连接层（作用不大），只用一层softmax层即可'''
        self.calssfier=nn.Linear(512,10)
    def forward(self,x):
        out=self.features(x)
        out=out.view(out.size(0),-1) #[B,C,H,W]转换为[B,C*H*W]
        out=self.calssfier(out)
        return out
    
    def _make_layers(self,cfg):
        layers=[]
        in_channels=3 #输入彩色图片
        for x in cfg:
            if x=='M':
                layers+=[nn.MaxPool2d(kernel_size=2,stride=2)]
            else:
                layers+=[nn.Conv2d(in_channels,x,kernel_size=3,padding=1),
                         nn.BatchNorm2d(x),
                         nn.ReLU(inplace=True)] #不额外创建变量，减少内春占用
                in_channels=x
        layers+=[nn.AvgPool2d(kernel_size=1,stride=1)] #reshape (B, 512, 1, 1) array into (B , 512) array.
        return nn.Sequential(*layers)
                        
