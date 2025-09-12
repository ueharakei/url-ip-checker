# Pythonの公式イメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# アプリケーションがリッスンするポートを公開
EXPOSE 8080

# アプリケーションを実行
CMD ["python", "app.py"]