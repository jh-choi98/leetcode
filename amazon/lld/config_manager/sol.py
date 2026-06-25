"""
RemoteConfigurationSender

Config: {
    "namespace": "com.amazon.laptop",
    "attributes": {
        "key1": "value1",
        "key2": "value2",
    },
    "priority": 1
}

Device
    -device_id
    - namesapce

DeviceConfiguration
    - config_id
    - namepsace
    - atrributes
    - priority
    
ConfigurationStore

DeviceConfigurationManager

"""

from zmq import device


class DeviceConfiguration:
    def __init__(self, config_id: str, namespace: str, attributes: dict[str, str], priority: int):
        if not config_id:
            raise ValueError("Configuration ID cannot be empty")
        
        if not namespace:
            raise ValueError("Configuration namespace cannot be empty")
        
        if attributes is None:
            raise ValueError("Configuration attributes cannot be None")
        
        self.config_id = config_id
        self.namespace = namespace
        
        """
            I'll copy the attributes so the caller cannot accidentally
            mutate the configuration after adding it
        """
        self.attributes = dict(attributes)
        
        self.priority = priority
        
class Device:
    def __init__(self, device_id: str, namespace: str):
        if not device_id:
            raise ValueError("Device ID cannot be empty")
        
        if not namespace:
            raise ValueError("Device namespace cannot be empty")
        
        self.device_id = device_id
        self.namespace = namespace

class RemoteConfigurationSender:
    def send(self, device: Device, configuration: DeviceConfiguration):
        pass
          
class ConfigurationStore:
    def __init__(self):
        # Say: "I'll store configurations by ID so each configuration is uniquely
        # identifiable. This helps with future update, delete, or audit
        # use cases."
        self.configuration_by_id: dict[str, DeviceConfiguration] = {}
        
        # Say: "I'll keep configurations grouped by namespace because devices
        # receive configurations based on their namespace."
        self.configuration_by_namespace: dict[str, list[DeviceConfiguration]] = {}
        
        # Say: "For the current requirement, I'll cache the best configuration
        # per namespace so lookup is efficient."
        self.best_config_by_namespace: dict[str, DeviceConfiguration] = {}
        
    def add_configuration(self, configuration: DeviceConfiguration):
        config_id = configuration.config_id
        namespace = configuration.namespace
        
        if config_id in self.configuration_by_id:
            raise ValueError("Configuration already exists")
        
        self.configuration_by_id[config_id] = configuration
        
        if namespace not in self.configuration_by_id:
            self.configuration_by_namespace[namespace] = []
            
        self.configuration_by_namespace[namespace].append(configuration)
        
        current_best = self.best_config_by_namespace.get(namespace)
        
        # Say: "Lowest priority value wins. If priorities tie, I keep the first
        # added configuration by only updating on strictly lower
        # priority."
        if current_best is None or configuration.priority < current_best.priority:
            self.best_config_by_namespace[namespace] = configuration
    
    def get_best_configuration(self, namespace: str):
        return self.best_config_by_namespace.get(namespace)
    
class DeviceConfigurationManager:
    def __init__(self, remote_sender: RemoteConfigurationSender, configuration_store: ConfigurationStore):
        self.remote_sender = remote_sender
        self.configuration_store = configuration_store
        
        # Say: "The manager owns device registration, while configuration
        # storage and best-config tracking are delegated to
        # ConfigurationStore."
        self.devices_by_id: dict[str, Device] = {}
        
    def register_device(self, device_id: str, namespace: str):
        if device_id in self.devices_by_id:
            raise ValueError("Device already registered")
        
        device = Device(device_id, namespace)
        self.devices_by_id[device_id] = device
        
    def _get_device(self, device_id: str):
        # Say: "I'll use a helper because multiple methods need the same
        # device lookup and validation logic."
        device = self.devices_by_id.get(device_id)
        
        if device is None:
            raise ValueError("Unknown device ID")
        
        return device
    
    def add_configuration(self, config_id: str, namespace: str, attributes: dict[str, str], priority: int):
         # Say: "The manager creates the configuration object, then delegates
        # storage and best-config tracking to the store."
        configuration = DeviceConfiguration(config_id, namespace, attributes, priority)
        
        self.configuration_store.add_configuration(configuration)
        
    def get_effective_configuration(self, device_id: str):
        # Say: "First, I get the device, then I ask the configuration store
        # for the best config matching that device's namespace."
        device = self._get_device(device_id)
        return self.configuration_store.get_best_configuration(device.namespace)
    
    def send_configuration(self, device_id: str):
        # Say: "To send a configuration, I need both the target device and
        # the effective configuration for that device."
        device = self._get_device(device_id)
        configuration = self.configuration_store.get_best_configuration(device.namespace)
        
        if configuration is None:
            # Say: "The device exists, but there is no applicable configuration,
            # so there is nothing to send."
            return False
        
        self.remote_sender.send(device, configuration)

        return True
