all: FluxPBX.Managed.dll

clean:
	rm -fr FluxPBX.Managed.dll

FluxPBX.Managed.dll: AssemblyInfo.cs Extensions.cs Loader.cs Log.cs ManagedSession.cs PluginInterfaces.cs PluginManager.cs ScriptPluginManager.cs swig.cs
	dmcs -target:library -out:FluxPBX.Managed.dll AssemblyInfo.cs Extensions.cs Loader.cs Log.cs ManagedSession.cs PluginInterfaces.cs PluginManager.cs ScriptPluginManager.cs ChannelVariables.cs Util.cs swig.cs XmlSearchBinding.cs

install: FluxPBX.Managed.dll
	$(INSTALL) FluxPBX.Managed.dll $(DESTDIR)$(MODINSTDIR)

uninstall:
	$(UNINSTALL) $(MODINSTDIR)/FluxPBX.Managed.dll

