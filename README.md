# Managing Jenkins Proccesses

**Creating User Script:** 

> **Info:** You can create multiple user at once

You should create `config.json` file and edit.

```shell
cp config.json.sample config.json
vi config.json
```
You should create users.txt command below
```shell
cat >> greetings.txt <<EOL
test_user testtest
test_user2 testtest
EOL
```
You should run this script on your jenkins master as command below
```shell
python create_user.py
```
---
