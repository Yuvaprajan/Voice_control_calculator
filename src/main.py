# File: src/main.py
from .voice_recognition import VoiceRecognizer
from .calculator_control import CalculatorController
import time


class VoiceCalculatorApp:
    def __init__(self):
        self.voice_recognizer = VoiceRecognizer()
        self.calculator = CalculatorController()
        self.is_running = False

    def process_command(self, command):
        """Process voice commands"""
        command = command.lower()

        # Open calculator commands
        if 'open' in command and 'calculator' in command:
            return self.calculator.open_calculator()

        # Close calculator commands
        if 'close' in command and 'calculator' in command:
            return self.calculator.close_calculator()
        
        if 'clear' in command and 'screen' in command:
            return self.calculator.clear_calculator()

        # Calculation commands
        if any(op in command for op in ['plus', 'minus', 'multiply', 'divide', 'multiplied', '*', '+', '-', '/']):
            # Remove verbal filler words and standardize
            calculation = command.replace('calculate', '').replace('what is', '')
            
            # Attempt to input calculation
            return self.calculator.input_calculation(calculation)

        return False

    def run(self):
        """Main application loop"""
        print("Voice Calculator Started. Say 'open calculator' to begin.")
        self.is_running = True

        while self.is_running:
            # Listen for command
            command = self.voice_recognizer.listen()
            
            if command:
                # Check for exit commands
                if 'exit' in command or 'quit' in command:
                    self.calculator.close_calculator()
                    self.is_running = False
                    break
                
                # Process the command
                self.process_command(command)

def main():
    app = VoiceCalculatorApp()
    app.run()

if __name__ == "__main__":
    main()