class Module:
    """
    Basic communication functions via Modbus RTU and TCP
    """
    client_modbus = None
    modbus_id = None

    def modbus_init(self, client, modbus_id: int):
        self.client_modbus = client
        self.modbus_id = modbus_id

    def read_regs(self, address: int, count: int):
        result = self.client_modbus.read_holding_registers(address, count, unit=self.modbus_id)
        if hasattr(result, 'registers'):
            return result.registers
        else:
            return None

    def read_reg(self, address: int):
        registers = self.read_regs(address, 1)
        if registers is not None:
            registers = registers[0]
        return registers

    def write_reg(self, address: int, value: int):
        return self.client_modbus.write_register(address, value, unit=self.modbus_id)

    def read_coils(self, register: int, count: int):
        result = self.client_modbus.read_coils(register, count, unit=self.modbus_id)
        if hasattr(result, 'bits'):
            return result.bits
        else:
            return None

    def read_coil(self, register: int):
        bits = self.read_coils(register, 1)
        if bits is not None:
            bits = bits[0]
        return bits

    def check_connection(self, reg: int = 0):
        return self.read_reg(reg)
