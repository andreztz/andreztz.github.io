all: clean build server

server:
	hugo server -e production 

dev:
	hugo server --disableFastRender --buildDrafts

build:
	hugo

clean:
	rm -rf plublic/*
