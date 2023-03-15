let g:syntastic_javascript_checkers=['standard']
let g:syntastic_javascript_standard_exec = 'semistandard'
autocmd bufwritepost *.js silent !semistandard % --fix
set autoread
