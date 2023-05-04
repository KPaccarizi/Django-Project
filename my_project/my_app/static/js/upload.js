function openModal(img) {
    var modal = document.createElement("div");
    modal.className = "modal";
    var modalImg = document.createElement("img");
    modalImg.src = img.src;
    modalImg.alt = img.alt;
    modal.appendChild(modalImg);
    document.body.appendChild(modal);
    modal.addEventListener("click", closeModal);
  }
  
  function closeModal(event) {
    if (event.target.className == "modal") {
      event.target.parentNode.removeChild(event.target);
    }
  }
  