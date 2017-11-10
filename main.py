import numpy as np
import os
import argparse
import copy
import opts
import utils
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as modelzoo
import models.__init__ as init
import datasets.data_loader as loader
#from tensorboard_logger import Logger

parser = opts.myargparser()


def main():
    global opt, best_studentprec1

    opt = parser.parse_args()
    opt.logdir = opt.logdir + '/' + opt.name
   # logger = Logger(opt.logdir)

    print(opt)

    print('Loading models...')
    teacher = init.load_model(opt, 'teacher')
    print("Done loading from other file")
    teacher = init.setup(teacher, opt, 'teacher')
    print(teacher)

    # if opt.resume:
    #     if os.path.isfile(opt.resume):
    #         model, optimizer, opt, best_prec1 = init.resumer(
    #             opt, model, optimizer)
    #     else:
    #         print("=> no checkpoint found at '{}'".format(opt.resume))
    dataloader = loader.loadCIFAR10(opt)
    print dataloader
    train_loader = dataloader['train_loader']
    val_loader = dataloader['val_loader']


if __name__ == '__main__':
    main()
