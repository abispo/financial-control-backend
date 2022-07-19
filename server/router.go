package server

import (
	"github.com/abispo/financial-control-backend/controllers"
	"github.com/gin-gonic/gin"
)

func NewRouter() *gin.Engine {
	router := gin.Default()
	router.SetTrustedProxies(nil)

	v1 := router.Group("")
	v1.Use(gin.Logger())
	v1.Use(gin.Recovery())

	health := new(controllers.HealthController)

	router.GET("/health", health.Status)
	return router
}
