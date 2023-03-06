package main

// A simple program demonstrating the spinner component from the Bubbles
// component library.

import (
	"fmt"
	"os"

	"github.com/charmbracelet/bubbles/spinner"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

type model struct {
   spinner   spinner.Model
   quitting  bool
   err       error
}

func main()  {
    // Prints out useless quote...
    // fmt.Println(quote.Go())
}
