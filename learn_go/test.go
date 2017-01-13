package main

import "net/http"
import "fmt"
import "io/ioutil"
import "net/url"


func main() {
    resp, err := http.PostForm("http://192.168.50.46:9528/crazybot/api/chat",
    url.Values{"botkey": {"5870a3a11d41c80f8bf71918"}, "question": {"dedea"}})

    if err != nil {
        // handle error
    }

    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        // handle error
    }

    fmt.Println(string(body))

}
