SELECT * FROM reddy.crops;
use reddy;

SELECT crop,year,area from crops where crop="rice";

select count(*) from crops where area>2000;

select crop,year from crops where area>2000 and area<4000;

select * from crops where area>1300 and crop='maize';

select * from crops where area>1300 and crop='maize' or crop='sugarcane';

select * from crops order by area;

select year,min(area) from crops group by year;

select * from crops limit 9;

select * from crops order by area desc;
