The IT team at Amazon has device configurations for Amazon employees' devices for their work laptops, work mobile phones, etc.

Assuming there's a RemoteConfigurationSender service implemented that sends the given configuration to the device, write the LLD for the device configurations manager.

Device configurations can be like:

```json
{
  "namespace": "com.amazon.laptop",
  "attributes": {
    "key1": "value1",
    "key2": "value2"
  },
  "priority": 1
}
```

The configuration that needs to be sent to a device is the one with the lowest "priority" value

Some entities to start-off with to give a better idea:

- DeviceConfiguration
- Device

The LLD code must be modular, extensible and follow the right design
principles as applicable
