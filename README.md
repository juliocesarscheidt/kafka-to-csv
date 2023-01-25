# Kafka to CSV

```bash
export BOOTSTRAP_SERVERS='127.0.0.1:9092'
export TOPIC_NAME=''

# produce some data
declare -i counter
while true; do
  kafka-console-producer \
    --broker-list 127.0.0.1:9092 \
    --topic $TOPIC_NAME <<EOF
  {"id": $counter, "firstname": "Julio", "lastname": "Cesar", "countrycode": "BR"}
EOF
  let "counter=counter+1"
done

# run
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
