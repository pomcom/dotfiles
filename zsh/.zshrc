
export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH=$PATH:~/opt/bin

#Android Stuff -currently only needed for Appium :(
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools


# Path to your oh-my-zsh installation.
export ZSH="/home/pomcom/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    autojump
    last-working-dir
    )

source $ZSH/oh-my-zsh.sh
source /home/pomcom/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

#JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-1.14.0-openjdk-amd64
export PATH="$HOME/.local/bin:$PATH"

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
export PATH=$PATH:$GOPATH/bin
