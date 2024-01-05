# Reboot Raspi4B using a Physical Button
You can reboot your Raspberry Pi 4B using a physical switch connected to GPIO pin of the device.
This programme is based on this blog: [Please check it out](https://gpiozero.readthedocs.io/en/stable/recipes.html#shutdown-button).

Install the follwing python modules: gpiozero, lgpio
```sh
sudo apt update
sudo apt upgrade
sudo pip3 install gpiozero
sudo apt install python3-lgpio
```

## Programme
You can reboot your Raspberry Pi 4B using the programme but be careful with the directory.
(You need to activate your programme as you will see in the next section)
You may put the reboot.py file anywhere you'd like to but remember the directory.
You will modify to the directory when you write a service file.

If you'd like to shutdown instead of reboot, modify the last part of reboot function as follows.
```
    check_call(['sudo', 'shutdown', '-h', 'now'])
```

If you rewrite by yourself, it's better to check there is no problem with the programme.
```sh
python3 reboot.py
```

## Resistor the programme as a service
1. Change the authentification to root user as follows.
```sh
chmod 755 reboot.py
```

2. Add a service and modify a little.
```sh
sudo vi /usr/lib/systemd/system/reboot.service
```

Modify the service directory.
Following example assume that the directory of the programme is in /home/karugamot/presets/.
```sh
[Unit]
Description=Reboot raspberry pi by GPIO button input

[Service]
ExecStart=/usr/bin/python3 /home/karugamot/presets/reboot.py

[Install]
WantedBy=multi-user.target
```

3. Apply the service
```sh
sudo systemctl daemon-reload
```
```sh
sudo systemctl start reboot.service
```

4. Check whether it is working
```sh
sudo systemctl status reboot.service
```

5. Set the service to launch when the raspi is booted
```sh
sudo systemctl enable reboot.service
```

ETC. Stop the service
```sh
sudo systemctl disable reboot.service
```