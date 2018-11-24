function varargout = Iris_feature(Operation,Global,input)
% <problem> <DTLZ>
% Scalable Test Problems for Evolutionary Multi-Objective Optimization
% operator --- EAreal

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group. You are free to use the PlatEMO for
% research purposes. All publications which use this platform or any code
% in the platform should acknowledge the use of "PlatEMO" and reference "Ye
% Tian, Ran Cheng, Xingyi Zhang, and Yaochu Jin, PlatEMO: A MATLAB Platform
% for Evolutionary Multi-Objective Optimization [Educational Forum], IEEE
% Computational Intelligence Magazine, 2017, 12(4): 73-87".
%--------------------------------------------------------------------------

    switch Operation
%% Initialize the parameter setting, and randomly generate a population
        case 'init'
            % Set the default number of objectives
            Global.M        = 2;
            % Set the default number of decision variables
            Global.D        = 4;
            % Set the lower bound of each decision variable
            Global.lower    = zeros(1,Global.D);
            % Set the upper bound of each decision variable
            Global.upper    = ones(1,Global.D);
            % Set the default operator for this problem
            Global.operator = @EAreal;
            % Randomly generate a number of solutions' decision variables
            PopDec    = rand(input,Global.D);
            % Return the set of decision variables
            varargout = {PopDec};
%% 
        case 'value'
            PopDec = input;
            [N,D]  = size(PopDec);
            data = xlsread('./Problems/DTLZ/data.xlsx');
            dataM = data(:,1:4);
            labels = data(:,5);
            PopObj = PopDec(:,1:2);
            %part = rand(1);
            PopDec(PopDec>0.5)=1;
            PopDec(PopDec<=0.5)=0;
            for i = 1:N
                dataMat =[];
                c = 0;
%                 for j = 1:D
% %                     if PopDec(i,j)>0.5
% %                        dataMat=[dataMat dataM(:,j)];  
% %                        c = c +1;
% %                     end
%                     
%                 end
                c=sum(PopDec(i));
                if c==0
                    PopDec(i,:) = 1;
                    c=4;
                end
                dataMat=dataM(:,PopDec(i,:)==1);
                len = size(dataMat,1);
                k = 2;
                error = 0;
                % test data ratio
                Ratio = 0.3;
                numTest = Ratio*len;
                maxV = max(dataMat);
                minV = min(dataMat);
                range = maxV - minV;
                newdataMat = (dataMat-repmat(minV,[len,1]))./(repmat(range,[len,1]));
                for j = 1:numTest
%                     classifyresult = KNN(newdataMat(j,:),newdataMat(numTest:len,:),labels(numTest:len,:),k);
                    % classifyresult = knnclassify(newdataMat(j,:),newdataMat(numTest:len,:),labels(numTest:len,:),k,'euclidean','random');
                    knnModel = fitcknn(newdataMat(numTest:len,:),labels(numTest:len,:), 'NumNeighbors',k,'Standardize',1);
                    disp(knnModel)
                    res_mat = predict(knnModel, newdataMat(j,:));
                    disp(res_mat)
                    if(res_mat~=labels(j))
                        error = error+1;
                    end
                end
                erate = error/numTest;
                frate = c/4;
                PopObj(i,1) =erate;
                PopObj(i,2)=frate;
            end
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
%% Generate reference points on the true Pareto front
        case 'PF'
            % Generate a set of reference points on the true Pareto front
            f = UniformPoint(input,Global.M);
            f = f./repmat(sqrt(sum(f.^2,2)),1,Global.M);
            % Return the reference points
            varargout = {f};

    end
end