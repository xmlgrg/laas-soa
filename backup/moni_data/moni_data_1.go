package moni_data

import (
	"log"
	"strconv"
	"time"
)

func TestChangeBuildProject() {
	globalActionChanMap["agent_action"] = make(chan string, 99999) // 最大承载数量
	for i := 0; true; i++ {
		productValue := strconv.Itoa(i)
		globalActionChanMap["agent_action"] <- productValue
		log.Println("product: " + productValue)
		time.Sleep(time.Duration(1) * time.Second)
	}
}
