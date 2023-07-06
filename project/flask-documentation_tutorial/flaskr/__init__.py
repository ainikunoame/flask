import os

from flask import Flask


def create_app(test_config=None):
    # アプリの作成と設定
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # インスタンスのコンフィグが存在すれば、それをロードする。
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 渡された場合、テスト設定をロードする。
        app.config.from_mapping(test_config)

    # インスタンスフォルダが存在することを確認する
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 「こんにちは」というシンプルなページ
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app