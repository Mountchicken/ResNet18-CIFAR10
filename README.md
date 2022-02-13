# ResNet18-CIFAR10
ResNet18 on CIFAR10 reachs 95.09% Accuracy on TestSet

## 项目结构
### 文件

- `ResNet18.py`: 定义模型
- `Mydataset.py`:定义数据集以及dataloader，初次运行时请修改其中的`DATASET_PATH`以读取CIFAR10数据集
- `Train.py`: 训练模型，初次运行时请修改其中的`SAVED_PATH`指定模型保存地址
- `Test.py`: 测试模型在训练集准确率
- `ConfusuinMatrix.py`: 绘制单个模型的混淆矩阵
- `Predict.py`: 用以预测单幅图像
- `main_gui.py,widget.ui,ui_widget.py`: GUI封装代码

### 文件夹
- `Models`: 存放预训练的模型参数

## 如何使用

### 如何使用tensorboard进行调参训练
- `pip install tensorboard`
- 在`Train.py`中修改 `TestParameters`，往列表中加入训练参数，代码会自动对所有可能的训练参数进行训练
- 训练结束后，在Anaconda Prompt中执行命令行 ` tensorboard --logdir=runs`

### 如何启动GUI

- `pip install PyQt5`
- `pip install PyQt5-tools`
- 运行文件`main_gui.py`

## 权重下载
[百度云：提取码eh6h](https://pan.baidu.com/s/1VgOpetLpongi74olRT6I5Q)

## 联系方式
- mountchicken@outlook.com



