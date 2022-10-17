all: clean build prod

prod:
	hugo server -e production 

dev:
	hugo server --disableFastRender

build:
	hugo

clean:
	rm -rf plublic/*
