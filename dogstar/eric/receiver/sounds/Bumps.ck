// Bumps
// written by Eric heep

// Dog Star 2018
// ~-~-

public class Bumps extends Chubgraph {
    Noise noise => LPF lpf => Dyno d => ADSR env => outlet;

    int running;

    fun void connect() {
        1 => running;
        env => outlet;
    }

    fun void disconnect() {
        0 => running;
        env =< outlet;
    }

    fun void trigger(float progress) {
        (progress - 1.0) * -1.0 => float reverse;
        // noise.gain(reverse * 0.7 - 1.0);

        lpf.freq(200 + 400 * reverse);
        Math.pow(reverse, 6) => float revExp;

        0.75::second => dur range;
        100::ms => dur min;
        10::ms + 100::ms * revExp => dur attackTime;

        revExp * range + min => dur bumpDur;

        repeat(2) {
            env.attackTime(attackTime);
            env.sustainLevel(1.0);
            env.keyOn();
            attackTime => now;
            env.releaseTime(attackTime);
            env.keyOff();
            bumpDur => now;
        }
    }

    fun int isRunning() {
        return running;
    }
}