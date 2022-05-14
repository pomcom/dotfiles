# pomcom <pomcom@mailbox.org>

# currently using zathura for pdf-viewing
alias open='zathura'

alias at='alacritty-themes'

alias ende='shutdown -r now'
alias lock='betterlockscreen -l'

# pbcopy and pbpaste
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

alias v='nvim'
alias vim='nvim'

## override oh my zsh default alias
alias ll='lsd -lh'
alias ls='lsd'

## better cat
alias cat='bat'


#i am lazy
alias initscan='nmap -sC -sV -Pn -oN'
alias deepscan='nmap -T4 -n -Pn -p- -o'
alias c='clear'
alias v.kb='vboxmanage startvm Kali-Linux-ctf'
alias v.wb='vboxmanage startvm windows_clean'

alias pray='sudo pacman -Syu'
alias lg='lazygit'

alias hg='history | grep'
