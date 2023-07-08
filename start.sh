if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tsunemoriii/Request.git /Request
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone https://github.com/Tsunemoriii/Request /Request
fi
cd /Request
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
