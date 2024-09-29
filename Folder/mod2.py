from pymodbus.client import ModbusTcpClient

# Connect to the Modbus server
client = ModbusTcpClient('127.0.0.1', port=502)

# Write data to holding registers
client.write_registers(0, [10, 20, 30, 40, 50])

# Close the connection
client.close()
