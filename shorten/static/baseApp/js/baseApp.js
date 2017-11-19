function copyToClipboard() {
    var copyText = document.getElementById("shortUrl");
    copyText.select();
    document.execCommand("Copy");
    alert("Copied the text: " + copyText.value);
}