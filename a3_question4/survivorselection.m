function updatedPopulation = survivorselection(fitnessList, firstChild, secondChild, currentPopulation)
[~, indices] = sort(fitnessList, 'ascend');
smallestFitnessIdx = indices(1);
secondSmallestFitnessIdx = indices(2);
currentPopulation(smallestFitnessIdx, :) = firstChild;
currentPopulation(secondSmallestFitnessIdx, :) = secondChild;
updatedPopulation = currentPopulation;
end