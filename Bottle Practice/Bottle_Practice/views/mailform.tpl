<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>メールフォームページ</title>
</head>
<body>
<form action="/my-handling-form-page" method="post">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name_val"/>
    </div>
    <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail"  name="mail_val"/>
    </div>
    <div>
        <label for="msg">Message:</label>
        <textarea id="msg"  name="msg_val"></textarea>
    </div>
    <div>
        <input type="submit" value="next">
    </div>
</form>
</body>
</html>