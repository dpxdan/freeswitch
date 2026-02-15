move fluxpbx_wrap.cxx fluxpbx_wrap.bak
\dev\swig20\swig.exe -I..\..\..\include -v -O -c++ -csharp -namespace FluxPBX.Native -dllimport mod_managed -DSWIG_CSHARP_NO_STRING_HELPER fluxpbx.i 
del swig.csx
move fluxpbx_wrap.cxx fluxpbx_wrap.2010.cxx
move fluxpbx_wrap.bak fluxpbx_wrap.cxx
@ECHO OFF
for %%X in (*.cs) do type %%X >> swig.csx
@ECHO ON
move swig.csx managed\swig.2010.cs
del *.cs
