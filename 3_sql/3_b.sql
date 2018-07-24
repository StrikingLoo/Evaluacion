select
extract(month from date) as mes,
sum(impresiones) as impresiones,
sum(clicks) as clicks, 
1.0*sum(clicks)/sum(impresiones) as CTR_mes, --casteamos a float por si no todas las impresiones generan clicks.
sum( precio_promedio * impresiones )/sum(impresiones) as precio_promedio_impresiones,
avg(prediccion_ctr_promedio) as prediccion_ctr_promedio_mes --no me queda claro si asi se define la prediccion.

from daily_data
;
