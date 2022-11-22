all: clean build server

server:
	hugo server -e production 

dev:
	hugo server --disableFastRender

build:
	hugo

clean:
	rm -rf plublic/*
