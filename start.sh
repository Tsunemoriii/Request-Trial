if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MahirModan/utah.git /utah
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone https://github.com/MahirModan/utah /utah
fi
cd /utah
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
