function geneticalgorithm()
	numGeneration = 150;
	numPopulation = 50;
	pc = 0.6;
	pm = 0.25;
    bestFitness = zeros(1, numGeneration);
    population = zeros(numPopulation, 3);
    bounds = [2 18; 1.05 9.42; 0.26 2.37];
    
    for p=1:numPopulation
        for n = 1:3
            lower = bounds(n, 1);
            upper = bounds(n, 2);
            population(p, n) = lower + (upper-lower)*rand;   
        end
    end

	for j = 1:numGeneration
        fitnessList = fitness(population, numPopulation);
        [firstParent, secondParent] = parentselection(population, fitnessList, numPopulation);
        [firstChild, secondChild] = crossover(firstParent, secondParent, pc);
        firstChild = mutation(firstChild, pm);
        secondChild = mutation(secondChild, pm);
        population = survivorselection(fitnessList, firstChild, secondChild, population);
        fitnessList = fitness(population, numPopulation);
        [bestSolutionFound, bestIdxFound] = bestsolution(fitnessList, population);
        bestFitnessFound = fitnessList(bestIdxFound);
        bestFitness(j) = bestFitnessFound;
        disp('Generation = ');
        disp(j);
        disp('bestSolutionFound = ');
        disp(bestSolutionFound);
        disp('bestFitnessFound = ');
        disp(bestFitnessFound);
    end
    
    plot(linspace(1,numGeneration,numGeneration), bestFitness);
    title('Fitness vs Generation');
    xlabel('Generation');
    ylabel('Fitness');
	
end