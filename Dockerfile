# syntax=docker/dockerfile:1

FROM golang:1.18-alpine

RUN apk update && apk upgrade && apk add curl

WORKDIR /app

COPY go.mod ./
COPY go.sum ./


RUN go mod download

COPY *.go ./

RUN go build -o /financial-control-backend

EXPOSE 8001

RUN curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s -- -b $(go env GOPATH)/bin


CMD [ "air" ]
