E = [-1170.31429616,-1171.07865896,-1171.43959399,-1171.53663541,-1171.46615680,-1171.29440609,-1171.06824634,-1170.82017855,-1170.57530569];
disp = linspace(-0.3,0.5,9);
p = polyfit(disp(3:5),E(3:5),2);

figure1 = figure(1);
plot(disp,E-E(4),'-o', 'LineWidth', 1.2)
hold
plot(disp,polyval(p,disp)-E(4), 'LineWidth', 1.2)
ax = gca;
ax.FontSize = 12;
%xlim([0.3 1.0]);
%ylim([0 31]);
legend('Actual', 'Harmonic', 'Location', 'northwest')
xlabel(sprintf('Displacement from equilibrium (%c)',197), 'FontSize', 15, 'Interpreter', 'tex')
ylabel('Energy above min (eV)', 'FontSize', 15, 'Interpreter', 'tex')