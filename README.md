<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
        }
        .logo {
            width: 100px;
        }
        h1 {
            font-size: 36px;
            color: #4da8da;
        }
        h2 {
            font-size: 24px;
            margin-top: 20px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        a {
            color: #4da8da;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            background: rgba(77, 168, 218, 0.2);
            padding: 8px 12px;
            border-radius: 5px;
        }
        a:hover {
            background: rgba(77, 168, 218, 0.4);
        }
    </style>
</head>
<body>

    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" alt="Django Logo" class="logo">
        <h1>Django</h1>
        
        <p>
            Django, hızlı geliştirme ve temiz, pragmatik tasarım için oluşturulmuş bir web çerçevesidir. 
            Geliştiricilerin hızlı ve güvenli web uygulamaları oluşturmasına yardımcı olur.
        </p>

        <h2>Özellikler</h2>
        <ul>
            <li><a href="#">Güçlü URL Yönlendirme</a></li>
            <li><a href="#">Yerleşik Admin Paneli</a></li>
            <li><a href="#">Güvenlik Mekanizmaları</a></li>
            <li><a href="#">ORM ile Veri Tabanı Yönetimi</a></li>
            <li><a href="#">Cache Desteği</a></li>
            <li><a href="#">Gerçek Zamanlı İşlem Desteği</a></li>
        </ul>
    </div>

</body>
</html>
