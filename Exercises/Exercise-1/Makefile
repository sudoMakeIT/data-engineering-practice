up:
	docker-compose up --build

down: 
	docker-compose down
	
clean:
	rm -rf downloads/
	docker-compose down
	docker-compose build --no-cache
	docker-compose up
