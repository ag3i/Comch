# 概要
Slackのスラッシュコマンドでチャンネルにメンバーを招待
# necessary
Slack Api Token
# Read
AWS Lamdba上で動くこと前提に書いています

Slackの仕様上、3秒以内にレスポンスを返さないとtimeoutしてしまうので、mainの関数を非同期で呼び出しています。
