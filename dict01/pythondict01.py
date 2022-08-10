#!/usr/bin/env python3

switch = {"hostname": "sw1",
        "ip": "10.0.1.1",
        "version": "1.2",
        "vendor": "cisco"
        }

print( switch["hostname"] )
print( switch["ip"] )


## request a 'fake' key
## print( switch["lynx"] )


print( "First test - .get()" )
print( switch.get("lynx") )

print( "second test - .get()" )
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

print( "third test - .get()" )
print( switch.get("version") )

print( "fourth test - .get()" )
print( switch.keys() )

print( "fifth test - .get()" )
print( switch.values() )

print( "sixth test - .pop()" )
switch.pop("version")
print( switch.keys() )
print( switch.values() )

print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values()

print( "Eighth test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )
