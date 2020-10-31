package component

import (
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
	"log"
	"strconv"
)

// 初始化mysql
func InitMysql(host string, port int, username string, password string, dbName string) *sql.DB {
	//"用户名:密码@[连接方式](主机名:端口号)/数据库名"
	connInfo := username + ":" + password + "@(" + host + ":" + strconv.Itoa(port) + ")/" + dbName + "?charset=utf8"
	db, _ := sql.Open("mysql", connInfo) // 设置连接数据库的参数
	//defer db.Close()                     //关闭数据库
	err := db.Ping() //连接数据库
	if err != nil {
		log.Println("init mysql occur error: ", err)
		panic(err)
	}
	return db
}

// 查询mysql数据
func QueryMysql(db *sql.DB, sqlInfo string, args ...interface{}) ([]map[string]interface{}, error) {
	var result []map[string]interface{} //返回的切片
	rows, err := db.Query(sqlInfo, args...)
	defer rows.Close()
	if err != nil {
		log.Println("query mysql occur error: ", err)
		return result, err
	}
	columns, _ := rows.Columns()
	columnLength := len(columns)
	cache := make([]interface{}, columnLength) //临时存储每行数据
	for index := range cache {                 //为每一列初始化一个指针
		var a interface{}
		cache[index] = &a
	}

	for rows.Next() {
		err = rows.Scan(cache...)
		if err != nil {
			log.Println("query mysql columns occur error: ", err)
			return result, err
		}
		item := make(map[string]interface{})
		for i, data := range cache {
			item[columns[i]] = *data.(*interface{}) //取实际类型
		}
		result = append(result, item)
	}
	log.Println(result[0]["name"])
	return result, nil
}

// 变更
func ChangeMysql() bool {
	var result = true
	/*
	   stu:=[2][2] string{{"3","ketty"},{"4","rose"}}
	   stmt,_:=db.Prepare("insert into stu values (?,?)")      //获取预处理语句对象
	   for _,s:=range stu{
	       stmt.Exec(s[0],s[1])            //调用预处理语句
	   }
	*/
	return result
}
