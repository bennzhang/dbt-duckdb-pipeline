
{{ config(
    materialized='external',
    location='videos.csv',
    delimiter=','
   ) 
}}
select count(distinct video_id) videos
from {{ ref('video_visitors') }}
