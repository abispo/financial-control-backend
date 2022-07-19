package tests

import (
	"log"
	"os"
	"testing"

	"github.com/abispo/financial-control-backend/server"
	"github.com/gin-gonic/gin"
)

func SetUpRouter() *gin.Engine {
	router := server.NewRouter()
	return router
}

func TestMain(m *testing.M) {
	log.Println("Running tests")

	os.Exit(m.Run())
}
