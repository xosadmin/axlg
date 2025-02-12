function copycontent(flag) {
    var copyText = document.getElementById(flag);
    copyText.select();
    document.execCommand("Copy");
    alert("IP Address Copied");
}

function doActions(type) {
    var value = document.getElementById("dstaddr").value;
    document.getElementById("lgResult").style.display = "none";
    const Http = new XMLHttpRequest();
    const url='/process/' + type + "/" + value;
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = (e) => {
        if (Http.readyState === 4 && Http.status === 200) {
            document.getElementById("lgResult").innerHTML = Http.responseText;
            document.getElementById("lgResult").style.display = "block";
        }
    }
}