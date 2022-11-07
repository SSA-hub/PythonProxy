docker compose up -d
cd test
py -m spamer
cd..
sleep(100)
docker compose stop target3
sleep(100)
docker compose restart target3