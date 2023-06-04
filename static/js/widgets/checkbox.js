window.onload = () => {
  var checkbox = document.getElementById("id_trending");
  checkbox.classList.add("my-checkbox");
  var label = document.createElement("label");
  label.setAttribute("for", "id_trending");
  label.classList.add("my-label");
  checkbox.insertAdjacentElement("afterend", label);


  var checkbox2 = document.getElementById("id_enabled");
  checkbox2.classList.add("my-checkbox-enabled");
  var label2 = document.createElement("label");
  label2.setAttribute("for", "id_enabled");
  label2.classList.add("my-label-enabled");
  checkbox2.insertAdjacentElement("afterend", label2);
};
