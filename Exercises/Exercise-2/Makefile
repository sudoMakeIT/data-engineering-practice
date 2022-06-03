
up:
	docker-compose up --build

down: 
	docker-compose down

clean:
	docker-compose down
	docker-compose build --no-cache
	docker-compose up

build:
	docker-compose build --no-cache

shell:
	docker exec -ti container bash

logs:
	docker logs -f --tail 100 container

pytest:
	docker exec container pytest
