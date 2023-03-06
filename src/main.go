package main

// A simple program demonstrating the spinner component from the Bubbles component library.

import (
    "fmt"
    "os"

    "github.com/charmbracelet/bubbles/spinner"
    tea "github.com/charmbracelet/bubbletea"
    "github.com/charmbracelet/lipgloss"
)


type errMsg error  // An interface for representing nasty errors. 😷

type model struct {
    spinner   spinner.Model // Spinner is a package from bubbles. 🧋
    quitting  bool          // Is the model quitting? 🧩
    err       error         // An interface for representing nasty errors. 😷
}

func initialModel() model {
	wheel := spinner.New()       // Create a new spinner we're calling wheel. 🎡
	wheel.Spinner = spinner.Dot  // One of the spinner settings is a Dot! 💠
	wheel.Style = lipgloss.NewStyle().Foreground(lipgloss.Color("205"))
	return model{spinner: wheel} // We re-use our model from before. 🌴
}

func main()  {
    // Prints out useless quote...
    // fmt.Println(quote.Go())
}
