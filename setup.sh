#!/bin/bash

echo "Setting Up PiGrow!"

echo "Installing Utilities"
sudo cp ./utils/* /usr/local/sbin/

echo "Installing Python Apps"
sudo cp ./python/* /usr/local/sbin/

echo "Installing Services"
sudo cp ./services/* /lib/systemd/system/

echo "Reloading systemctl"
sudo systemctl daemon-reload

echo "Spinning up Oscillating Circulation Fans!"
sudo systemctl enable fans.service
sudo systemctl start fans.service

echo "Firing RED LED's"
sudo systemctl enable red-led.service
sudo systemctl start red-led.service

echo "Done!"
echo "Ready to Grow!"
