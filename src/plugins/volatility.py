import volatility3.framework as vol

class ThreatScanner:
    def __init__(self, memory_dump):
        self.context = vol.Context()
        self.config = vol.requirements.VirtualAddressSpaceRequirements(
            memory_dump
        )
        
    def find_malware(self):
        """Detects API unhooking and DLL injection"""
        plugins = [
            "windows.malfind.Malfind",
            "windows.pslist.PsList"
            
        ]
        
        return {
            plugin: vol.run_plugin(plugin, self.config) 
            for plugin in plugins
            
        }