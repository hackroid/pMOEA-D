function PMOEAD1(Global)
% <algorithm> <H-N>
% PMOEA/D1: A Multiobjective Evolutionary Algorithm Based on Decomposition
% kind --- 1 --- The type of aggregation function

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group. You are free to use the PlatEMO for
% research purposes. All publications which use this platform or any code
% in the platform should acknowledge the use of "PlatEMO" and reference "Ye
% Tian, Ran Cheng, Xingyi Zhang, and Yaochu Jin, PlatEMO: A MATLAB Platform
% for Evolutionary Multi-Objective Optimization [Educational Forum], IEEE
% Computational Intelligence Magazine, 2017, 12(4): 73-87".
%--------------------------------------------------------------------------

    %% Parameter setting
    kind = Global.ParameterSet(1);

    %% Generate the weight vectors
    [W,Global.N] = UniformPoint(Global.N,Global.M);
    T = ceil(Global.N/10);

    %% Detect the neighbours of each solution
    B = pdist2(W,W);
    [~,B] = sort(B,2);
    B = B(:,1:T);
    
    %% Generate random population
    Population = Global.Initialization();
    Z = min(Population.objs,[],1);

    %% Optimization
    while Global.NotTermination(Population)
       parfor l = 1: 3
            Optimization(Population,l,B,Z,kind,Global,W);
       end
    end
   
   


