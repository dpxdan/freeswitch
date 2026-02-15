package org.fluxpbx;

public interface HangupHook
{
    /** Called on hangup, usually in a different thread. */
    public void onHangup();
}

