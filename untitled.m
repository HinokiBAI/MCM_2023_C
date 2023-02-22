scatter3(letter',frequency',class',60,difficulty','filled');%  
ax = gca;%
ax.XDir = 'reverse';%
view(-31,14);%
xlabel('Letter occupancy');%
ylabel('Frequency');%
zlabel('AOA');%​
cb = colorbar;%                     
cb.Label.String = 'Difficulty';%