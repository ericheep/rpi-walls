// PiHandler
// written by Eric heep

// Dog Star 2018
// ~-~-

public class PiHandler {

    OscOut piOut[0];
    OscMsg msg;

    fun void init(string hostnames[], int port) {
        for (0 => int i; i < hostnames.size(); i++) {
            OscOut oscOut;
            piOut << oscOut;
            piOut[i].dest(hostnames[i], port);
        }
    }

    fun void send(string addr, float progress) {
        out.start(addr);
        out.add(progress);
        out.send();
    }
}
