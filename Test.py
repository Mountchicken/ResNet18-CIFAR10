import torch
import torch.nn.functional as F 
from ResNet18 import ResNet18
from Mydataset import get_test_data_loader
from torch.utils.tensorboard import SummaryWriter

MODEL_PATH='E:\LearningStuff\DLcode\Pytorch\CIFAR10\Models\BestModel.pkl'
TESTSET_LENGTH=10000
device='cuda' if torch.cuda.is_available() else 'cpu'

def test():
    test_loader=get_test_data_loader(100)
    network=ResNet18().to(device)
    state=torch.load(MODEL_PATH)
    param=state['network']
    network.load_state_dict(param)
    network.eval()
    total_correct=0
    total_loss=0
    with torch.no_grad():
        for images,labels in test_loader:
            images=images.to(device)
            labels=labels.to(device)
            preds=network(images)
            loss=F.cross_entropy(preds,labels)
            a=preds.argmax(dim=1).equal(labels)
            total_loss+=loss.item()
            total_correct+=preds.argmax(dim=1).eq(labels).sum().item()
        test_acc=total_correct/TESTSET_LENGTH
    return test_acc
if __name__=='__main__':
   print(test())