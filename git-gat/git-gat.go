package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "os/exec"
    "strings"
)

func getUrl(path string) string {
  // find origin URL of a repository from .git/config file
	data, err := ioutil.ReadFile(path + "/config")
	if err == nil{
		for _, line := range strings.Split(string(data), "\n"){
			parts := strings.Split(line, "url = ")
			if len(parts) > 1{
				return parts[1]
			}
		}
	}
	return ""
}

func getStatus(url string) int {
  // get http status code of a url
	resp, err := http.Get(url)
	if err == nil{
		return resp.StatusCode
	}
	return 0
}

func main() {
	filterPublic := true
	seed := "/home/"
	if len(os.Args) > 1{
		seed = os.Args[1]
		if len(os.Args) > 2 && os.Args[2] == "all" {
			filterPublic = false
		}
	}
    out, err := exec.Command("find", seed, "-name", ".git").Output()
    if err != nil {
    	os.Exit(1)
    }
    for _, path := range strings.Split(string(out), "\n"){
    	url := getUrl(path)
    	if strings.HasPrefix(url, "http"){
    		if filterPublic && getStatus(url) == 200{
    			continue
    		}
    		fmt.Printf("%s,%s\n", path, url)
    	}
    }
}
