local telescope = require 'telescope'
local builtin = require 'telescope.builtin'

telescope.setup {
  defaults = {
    prompt_prefix = ' ',
  }
}

local M = {}

function M.find_files()
  builtin.find_files {
    follow = true, -- follow symlinks
    hidden = true, -- show hidden
  }
end

function M.find_home_files()
  builtin.find_files {
    cwd = '~',
    follow = true, -- follow symlinks
    hidden = true, -- show hidden
  }
end

-- Keybindings
vim.keymap.set('n', '<leader>ff', M.find_files)
vim.keymap.set('n', '<leader>fp', M.find_home_files)
vim.keymap.set('n', '<leader>fb', builtin.buffers)
vim.keymap.set('n', '<leader>fh', builtin.help_tags)

