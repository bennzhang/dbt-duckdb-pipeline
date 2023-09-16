
{{ config(
    materialized='external',
    location='visitors.csv',
    delimiter=','
   ) 
}}

select CAST(time_stamp AS DATE) as day, video_id, count(1) as views
from  {{ source('local', 'data') }}
group by 1,2