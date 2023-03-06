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
    /* We also return the model we made before */
	wheel := spinner.New()       // Create a new spinner we're calling wheel. 🎡
	wheel.Spinner = spinner.Dot  // One of the spinner settings is a Dot! 💠
	wheel.Style = lipgloss.NewStyle().Foreground(lipgloss.Color("205"))
	return model{spinner: wheel} // We re-use our model from before. 🌴
}

func (m model) Init() tea.Cmd {
    /* Tick one frame forward, advancing the frame animation */
	return m.spinner.Tick  // 🍬 <-- Eye candy
}


func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    /* Create a new ✨ function ✨ called update */
	switch msg := msg.(type) { // Switch based on whatever the type is of msg
	case tea.KeyMsg: // Key messages contain info about the keypress
		switch msg.String() { // Return a string repr of key msg
		case "q", "esc", "ctrl+c": // These are all encoded from msg.String()
			m.quitting = true // See previous comment on the model struct
			return m, tea.Quit // A special command that tells Bubble to exit!
		default:
			return m, nil // Nil, in this case, does simply nothing.
		}

	case errMsg: // Previously declared interface, not actually part of Go.
		m.err = msg // Part of the interface for our model as well
		return m, nil // A builtin.

	default:
		var cmd tea.Cmd // A 'Cmd' is an io operation that returns a message when complete.
		m.spinner, cmd = m.spinner.Update(msg)
		return m, cmd // We return. Always.
	}
}


func (m model) View() string {
	if m.err != nil {
		return m.err.Error() // Return the interface error but also calling Error() from it.
	}
    // m.spinner.View() (in this case) renders the model's view
	str := fmt.Sprintf("\n\n   %s Loading forever...press q to quit\n\n", m.spinner.View())
	if m.quitting {
		return str + "\n"
	}
	return str
}

func main() {
	program := tea.NewProgram(initialModel()) // Create our new program with the wheel model
	if _, err := program.Run(); err != nil { // exit if program.Run() yields an error that is not nil
		fmt.Println(err)
		os.Exit(1) // exit 'with' an error code. 0 would be without an error code. 1 is the most generic I believe.
	}
