class Settings():
    """A class to store all settings for Sound House pi controller."""

    def __init__(self):
        """Initialize settings"""
        self.screen_width = 1200 # change later when building interface window
        self.screen_height = 500
        self.bg_color = (0, 0, 0)
        self.panel_bg_color = (50, 50, 50)

        # Ports
        self.portFeedbackControl = 7400
        self.portOscControl = 10001
        self.portPingSensors = 5000
        self.portGetSensorData = 12345

        #IPs

        self.wallIPs = ['pione.local', 'pitwo.local', 'pithree.local',
                        'pifour.local', 'pifive.local', 'pisix.local',
                        'piseven.local', 'pieight.local']

        # Client lists
        self.wallOSC_clients = []

        # Current wall panel to display
        self.wall_panel = 0 # Wall 1 by default
        # Current selected puppet
        self.puppet = 0 # P1 by default


        # Network status
        self.networkOn = False # when off, in 'dev' mode and sends things locally or not at all

        # Modes - all off to start
        self.ternaryWallMode = False
        self.feedbackMode = False
        self.playbackMode = False
        self.sensorTuningMode = False

        # Feedback defaults
        self.mic = 100 #starting vals, need to tech and set exactly
        self.hp = 0
        self.lp = 100
        self.res = 100
        self.threshold = 5
        self.packetLength = 50
        self.delayLength = 5

        # Ternary Wall Mode settings
        self.centerFreq = 440.01 # why does 440.01 work and not 440????
        self.interval = 1.1667 # add fractions and selection availability, make control for this, a series of fractions? 7?
        self.u_interval = 1 / self.interval
        self.ternary_chain = [0, 0, 0, 0, 0, 0, 0] # initial vals

        # Wall Map settings
        self.wall_speed_factor = 1