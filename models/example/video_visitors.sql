
{{ config(
    materialized='external',
    location='visitors.csv',
    delimiter=','
   ) 
}}

select video_id, count(distinct visitor_id) as visitors
from  {{ source('local', 'data') }}
group by 1

