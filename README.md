# RSC
## Automatic Startup Using systemd

To automatically start the program on boot using systemd, follow these steps:

1. Copy the systemd service file (`my_program.service`) to the appropriate directory (e.g., `/etc/systemd/system/`).

2. Enable the systemd service to start automatically at boot:
   ```bash
   sudo systemctl enable my_program.service
   ```

3. Start the systemd service:
   ```bash
   sudo systemctl start my_program.service
   ```

4. Verify that the service is running:
   ```bash
   sudo systemctl status my_program.service
   ```

5. Reboot your Raspberry Pi and ensure that the program starts automatically.

