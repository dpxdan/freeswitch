# Example Perl script to originate. perlrun
fluxpbx::console_log("info", "Perl in da house!!!\n");

$session = new fluxpbx::Session("sofia/10.0.1.100/1002") ;
$session->execute("playback", "/sr8k.wav");
$session->hangup();
