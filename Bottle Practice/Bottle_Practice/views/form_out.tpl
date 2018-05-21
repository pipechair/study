<!DOCTYPE html>
<html>
    <head>
        <title>
                フォーム読み込み
        </title>
    </head>
    <body>
        name : {{name_val}}<br/>
        mail : {{mail_val}}<br/>
        msg : {{msg_val}}<br/>
        <form action="/send_mail" method="post">
            <input type="hidden" id="name" name="name_val" value="{{name_val}}"/>
            <input type="hidden" id="mail" name="mail_val" value="{{mail_val}}"/>
            <input type="hidden" id="msg" name="msg_val" value="{{msg_val}}"/>
            <input type="submit" value="next"/>
        </form>
        <form action="/top">
            <!-- 単に戻るだけのボタンなら、POSTの定義は不要。form の action だけ設定されていれば十分 -->
            <input type="submit" value="return"/>
        </form>
        
    </body>

</html>