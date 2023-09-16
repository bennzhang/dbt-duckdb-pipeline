
{{ config(
    materialized='external',
    location='videos.csv',
    delimiter=','
   ) 
}}
select date_trunc('MONTH', day) as month, sum(views) as views
from {{ ref('video_visitors') }}
group by 1
