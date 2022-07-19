package main

import (
	"github.com/abispo/financial-control-backend/db"
	"github.com/abispo/financial-control-backend/migrations"
	"github.com/abispo/financial-control-backend/server"
)

func main() {
	db.Init()
	migrations.Migrate()
	server.Init()
}
