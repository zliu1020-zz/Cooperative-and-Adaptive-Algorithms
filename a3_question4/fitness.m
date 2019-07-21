function result = fitness(population, numPopulation)
fitness_result = zeros(1, numPopulation);
scores = zeros(50, 4);
for i=1:numPopulation
	currentSolution = population(i, :);
	[ISE,t_r,t_s,M_p] = perfFCN(transpose(currentSolution));
    scores(i, 1) = ISE;
    scores(i, 2) = t_r;
    scores(i, 3) = t_s;
    scores(i, 4) = M_p;
    
    if(isnan(scores(i, 1)) == 1 || isnan(scores(i, 2)) == 1 || isnan(scores(i, 3)) == 1 || isnan(scores(i, 4)) == 1)
    else
        currentFitness = 1/(0.25*(ISE/2000) + 0.25*(t_r/20) + 0.25*(t_s/1000) + 0.25*(M_p/1000));
        fitness_result(i) = currentFitness;
    end
end
result = fitness_result;
end