# Reboot Raspberry Pi 4B Using a Physical Button
You can reboot your Raspberry Pi 4B using a physical switch connected to a GPIO pin.
The main program+ is based on this page: [Please check it out](https://gpiozero.readthedocs.io/en/stable/recipes.html#shutdown-button).

Install the following Python modules: `gpiozero`, `lgpio`
```sh
sudo apt update
sudo apt upgrade
sudo pip3 install gpiozero
sudo apt install python3-lgpio
```

## Program
You can reboot your Raspberry Pi 4B using `reboot.py`.
You may place this program in any directory, but note the path because you will need it when creating the service file later.
The following commands assume that the directory is in `/home/hoge/`

If you'd like to shut down instead of reboot, modify the last part of the reboot function in the program as follows.
```
    check_call(['sudo', 'shutdown', '-h', 'now'])
```

If you write the script yourself, it is a good idea to test it to ensure there are no issues:
```sh
python3 reboot.py
```


## Register the Program as a Service

Run the following commands in a terminal.

1. Change the file permission:
```sh
chmod 755 /home/hoge/reboot.py
```

2. Create a service file and edit it:
```sh
sudo vi /usr/lib/systemd/system/reboot.service
```

Modify the program file path as needed.
```sh
[Unit]
Description=Reboot Raspberry Pi by GPIO button input

[Service]
ExecStart=/usr/bin/python3 /home/hoge/reboot.py

[Install]
WantedBy=multi-user.target
```

3. Apply the service:
```sh
sudo systemctl daemon-reload
sudo systemctl start reboot.service
```

4. Check whether it is running:
```sh
sudo systemctl status reboot.service
```

5. Enable the service so that it launches automatically when the Raspberry Pi boots:
```sh
sudo systemctl enable reboot.service
```

ETC. If you'd like to stop the service, run the following command:
```sh
sudo systemctl disable reboot.service
```
