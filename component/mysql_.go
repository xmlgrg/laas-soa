package component

import (
	"container/list"
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"strconv"
)

var db sql.DB

// 初始化mysql
func Init(ip string, port int, username string, password string, dbName string) {
	//"用户名:密码@[连接方式](主机名:端口号)/数据库名"
	connInfo := username + ":" + password + "@(" + ip + ":" + strconv.Itoa(port) + ")/" + dbName
	db, _ := sql.Open("mysql", connInfo) // 设置连接数据库的参数
	defer db.Close()                     //关闭数据库
	err := db.Ping()                     //连接数据库
	if err != nil {
		panic(err)
	}
}

// 查询
func Query(sql string, args ...interface{}) {
	rows, _ := db.Query(sql, args) //获取所有数据
	list.New()
	var id, name string
	for rows.Next() { //循环显示所有的数据
		rows.Scan(&id, &name)
		fmt.Println(id, "--", name)
	}
}

// 变更
func Change() {
	/*
	   stu:=[2][2] string{{"3","ketty"},{"4","rose"}}
	   stmt,_:=db.Prepare("insert into stu values (?,?)")      //获取预处理语句对象
	   for _,s:=range stu{
	       stmt.Exec(s[0],s[1])            //调用预处理语句
	   }
	*/
}
