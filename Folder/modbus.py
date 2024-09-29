from pymodbus.client import ModbusTcpClient

# Connect to the Modbus server
client = ModbusTcpClient('127.0.0.1', port=502)

# Read data from holding registers
result = client.read_holding_registers(0, 5)
print(result.registers)

# Close the connection
client.close()
