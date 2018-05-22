<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>検索結果表示</title>
</head>
<body>
    元データ<BR/>
    {{org_data}}
    <table>
        <caption>
        <strong>検索結果：{{query}}</strong>
        <details>
        <p>検索結果を表示する</p>
        </details>
        </caption>
        <thead>
        <tr><th>投稿時間</th><th>本文</th><th>アカウント名</th></tr>
        </thead>
        <tbody>
            {{tables}}
        </tbody>
        </table>
</body>
</html>
