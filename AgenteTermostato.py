class ThermostatAgent:
    def __init__(self, target_temp):
        self.target_temp = target_temp  # Temperatura deseada

    def sense_environment(self, current_temp):
        """Recibe la temperatura actual del entorno."""
        return current_temp

    def act(self, current_temp):
        """Decide la acción basada en la temperatura actual."""
        if current_temp < self.target_temp - 1:
            return "Encender calefacción"
        elif current_temp > self.target_temp + 1:
            return "Encender aire acondicionado"
        else:
            return "Mantener temperatura"

# Simulación de un agente termostato
if __name__ == "__main__":
    thermostat = ThermostatAgent(target_temp=22)  # Temperatura objetivo de 22°C
    
    # Simulación de distintas temperaturas
    test_temperatures = [18, 21, 22, 24, 26]
    
    for temp in test_temperatures:
        action = thermostat.act(temp)
        print(f"Temperatura actual: {temp}°C -> Acción: {action}")