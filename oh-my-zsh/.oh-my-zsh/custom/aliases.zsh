# pomcom <pomcom@mailbox.org>


# currently using zathura for pdf-viewing
alias open='zathura'


# lazy way for chaning alacritty-themes
alias at='alacritty-themes'

# tschuessi
alias ende='shutdown -r now'
alias lock='betterlockscreen -l'

# pbcopy and pbpaste
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

# neovim
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

# and forget stuff
alias quad='dig +short txt id.server.on.quad9.net'
alias c='clear'
