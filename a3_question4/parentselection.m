function [firstParent, secondParent] = parentselection(population, fitnessList, numPopulation)
fitnessSum = sum(fitnessList);
probabilities = zeros(1, numPopulation);
runningProbSum = 0;
parent1 = zeros(3);
parent2 = zeros(3);
parent1Found = 0;
parent2Found = 0;
r1 = rand();
r2 = rand();

for i=1:numPopulation
    probabilities(i) = fitnessList(i)/fitnessSum;
end

for p=1:numPopulation
    runningProbSum = runningProbSum + probabilities(p);
    if(parent1Found == 1 && parent2Found == 1)
        break;
    end
    if(runningProbSum > r1 && parent1Found == 0)
        parent1 = population(p, :);
        parent1Found = 1;
    end
    if(runningProbSum > r2 && parent2Found == 0)
        parent2 = population(p, :);
        parent2Found = 1;
    end
end
firstParent = parent1;
secondParent = parent2;
end