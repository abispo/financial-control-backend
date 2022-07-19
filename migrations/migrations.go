package migrations

import (
	"github.com/abispo/financial-control-backend/db"
	"github.com/abispo/financial-control-backend/models"
)

func Migrate() {
	err := db.GetDB().AutoMigrate(&models.User{}, &models.PreRegister{})

	if err != nil {
		panic(err)
	}

}
