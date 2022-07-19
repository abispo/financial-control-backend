package db

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"strings"

	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var db *gorm.DB

func Init() {
	var sb strings.Builder
	var _, b, _, _ = runtime.Caller(0)
	var err error = nil

	err = godotenv.Load()

	if err != nil {
		log.Fatal("Error loading .env file")
	}

	root_path := filepath.Join((b), "../../")

	environment := os.Getenv("ENVIRONMENT")

	if environment == "test" {
		fmt.Fprintf(&sb, "%s", "sqlite:///")
		fmt.Fprintf(&sb, "%s", root_path)
		fmt.Fprintf(&sb, "db.sqlite3")

		db, err = gorm.Open(sqlite.Open(sb.String()), &gorm.Config{})

	} else if environment == "development" {
		fmt.Fprintf(&sb, "host=%s ", os.Getenv("DB_HOST"))
		fmt.Fprintf(&sb, "user=%s ", os.Getenv("DB_USER"))
		fmt.Fprintf(&sb, "password=%s ", os.Getenv("DB_PASSWORD"))
		fmt.Fprintf(&sb, "port=%s ", os.Getenv("DB_PORT"))
		fmt.Fprintf(&sb, "dbname=%s ", os.Getenv("DB_NAME"))

		db, err = gorm.Open(postgres.Open(sb.String()), &gorm.Config{})
	} else {
		panic("Erro")
	}

	if err != nil {
		log.Fatalln(err)
	}
}

func GetDB() *gorm.DB {
	return db
}
