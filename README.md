# Reboot Raspberry Pi 4B using a Physical Button
You can reboot your Raspberry Pi 4B using a physical switch connected to a GPIO pin of the device.
The main programme is based on this page: [Please check it out](https://gpiozero.readthedocs.io/en/stable/recipes.html#shutdown-button).

Install the follwing python modules: gpiozero, lgpio
```sh
sudo apt update
sudo apt upgrade
sudo pip3 install gpiozero
sudo apt install python3-lgpio
```

## Programme
You can reboot your Raspberry Pi 4B using the programme.
You may put the reboot.py at any directory but note the directory.
You will modify to the directory when you write a service file.

If you'd like to shutdown instead of reboot, modify the last part of reboot function in the python file as follows.
```
    check_call(['sudo', 'shutdown', '-h', 'now'])
```

If you rewrite by yourself, it's better to check there is no problem with the programme.
```sh
python3 reboot.py
```

## Resistor the programme as a service
Run following in a terminal.
1. Change the authentification status to root user by follows.
```sh
chmod 755 reboot.py
```

2. Add a service and modify a little.
```sh
sudo vi /usr/lib/systemd/system/reboot.service
```

Modify the programme file directory.
Following example assume that the directory of the programme is in /home/hoge/.
```sh
[Unit]
Description=Reboot Raspberry Pi by GPIO button input

[Service]
ExecStart=/usr/bin/python3 /home/hoge/reboot.py

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

5. Enable the service so that it is launched when the Raspberry Pi is booted
```sh
sudo systemctl enable reboot.service
```

ETC. If you'd like to stop the service run the following line.
```sh
sudo systemctl disable reboot.service
```
