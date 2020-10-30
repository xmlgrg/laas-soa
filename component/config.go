package component

import (
	"github.com/spf13/viper"
	"os"
)

func LoadConfig() *viper.Viper {
	path, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	config := viper.New()
	config.AddConfigPath(path)   //设置读取的文件路径
	config.SetConfigName("conf") //设置读取的文件名
	config.SetConfigType("yaml") //设置文件的类型
	if err := config.ReadInConfig(); err != nil {
		panic(err)
	}
	return config
}
