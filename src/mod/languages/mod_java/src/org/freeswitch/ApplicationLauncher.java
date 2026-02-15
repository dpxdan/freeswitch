package org.fluxpbx.example;

import org.fluxpbx.swig.fluxpbx;

public class ApplicationLauncher {

	public static final void startup(String arg) {
		try {
			fluxpbx.setOriginateStateHandler(OriginateStateHandler.getInstance());
		} catch (Exception e) {
			fluxpbx.console_log("err", "Error registering originate state handler");
		}
	}

}
