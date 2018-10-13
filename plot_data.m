clear all
clc

dirname = '2018';
listing = dir(dirname);

volumes = [];
prices = [];
for i=3:length(listing)
    filename = listing(i).name;
    filedata = table2array(readtable(strcat(dirname,'/',filename),'TreatAsEmpty','–'));
    volumes = [volumes; filedata(:,1)];
    prices = [prices; filedata(:,2)];
end

figure

subplot(2,1,1)
plot(prices)
xlabel('Time [h]')
ylabel('Prices [EUR/MWh]')
grid

subplot(2,1,2)
plot(volumes)
xlabel('Time [h]')
ylabel('Volume [MWh]')
grid