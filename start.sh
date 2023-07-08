if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tsunemoriii/Request-Trial.git /Request-Trial
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone https://github.com/Tsunemoriii/Request-Trial /Request-Trial
fi
cd /Request-Trial
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
