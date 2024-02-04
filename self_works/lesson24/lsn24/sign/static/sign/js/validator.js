const form = document.querySelector("#form");

form.addEventListener("submit", (e) => {
  const pass = document.getElementById("id_password").value;
  const repeatPass = document.getElementById("id_repeat_password").value;

    console.log(pass===repeatPass)
});