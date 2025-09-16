
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
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip3 install pync

To make the script executable:
	chmod +x les_mots_du_jour.py

To create a global symlink to run from anywhere:
	sudo ln -s /full/path/to/les_mots_du_jour.py /usr/local/bin/les_mots_du_jour

Schedule with cron (daily at 9 AM):
	crontab -e
	0 9 * * * /usr/local/bin/les_mots_du_jour

### ** Challenges Solved**
```markdown
## Challenges & Solutions
- **File paths:** Used absolute paths to avoid “file not found” errors.
- **History management:** Ensures no repeated words until all are used.
- **Notifications:** Used `pync` for desktop notifications.
- **Automation:** Cron scheduling to run daily without manual input.

![Notification Example](assets/notification.png)

