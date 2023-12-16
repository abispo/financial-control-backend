FROM golang:1.18-alpine AS base
WORKDIR /app

ENV GO111MODULE="on"
ENV GOOS="linux"
ENV CGO_ENABLED=0

# System dependencies
RUN apk update \
    && apk add --no-cache \
    ca-certificates \
    git \
    curl \
    && update-ca-certificates

### Development with hot reload and debugger
FROM base AS dev
WORKDIR /app

COPY go.mod /app

RUN go install github.com/go-delve/delve/cmd/dlv@latest

# Hot reloading mod
RUN curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s -- -b $(go env GOPATH)/bin
EXPOSE 8080
EXPOSE 2345

RUN git config --global --add safe.directory /app

ENTRYPOINT ["air"]

### Executable builder
FROM base AS builder
WORKDIR /app

# Application dependencies
COPY . /app
RUN go mod download \
    && go mod verify

RUN go build -o financial-control-backend -a .

### Production
FROM alpine:3.18.3

RUN apk update \
    && apk add --no-cache \
    ca-certificates \
    tzdata \
    && update-ca-certificates

# Copy executable
COPY --from=builder /app/financial-control-backend /usr/local/bin/financial-control-backend
EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/financial-control-backend"]
