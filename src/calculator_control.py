# File: src/calculator_control.py
import os
import subprocess
import pyautogui
import time

class CalculatorController:
    def __init__(self):
        self.os_type = self._detect_os()
        pyautogui.PAUSE = 0.5  # Small delay between keystrokes

    def _detect_os(self):
        """Detect operating system"""
        if os.name == 'nt':
            return 'windows'
        elif os.name == 'posix':
            if subprocess.call(['which', 'sw_vers'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                return 'mac'
            else:
                return 'linux'
        return 'unknown'

    def open_calculator(self):
        """Open system calculator based on OS"""
        try:
            if self.os_type == 'windows':
                subprocess.Popen('calc.exe')
            elif self.os_type == 'mac':
                subprocess.Popen(['open', '-a', 'Calculator'])
            elif self.os_type == 'linux':
                subprocess.Popen(['gnome-calculator'])
            
            time.sleep(1)  # Wait for calculator to open
            return True
        except Exception as e:
            print(f"Error opening calculator: {e}")
            return False

    def close_calculator(self):
        """Close system calculator based on OS"""
        try:
            if self.os_type == 'windows':
                subprocess.call('taskkill /F /IM calc.exe', shell=True)
            elif self.os_type == 'mac':
                subprocess.call(['pkill', 'Calculator'])
            elif self.os_type == 'linux':
                subprocess.call(['pkill', 'gnome-calculator'])
            return True
        except Exception as e:
            print(f"Error closing calculator: {e}")
            return False

    def input_calculation(self, expression):
        """
        Input calculation steps into the calculator and press equals
        Supports basic arithmetic operations
        """
        # Standardize expression
        expression = expression.replace('x', '*').replace('multiplied by', '*')
        
        # Evaluate expression for validation
        try:
            result = eval(expression)
        except Exception:
            print("Invalid mathematical expression")
            return False

        # Type out the expression
        for char in expression:
            if char.isdigit():
                pyautogui.press(char)
            elif char in ['+', '-', '*', '/', '=']:
                if char == '*':
                    pyautogui.press('*')
                elif char == '/':
                    pyautogui.press('/')
                elif char == '+':
                    pyautogui.press('+')
                elif char == '-':
                    pyautogui.press('-')
        
        # Press equals button 
        pyautogui.press('enter')  # Most calculators use Enter for equals
        
        return True

    def clear_calculator(self):
        """
        Clear the calculator screen
        Platform-specific clearing method
        """
        if self.os_type == 'windows':
            pyautogui.press('esc')  # Clear on Windows calculator
        elif self.os_type == 'mac':
            pyautogui.hotkey('command', 'backspace')  # Clear on Mac calculator
        elif self.os_type == 'linux':
            pyautogui.press('esc')  # Clear on most Linux calculators