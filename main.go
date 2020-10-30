package main

import (
	"flag"
	"github.com/laashub-soa/laas-soa/component"
	"log"
	"net/http"
)

var config = component.LoadConfig()
var globalActionChanMap = map[string]chan string{} // 全局消息数据

func main() {
	flag.Parse()
	log.SetFlags(0)
	log.Println("server started")
	InitRoute()
	var addr = flag.String("addr", "localhost:8080", "http service address")
	log.Fatal(http.ListenAndServe(*addr, nil))
}
