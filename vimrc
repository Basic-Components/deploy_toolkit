set nu
set shortmess=atI
syntax on
set nobackup
set confirm
set mouse=c
set tabstop=4
set shiftwidth=4
set expandtab
set smarttab
set autoread
set cindent
set autoindent
set smartindent
set hlsearch
set background=dark
set showmatch
set ruler
set nocompatible
set foldenable
set fdm=syntax
nnoremap <space> @=((foldclosed(line('.')<0)?'zc':'zo'))<CR>
set novisualbell
set laststatus=2
autocmd InsertLeave * se nocul
autocmd InsertEnter * se cul
set showcmd
set fillchars=vert:/
set fillchars=stl:/
set fillchars=stlnc:/