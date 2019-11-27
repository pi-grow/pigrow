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

echo "Firing Up the Far Red LED's!"
sudo systemctl enable farred.service
sudo systemctl start farred.service

echo "Spinning up Oscillating Circulation Fans!"
sudo systemctl enable fans.service
sudo systemctl start fans.service

echo "Done!"
echo "Ready to Grow!"
