# Kafka to CSV

```bash
export BOOTSTRAP_SERVERS=''
export TOPIC_NAME=''

docker-compose up -d --build
docker-compose logs -f

python3 src/main.py

cat src/output.csv
```

## Tests

```bash
docker-compose run kafka-csv pytest -v tests/
docker-compose run kafka-csv pytest --log-cli-level=debug -v src/tests/

python3 -m pytest -v src/tests/
python3 -m pytest --log-cli-level=debug -v src/tests/
```
