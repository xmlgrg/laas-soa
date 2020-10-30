package main

import (
	"flag"
	"log"
	"net/http"
	"strconv"
	"time"
)

var globalActionChanMap = map[string]chan string{} // 全局消息数据

var addr = flag.String("addr", "localhost:8080", "http service address")

func testChangeBuildProject() {
	globalActionChanMap["agent_action"] = make(chan string, 99999) // 最大承载数量
	for i := 0; true; i++ {
		productValue := strconv.Itoa(i)
		globalActionChanMap["agent_action"] <- productValue
		log.Println("product: " + productValue)
		time.Sleep(time.Duration(1) * time.Second)
	}
}
func doInit() {
	go testChangeBuildProject()
}
func main() {
	doInit()
	flag.Parse()
	log.SetFlags(0)
	log.Println("server started")
	InitRoute()
	log.Fatal(http.ListenAndServe(*addr, nil))
}
