package models

import (
	"gorm.io/gorm"
)

type PreRegister struct {
	gorm.Model
	UserID uint
}
