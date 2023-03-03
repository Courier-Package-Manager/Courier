cd ../..
mkdir libs
cd libs
git clone https://github.com/charmbracelet/glow.git
cd glow
go build
go install github.com/charmbracelet/gum@latest
