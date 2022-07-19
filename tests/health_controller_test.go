package tests

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
)

func TestHealthController(t *testing.T) {
	expected := gin.H{
		"message": "OK",
	}

	r := SetUpRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/health", nil)
	r.ServeHTTP(w, req)

	var response map[string]string
	err := json.Unmarshal([]byte(w.Body.String()), &response)

	value, _ := response["message"]

	assert.Nil(t, err)
	assert.Equal(t, expected["message"], value)
}
