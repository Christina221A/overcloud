function jumpToSignIn(){
    window.location.href = "signIn";
}
document.addEventListener('DOMContentLoaded', function(){
    // console.log("index.js");
    document.querySelector('#signIn').onclick = jumpToSignIn;
});