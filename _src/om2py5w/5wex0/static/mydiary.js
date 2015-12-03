function validate(){
    var diary = document.forms["myform"]["diary"].value;
    var tag   = document.forms["myform"]["tag"].value;
    if (diary == null || diary == "") {
        alert("日记为空不能提交哦!!"); 
        return false;
    }
    if (tag == null || tag == "") {
        alert("标签不能为空!!");
        return false;
    }
}