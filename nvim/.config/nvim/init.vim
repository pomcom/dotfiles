call plug#begin('~/.local/share/nvim/plugged')

Plug 'davidhalter/jedi-vim'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'zchee/deoplete-jedi'
Plug 'deoplete-plugins/deoplete-clang'

"telescope"
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

"statusbar"
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'sbdchd/neoformat'

"filemanager sidemenu"
Plug 'scrooloose/nerdtree'

"markdown editing"
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'

"syntax highlighting markdown"

" tabular plugin is used to format tables
Plug 'godlygeek/tabular'
" JSON front matter highlight plugin
Plug 'elzr/vim-json'
Plug 'plasticboy/vim-markdown'

"Latex"
Plug 'lervag/vimtex'

" Indentline 
Plug 'lukas-reineke/indent-blankline.nvim'

Plug 'ellisonleao/gruvbox.nvim'
call plug#end()

set background=dark " or light if you want light mode
colorscheme gruvbox

lua vim.opt.list = true
lua vim.opt.listchars:append("space:⋅")
lua require("indent_blankline").setup { char = "|", buftype_exclude = {"terminal"} }

let g:deoplete#enable_at_startup = 1
let g:airline_powerline_fonts = 1

" Enable alignment
let g:neoformat_basic_format_align = 1

" Enable tab to space conversion
let g:neoformat_basic_format_retab = 1

" Enable trimmming of trailing whitespace
let g:neoformat_basic_format_trim = 1

"markdown"
let g:UltiSnipsExpandTrigger="<tab>"  " use <Tab> to trigger autocompletion
let g:UltiSnipsJumpForwardTrigger="<c-j>"
let g:UltiSnipsJumpBackwardTrigger="<c-k>"

" --------------------------------- vim-markdown settings
" disable header folding
let g:vim_markdown_folding_disabled = 1

" do not use conceal feature, the implementation is not so good
let g:vim_markdown_conceal = 0

" disable math tex conceal feature
let g:tex_conceal = ""
let g:vim_markdown_math = 1

" support front matter of various format
let g:vim_markdown_frontmatter = 1  " for YAML format
let g:vim_markdown_toml_frontmatter = 1  " for TOML format
let g:vim_markdown_json_frontmatter = 1  " for JSON format
" ------------------------------ vim-markdown settings end

augroup highlight_yank
    autocmd!
    au TextYankPost * silent! lua vim.highlight.on_yank{higroup="IncSearch", timeout=700}
augroup END

"latex"
call deoplete#custom#var('omni', 'input_patterns', {
            \'tex': g:vimtex#re#deoplete
            \})

set number
set relativenumber
set tabstop=4
set shiftwidth=4
set autoindent
set expandtab 			" use spaces as tab
set cursorline

 " windownavigation keymap"
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

let mapleader="\<Space>"
"copy system clipboard
nnoremap <leader>y "+y
nnoremap <leader>p "+p

"telescope"
"leader find file"
nnoremap <leader>ff <CMD>Telescope find_files<CR>
nnoremap <leader>fp <CMD>Telescope find_files cwd=~<CR>
nnoremap <leader><CR> <CMD>Telescope buffers<CR>
nnoremap <leader>fh <CMD>Telescope help_tags<CR>

