-- Example Lua script to originate. luarun
fluxpbx.console_log("info", "Lua in da house!!!\n");

local session = fluxpbx.Session("sofia/10.0.1.100/1001");
session:execute("playback", "/sr8k.wav");
session:hangup();
