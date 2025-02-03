vim.g.mapleader = " "

local keymap = vim.keymap -- for conciseness

keymap.set("n", "<leader>pv", vim.cmd.Ex, { desc = "[ ] open netrw" })

-- window management
keymap.set("n", "<leader>sv", "<C-w>v", { desc = "[S]plit window [V]ertically" }) -- split window vertically
keymap.set("n", "<leader>sh", "<C-w>s", { desc = "[S]plit window [H]orizontally" }) -- split window horizontally
keymap.set("n", "<leader>se", "<C-w>=", { desc = "(make) [S]plits [E]equal size" }) -- make split windows equal width & height
keymap.set("n", "<leader>sx", "<cmd>close<CR>", { desc = "[S]plit [X]close" }) -- close current split window

keymap.set("n", "<leader>to", "<cmd>tabnew<CR>", { desc = "[ ] Open new tab" }) -- open new tab
keymap.set("n", "<leader>tx", "<cmd>tabclose<CR>", { desc = "[ ] Close current tab" }) -- close current tab
keymap.set("n", "<leader>tn", "<cmd>tabn<CR>", { desc = "[ ] Go to next tab" }) --  go to next tab
keymap.set("n", "<leader>tp", "<cmd>tabp<CR>", { desc = "[ ] Go to previous tab" }) --  go to previous tab
keymap.set("n", "<leader>tf", "<cmd>tabnew %<CR>", { desc = "[ ] Open current buffer in new tab" }) --  move current buffer to new tab

-- primagen keymaps for moiving lines

vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv", { desc = "move line to the top" })
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "move line to the down" })

--[[ hilight tet while yanking ]]
vim.api.nvim_create_autocmd("TextYankPost", {
	desc = "Highlight when yanking (copying) text",
	group = vim.api.nvim_create_augroup("kickstart-highlight-yank", { clear = true }),
	callback = function()
		vim.highlight.on_yank()
	end,
})
