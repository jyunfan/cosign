function gen_birth() {
    var y;
    for (y=2000; y>=1900; y--)
        jQuery('<option/>').attr('value',y).text(y).appendTo(jQuery("select#birthyear"));
    var m; 
    for (m=1; m<=12; m++)
        jQuery('<option/>').attr('value',m).text(m).appendTo(jQuery("select#birthmonth"));
    var d;
    for (d=1; d<=31; d++)
        jQuery('<option/>').attr('value',d).text(d).appendTo(jQuery("select#birthdate"));
}
