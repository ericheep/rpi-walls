// desert lines test
// sender script

// written by Eric Heep
// Dog Star 2018
// ~-~-

"127.0.0.1" => string hostname;

OscOut out;
OscMsg msg;

out.dest(hostname, 10001);

0.25::second => now;

out.start("/gasStation");
out.add(0.0);
out.send();
