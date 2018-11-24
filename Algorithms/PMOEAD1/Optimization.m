  
function Optimization(Population,l,B,Z,kind,Global,W)
     
        Population1 = Population(:);
        % For each solution
        for i = fix(Global.N/3)*(l-1)+1 : fix(Global.N/3)*l      
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
        
        
       
        for i = (l-1)*fix(Global.N/3)+1 : l*fix(Global.N/3) 
             Population(i) = Population1(i);
        end
        
    end

    