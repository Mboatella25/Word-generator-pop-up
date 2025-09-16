# French Words of the Day
A simple Python tool that pops 5 random French words every day with desktop notifications.

## Motivation
I created this project while learning Python and French. It combines language learning with automation, notifications, and file handling. Along the way, I solved common problems like:
- Avoiding repeated words until all are used
- Cross-platform notifications on Mac
- Scheduling a script daily with cron

## How It Works
1. Reads a vocabulary file (`levocab.txt`) containing French words.
2. Tracks previously used words in `history.txt`.
3. Picks 5 random words each day that haven’t been used recently.
4. Sends a macOS desktop notification using `pync`.
5. Can be scheduled with `cron` to run automatically.

## Setup
1. Clone this repository:
```bash
git clone https://github.com/Mboatella25/Word-generator-pop-up.git
cd Word-generator-pop-up
```
2. Install dependencies:
```bash
pip3 install pync
```
3. Make the script executable:
```bash
chmod +x les_mots_du_jour.py
```
4. Create a global symlink to run it from anywhere:
```bash
sudo ln -s /full/path/to/les_mots_du_jour.py /usr/local/bin/les_mots_du_jour
```
5.	Schedule with cron (daily at 9 AM):
```bash
crontab -e
# Add the following line:
0 9 * * * /usr/local/bin/les_mots_du_jour
```

   
