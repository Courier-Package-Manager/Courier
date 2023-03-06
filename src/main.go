package main

import "fmt"
import "rsc.io/quote"
import "github.com/charmbracelet/charm/kv"

func generate_random_quote() {
    return quote.Go()
}

func hello() {
    // A freindly greeting, some might say!
    fmt.Println("Hello, world!")
}

func main()  {
    // Main function
    var quote = generate_random_quote()
    fmt.Println(quote)
}
