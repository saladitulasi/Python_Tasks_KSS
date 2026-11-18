class WiFiDevice:
    def wifi(self):
        print("WiFi Connectivity: Enabled")


class VoiceAssistant:
    def voice(self):
        print("Voice Control: Enabled")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Device: Smart Speaker")


s = SmartSpeaker()

s.display()
s.wifi()
s.voice()