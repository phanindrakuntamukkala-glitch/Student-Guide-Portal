const eye=document.getElementById("togglePassword");

const pass=document.getElementById("password");

eye.onclick=function(){

if(pass.type==="password"){

pass.type="text";

eye.classList.replace("fa-eye","fa-eye-slash");

}
else{

pass.type="password";

eye.classList.replace("fa-eye-slash","fa-eye");

}

}