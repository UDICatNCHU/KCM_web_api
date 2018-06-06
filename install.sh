# front-end use React
# so need to use webpack and bower
npm install
npm install -g bower
./node_modules/.bin/webpack --config webpack.config.index.js
./node_modules/.bin/webpack --config webpack.config.api.js
./node_modules/.bin/webpack --config webpack.config.member.js

# cause bower do not allow execute in root
# so change into another user to install all front-end package we need.
useradd -ms /bin/bash newuser
chown -R newuser:newuser .
sudo -u newuser -H sh -c "python3 /code/manage.py bower install"

# build all text mining model
# if may take few hours to few days
echo "build model in language ${1}"；

# migrate
python3 manage.py migrate

# build model kcm
python3 manage.py buildKcm --lang ${1} --cpus 20
# # build model KEM
python3 manage.py buildkem --lang ${1} --dimension 400
# build model kcem
python3 manage.py buildkcem --lang ${1} --cpus 6
# build model PMI
python3 manage.py buildPMI --lang ${1}
# build model TF
python3 manage.py buildTfidf --lang ${1}
echo '-----------------------------------'
echo "all api is available now"
echo "only some duplicate key of kcem need to be merged"
echo "this process would take some times, maybe few days to few weeks"
echo "but it's totally ok to skip this process"
echo '-----------------------------------'
python3 manage.py mergeKcem --lang ${1}
exit 0