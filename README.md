# FTV_restart

Scheduled on/off control for Fire TV devices (FTV).

## Features

- Schedule regular turn on/off times for your Fire TV
- Manual on/off control
- Configurable schedule via JSON configuration
- Status checking

## Installation

No installation required. This is a standalone Python script.

Requirements:
- Python 3.6 or higher

## Configuration

Edit `config.json` to set your schedule:

```json
{
  "device_ip": "192.168.1.100",
  "schedule": {
    "on_time": "08:00",
    "off_time": "22:00"
  },
  "enabled": true
}
```

- `device_ip`: IP address of your Fire TV device
- `on_time`: Time to turn on (24-hour format HH:MM)
- `off_time`: Time to turn off (24-hour format HH:MM)
- `enabled`: Enable/disable the scheduler

## Usage

### Manual Control

Turn on FTV:
```bash
python3 ftv_scheduler.py on
```

Turn off FTV:
```bash
python3 ftv_scheduler.py off
```

### Schedule Management

Set schedule times:
```bash
python3 ftv_scheduler.py set-schedule --on-time 08:00 --off-time 22:00
```

Set device IP:
```bash
python3 ftv_scheduler.py set-schedule --device-ip 192.168.1.100
```

Check status:
```bash
python3 ftv_scheduler.py status
```

### Automated Scheduling

Check and execute scheduled action (run this via cron):
```bash
python3 ftv_scheduler.py check
```

To run automatically, add to crontab (runs every minute):
```bash
* * * * * cd /path/to/FTV_restart && python3 ftv_scheduler.py check
```

## Ako regulárne zapnúť/vypnúť FTV (Slovak)

Pre automatické zapínanie a vypínanie Fire TV podľa rozvrhu:

1. Nastavte časy zapnutia a vypnutia:
```bash
python3 ftv_scheduler.py set-schedule --on-time 08:00 --off-time 22:00
```

2. Pridajte do crontab pre pravidelné spúšťanie:
```bash
crontab -e
```

Pridajte riadok:
```
* * * * * cd /path/to/FTV_restart && python3 ftv_scheduler.py check
```

## License

MIT