from pymodbus.client import ModbusTcpClient

# Define the Modbus server IP and port
MODBUS_SERVER_IP = '127.0.0.1'
MODBUS_SERVER_PORT = 502

# Create a Modbus client
client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_SERVER_PORT)

# Connect to the Modbus server
client.connect()

# Write data to a holding register (address 1)
write_response = client.write_register(1, 123)
write_response2 = client.write_register(2, 1233)
print(f'Write Response: {write_response}')

# Read data from a holding register (address 1)
read_response = client.read_holding_registers(1, 2)
print(f'Read Response: {read_response.registers[0:2]}')


# Close the client connection
client.close()