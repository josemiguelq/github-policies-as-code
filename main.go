package main

import (
// 	"io"
// 	"net/http"
	"log"
	"fmt"
	"os"
	"io/ioutil"
)

type Repository struct {
	HasIssues bool `json: "has_issues"`
}

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    log.Println(token)

	files, err := ioutil.ReadDir("./resources")
    if err != nil {
        log.Fatal(err)
    }

    for _, f := range files {
//         file, _ := ioutil.ReadFile(f)
//         data := CatlogNodes{}
//         _ = json.Unmarshal([]byte(file), &data)

        fmt.Println(f.read())
    }
}
