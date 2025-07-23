"""
/*
 * © 2022-2026 Ashraf Morningstar
 * GitHub: https://github.com/AshrafMorningstar
 *
 * This project is a personal recreation of existing projects, developed by Ashraf Morningstar 
 * for learning and skill development. Original project concepts remains the intellectual 
 * property of their respective creators.
 */
"""
# File # 96/300
# Category: Embedded
# Language: MicroPython
# Filename: 096_iot_sensor.py
# Description: IoT Sensor Reader (DHT11) for ESP32/ESP8266.
#              Demonstrates hardware access (Pin, DHT) and timers.

import machine
import dht
import time

print("--- MicroPython IoT Sensor Node ---")

# --- Configuration ---
LED_PIN = 2        # Built-in LED on most ESP boards
DTO_PIN = 4        # Data pin for DHT sensor
CHECK_INTERVAL = 5 # Seconds

# --- Setup ---
led = machine.Pin(LED_PIN, machine.Pin.OUT)
sensor = dht.DHT11(machine.Pin(DTO_PIN))

def blink_led(times, delay):
    for _ in range(times):
        led.value(1) # On
        time.sleep(delay)
        led.value(0) # Off
        time.sleep(delay)

def read_sensor():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print("Temp: {} C  |  Humidity: {} %".format(temp, hum))
        
        # Logic: Alarm if too hot
        if temp > 30:
            print("(!) ALERT: High Temperature")
            blink_led(3, 0.1) # Fast Blink
        else:
            blink_led(1, 0.5) # Heartbeat
            
    except OSError as e:
        print("Failed to read sensor:", e)

# --- Main Loop ---
print("Starting Loop...")

while True:
    read_sensor()
    time.sleep(CHECK_INTERVAL)
