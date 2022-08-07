if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ccadmin1/n2.git /n2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria
fi
cd /n2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
