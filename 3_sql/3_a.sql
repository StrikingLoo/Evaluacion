create table volumen_diario as (
select 
account_id, 
tx_date,
sum(value) daily_volume --asumo que somos indiferentes a la naturaleza de la operacion, sea extraer o depositar

from transactions

group by account_id, tx_date
) ;



select acc.id as account_id, 
avg(daily_volume) as average_daily_volume --esto seria mucho mas complicado si tuviera que tener en cuenta todos los dias donde el volumen es 0

from accounts as acc
inner join volumen_diario as vol on (vol.account_id = acc.id)

group by acc.id

;


