package main

import (
	"github.com/laashub-soa/laas-soa/service"
	"net/http"
)

func InitRoute() {
	http.HandleFunc("/insert_business", service.InsertBusiness)
	http.HandleFunc("/select_consume_business", service.SelectConsumeBusiness)
	http.HandleFunc("/select_data", service.SelectData)
}
