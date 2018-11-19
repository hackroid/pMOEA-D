function MOEAD(Global)
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
        Population1 = Population(:);
        Population2 = Population(:);
        % For each solution
        for i = 1 : fix(Global.N/3)      
            % Choose the parents
            P = B(i,randperm(size(B,2)));

            % Generate an offspring
            Offspring = Global.Variation(Population(P(1:2)),1);

            % Update the ideal point
            Z = min(Z,Offspring.obj);

            % Update the neighbours
            switch kind
                case 1
                    % PBI approach
                    normW   = sqrt(sum(W(P,:).^2,2));
                    normP   = sqrt(sum((Population(P).objs-repmat(Z,T,1)).^2,2));
                    normO   = sqrt(sum((Offspring.obj-Z).^2,2));
                    CosineP = sum((Population(P).objs-repmat(Z,T,1)).*W(P,:),2)./normW./normP;
                    CosineO = sum(repmat(Offspring.obj-Z,T,1).*W(P,:),2)./normW./normO;
                    g_old   = normP.*CosineP + 5*normP.*sqrt(1-CosineP.^2);
                    g_new   = normO.*CosineO + 5*normO.*sqrt(1-CosineO.^2);
                case 2
                    % Tchebycheff approach
                    g_old = max(abs(Population(P).objs-repmat(Z,T,1)).*W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z),T,1).*W(P,:),[],2);
                case 3
                    % Tchebycheff approach with normalization
                    Zmax  = max(Population.objs,[],1);
                    g_old = max(abs(Population(P).objs-repmat(Z,T,1))./repmat(Zmax-Z,T,1).*W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z)./(Zmax-Z),T,1).*W(P,:),[],2);
                case 4
                    % Modified Tchebycheff approach
                    g_old = max(abs(Population(P).objs-repmat(Z,T,1))./W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z),T,1)./W(P,:),[],2);
            end
            Population(P(g_old>=g_new)) = Offspring;
        end
        for i = 1+fix(Global.N/3) : 2*fix(Global.N/3)      
            % Choose the parents
            P = B(i,randperm(size(B,2)));
            
            % Generate an offspring
            Offspring = Global.Variation(Population1(P(1:2)),1);

            % Update the ideal point
            Z = min(Z,Offspring.obj);

            % Update the neighbours
            switch kind
                case 1
                    % PBI approach
                    normW   = sqrt(sum(W(P,:).^2,2));
                    normP   = sqrt(sum((Population1(P).objs-repmat(Z,T,1)).^2,2));
                    normO   = sqrt(sum((Offspring.obj-Z).^2,2));
                    CosineP = sum((Population1(P).objs-repmat(Z,T,1)).*W(P,:),2)./normW./normP;
                    CosineO = sum(repmat(Offspring.obj-Z,T,1).*W(P,:),2)./normW./normO;
                    g_old   = normP.*CosineP + 5*normP.*sqrt(1-CosineP.^2);
                    g_new   = normO.*CosineO + 5*normO.*sqrt(1-CosineO.^2);
                case 2
                    % Tchebycheff approach
                    g_old = max(abs(Population1(P).objs-repmat(Z,T,1)).*W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z),T,1).*W(P,:),[],2);
                case 3
                    % Tchebycheff approach with normalization
                    Zmax  = max(Population1.objs,[],1);
                    g_old = max(abs(Population1(P).objs-repmat(Z,T,1))./repmat(Zmax-Z,T,1).*W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z)./(Zmax-Z),T,1).*W(P,:),[],2);
                case 4
                    % Modified Tchebycheff approach
                    g_old = max(abs(Population1(P).objs-repmat(Z,T,1))./W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z),T,1)./W(P,:),[],2);
            end
            Population1(P(g_old>=g_new)) = Offspring;
        end
        for i = 1+2*fix(Global.N/3) : Global.N      
            % Choose the parents
            P = B(i,randperm(size(B,2)));

            % Generate an offspring
            Offspring = Global.Variation(Population2(P(1:2)),1);

            % Update the ideal point
            Z = min(Z,Offspring.obj);

            % Update the neighbours
            switch kind
                case 1
                    % PBI approach
                    normW   = sqrt(sum(W(P,:).^2,2));
                    normP   = sqrt(sum((Population2(P).objs-repmat(Z,T,1)).^2,2));
                    normO   = sqrt(sum((Offspring.obj-Z).^2,2));
                    CosineP = sum((Population2(P).objs-repmat(Z,T,1)).*W(P,:),2)./normW./normP;
                    CosineO = sum(repmat(Offspring.obj-Z,T,1).*W(P,:),2)./normW./normO;
                    g_old   = normP.*CosineP + 5*normP.*sqrt(1-CosineP.^2);
                    g_new   = normO.*CosineO + 5*normO.*sqrt(1-CosineO.^2);
                case 2
                    % Tchebycheff approach
                    g_old = max(abs(Population2(P).objs-repmat(Z,T,1)).*W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z),T,1).*W(P,:),[],2);
                case 3
                    % Tchebycheff approach with normalization
                    Zmax  = max(Population2.objs,[],1);
                    g_old = max(abs(Population2(P).objs-repmat(Z,T,1))./repmat(Zmax-Z,T,1).*W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z)./(Zmax-Z),T,1).*W(P,:),[],2);
                case 4
                    % Modified Tchebycheff approach
                    g_old = max(abs(Population2(P).objs-repmat(Z,T,1))./W(P,:),[],2);
                    g_new = max(repmat(abs(Offspring.obj-Z),T,1)./W(P,:),[],2);
            end
            Population2(P(g_old>=g_new)) = Offspring;
        end
        for i = 1+fix(Global.N/3) : 2*fix(Global.N/3) 
             Population(i) = Population1(i);
        end
        for i = 1+2*fix(Global.N/3) : Global.N 
             Population(i) = Population2(i);
        end
    end
end