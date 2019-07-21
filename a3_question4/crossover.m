function [firstChild, secondChild] = crossover(firstParent, secondParent, pc)
r = rand();
if(r > pc)
   fChild = firstParent;
   sChild = secondParent;
else
   fChild(1) = round(r*firstParent(1) + (1-r)*secondParent(1), 2); 
   fChild(2) = round(r*firstParent(2) + (1-r)*secondParent(2), 2);
   fChild(3) = round(r*firstParent(3) + (1-r)*secondParent(2), 2);
   
   sChild(1) = round((1-r)*firstParent(1) + r*secondParent(1), 2); 
   sChild(2) = round((1-r)*firstParent(2) + r*secondParent(2), 2);
   sChild(3) = round((1-r)*firstParent(3) + r*secondParent(2), 2);
end
firstChild = fChild;
secondChild = sChild;
end