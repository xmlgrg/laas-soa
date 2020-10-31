package main

import (
	"database/sql"
	"flag"
	"github.com/laashub-soa/laas-soa/backup/component"
	"log"
	"net/http"
)

var config = component.LoadConfig()
var db *sql.DB
var globalActionChanMap = map[string]chan string{} // 全局消息数据

func main() {
	db = component.InitMysql(config.Get("mysql.host").(string), config.Get("mysql.port").(int), config.Get("mysql.username").(string), config.Get("mysql.password").(string), config.Get("mysql.db_name").(string))
	log.Println(db)
	component.QueryMysql(db, `select * from tristan`)
	flag.Parse()
	log.SetFlags(0)
	log.Println("server started at: http://localhost:8080")
	InitRoute()
	var addr = flag.String("addr", "localhost:8080", "http service address")
	log.Fatal(http.ListenAndServe(*addr, nil))
}
