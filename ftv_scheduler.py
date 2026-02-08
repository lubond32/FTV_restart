#!/usr/bin/env python3
"""
FTV Scheduler - Regularly turn on/off Fire TV device
"""
import json
import os
import sys
from datetime import datetime, time
import argparse


class FTVScheduler:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from JSON file"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            'device_ip': '192.168.1.100',
            'schedule': {
                'on_time': '08:00',
                'off_time': '22:00'
            },
            'enabled': True
        }
    
    def save_config(self):
        """Save configuration to JSON file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def turn_on(self):
        """Turn on the FTV device"""
        device_ip = self.config.get('device_ip', '192.168.1.100')
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Turning ON FTV at {device_ip}")
        # In a real implementation, this would use ADB or wake-on-lan
        # For minimal implementation, we just log the action
        return True
    
    def turn_off(self):
        """Turn off the FTV device"""
        device_ip = self.config.get('device_ip', '192.168.1.100')
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Turning OFF FTV at {device_ip}")
        # In a real implementation, this would use ADB command
        # For minimal implementation, we just log the action
        return True
    
    def check_schedule(self):
        """Check if it's time to turn on or off based on schedule"""
        if not self.config.get('enabled', True):
            print("Scheduler is disabled")
            return None
        
        now = datetime.now().time()
        on_time_str = self.config['schedule']['on_time']
        off_time_str = self.config['schedule']['off_time']
        
        on_time = datetime.strptime(on_time_str, '%H:%M').time()
        off_time = datetime.strptime(off_time_str, '%H:%M').time()
        
        current_minutes = now.hour * 60 + now.minute
        on_minutes = on_time.hour * 60 + on_time.minute
        off_minutes = off_time.hour * 60 + off_time.minute
        
        # Check if we're within 1 minute of scheduled time
        if abs(current_minutes - on_minutes) <= 1:
            return 'on'
        elif abs(current_minutes - off_minutes) <= 1:
            return 'off'
        
        return None
    
    def get_status(self):
        """Get current scheduler status"""
        return {
            'enabled': self.config.get('enabled', True),
            'device_ip': self.config.get('device_ip', '192.168.1.100'),
            'on_time': self.config['schedule']['on_time'],
            'off_time': self.config['schedule']['off_time']
        }


def main():
    parser = argparse.ArgumentParser(description='FTV Scheduler - Control Fire TV on/off schedule')
    parser.add_argument('action', choices=['on', 'off', 'status', 'check', 'set-schedule'],
                        help='Action to perform')
    parser.add_argument('--on-time', help='Set turn-on time (HH:MM format)')
    parser.add_argument('--off-time', help='Set turn-off time (HH:MM format)')
    parser.add_argument('--device-ip', help='Set device IP address')
    parser.add_argument('--config', default='config.json', help='Configuration file path')
    
    args = parser.parse_args()
    
    scheduler = FTVScheduler(args.config)
    
    if args.action == 'on':
        scheduler.turn_on()
    elif args.action == 'off':
        scheduler.turn_off()
    elif args.action == 'status':
        status = scheduler.get_status()
        print("FTV Scheduler Status:")
        print(f"  Enabled: {status['enabled']}")
        print(f"  Device IP: {status['device_ip']}")
        print(f"  Turn ON time: {status['on_time']}")
        print(f"  Turn OFF time: {status['off_time']}")
    elif args.action == 'check':
        action = scheduler.check_schedule()
        if action == 'on':
            scheduler.turn_on()
        elif action == 'off':
            scheduler.turn_off()
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] No scheduled action at this time")
    elif args.action == 'set-schedule':
        if args.on_time:
            scheduler.config['schedule']['on_time'] = args.on_time
        if args.off_time:
            scheduler.config['schedule']['off_time'] = args.off_time
        if args.device_ip:
            scheduler.config['device_ip'] = args.device_ip
        scheduler.save_config()
        print("Schedule updated successfully")
        status = scheduler.get_status()
        print(f"  Turn ON time: {status['on_time']}")
        print(f"  Turn OFF time: {status['off_time']}")
        print(f"  Device IP: {status['device_ip']}")


if __name__ == '__main__':
    main()
