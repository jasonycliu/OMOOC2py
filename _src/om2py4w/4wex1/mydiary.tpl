<html>
<head><title>WEB-101</title> </head>
<body>
    <form action='/' method='post'>    
        笔记:<input name="diary" type="text"/>
            <input value="提交" type="submit" /> 
    </form>
    <div>以下是日记内容:</div>
    <textarea cols=60 rows=30>{{diary}}</textarea>
</body>
</html>