function mutation_result = mutation(current, pm)
r = [rand(), rand(), rand()];
bounds = [2 18; 1.05 9.42; 0.26 2.37];
result = zeros(1, 3);
for n = 1:length(r)
    randNum = r(n);
    
    if(randNum > pm)
        result(n) = current(n);
    else
        lower = bounds(n, 1);
        upper = bounds(n, 2);
        result(n) = round(lower + (upper-lower)*rand, 2);
    end   
end
mutation_result = result;
end