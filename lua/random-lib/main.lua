package.path = ("./%s-?.lua;"):format(os.date("%p")) .. package.path
require("what")
