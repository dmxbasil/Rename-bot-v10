if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MrMKN/TG-RENAMER-BOT-V5.git /TG-RENAMER-BOT-V5     
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /TG-RENAMER-BOT-V5
fi
cd /TG-RENAMER-BOT-V5
pip3 install -U -r requirements.txt
echo """
------------------------
| ⚡️ Bot is Starting ⚡️|
------------------------
"""
python3 boy.py
