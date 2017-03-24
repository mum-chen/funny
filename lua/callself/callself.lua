local function call_self(t)
	setmetatable(t, {
		__call = function(self, index)
			return (index == nil) and self or index
		end
	})
	return t
end

local loop = call_self({})

print(loop()()()()()()()()()()()()()()()("success"))
