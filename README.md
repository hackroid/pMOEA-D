# pMOEA-D

> Part of code(moead.py knapsack.py) were directly used and changed from [moead-py](https://github.com/mbelmadani/moead-py) under LGPL-3.0.
> This Porject is base on the code of [BIMK/PlatEMO](https://github.com/BIMK/PlatEMO), please follow the instruction and copyright of the original author [link](https://github.com/BIMK/PlatEMO/blob/master/README.md).



## Usage

1. 框架没有变动
2. Parallel run by time函数最后添加一个参数ratio,默认是0。 Ratio代表overlapping的比例。比如0.1代表会有10%的部分是overlapping的。
3. 程序运行的结果会存到/result文件夹内。结果是原始数据，可以调用clean result来过滤结果。过滤后的文件也要存在result里。Draw picture函数是对过滤后的结果画图的程序，使用matlibplot的库。可以自己学习一下。
4. get_dimnsion是用来计算测试文件的feature个数。

## Reference

[1] Ye Tian, Ran Cheng, Xingyi Zhang, and Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective Optimization [Educational Forum], IEEE Computational Intelligence Magazine, 2017, 12(4): 73-87

