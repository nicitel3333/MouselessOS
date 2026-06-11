# history
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt share_history

# env
export PATH="$HOME/.local/bin:$PATH"
export EDITOR=nvim
export VISUAL=nvim

# vi mode
bindkey -v
export KEYTIMEOUT=1
export FUNCNEST=1000

# plugins
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# tools
eval "$(atuin init zsh)"
eval "$(zoxide init zsh)"
eval "$(starship init zsh)"

# keybindings
bindkey -M vicmd ';' atuin-search-vicmd
bindkey -M vicmd 'k' up-line-or-history
bindkey -M vicmd 'j' down-line-or-history
bindkey '\t' autosuggest-accept
bindkey '\e[Z' expand-or-complete

# aliases
alias ls='eza --icons'
alias ll='eza -lah --icons --git'
alias vim='nvim'
alias off='poweroff'
alias syu='sudo pacman -Syu && yay'
