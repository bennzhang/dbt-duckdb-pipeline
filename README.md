# dbt-duckdb-pipeline

## env setup
```
brew install duckdb
python3 -m venv env
source env/bin/activate
pip install dbt-duckdb
dbt init dbt-duckdb-pipeline
cd dbt-duckdb-pipeline
duckdb demo.duckdb  # create an empty db
```


## create files
```
profiles.yml
packages.yml
dbt_project.yml
sources.yml
```

## test file
run command below to generate sample data `data.csv`
```
python data_generator.py
```

## run
```
# add deps
dbt deps
# compile
dbt compile --target local --models video_visitors videos
# run
dbt run --target local --models video_visitors videos
# generate dbt doc
dbt docs generate
# show dbt doc
dbt docs serve --port 8001
```