import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

device = torch.device('cuda' if torch.cuda.is_available else 'cpu')

imput_size = 784
hidden_size = 100
num_classes = 10
num_epochs = 2
batch_size = 1000
learning_rate = 0.001

train_dataset = torchvision.datasets.MNIST(root='./data', train=True,
    transform=transforms.ToTensor(), download = True)

test_dataset = torchvision.datasets.MNIST(root='./data', train=False,
    transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size,
    shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size,
    shuffle=False)

example = iter(train_loader)
samples, labels = next(example)
print(samples.shape, labels.shape)

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(samples[i][0], cmap='grey')
plt.show()