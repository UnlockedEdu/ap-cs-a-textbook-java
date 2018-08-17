build:
	docker build -t brainz .
run-textbook:
	docker run --rm -v `pwd`/AP-CS-A/textbook:/data -it -p 8000:8000 brainz
run-curriculum:
	docker run --rm -v `pwd`/AP-CS-A/curriculum:/data -it -p 8000:8000 brainz
